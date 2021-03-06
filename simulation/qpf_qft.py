from pyqpanda import *
from simple_number_theory import *
import numpy as np
import matplotlib
matplotlib.use('TkAgg')

# 使用 pyqpanda 搭建量子电路模拟量子周期查找算法

def CCR(c1: Qubit, c2: Qubit, tar: Qubit, theta: float) -> QCircuit :
    # 双受控相移门
    circ = QCircuit()
    circ << CR(c1, tar, theta/2) << CR(c2, tar, theta/2)
    circ << CNOT(c1, c2) << CR(c2, tar, -theta/2) << CNOT(c1, c2)
    return circ

def CSWAP(c: Qubit, x: Qubit, y: Qubit) -> QCircuit :
    # 受控交换门
    circ = QCircuit()
    circ << CNOT(y,x) << Toffoli(c,x,y) << CNOT(y,x)
    return circ

def Rotate(
        tar: Qubit, theta: float,
        c1: Qubit or None,
        c2: Qubit or None,
    ) -> QGate :
    # （受控）旋转门

    if   (c1 == None and c2 == None) : return U1(tar, theta)
    elif (c1 != None and c2 != None) : return CCR(c1, c2, tar, theta)
    else : return CR(c1 if c1 != None else c2, tar, theta)

##############################################################################################

def PHI_ADD(
        x: QVec, a: int,
        c1: Qubit or None = None, 
        c2: Qubit or None = None,
    ) -> QCircuit :
    # （受控）相位加法门
    # |φ(x)>  -->  |φ(x+a)>

    q = len(x)
    Q = 2**q
    a = (a % Q + Q) % Q

    circ = QCircuit()
    for i in range(q) :
        if a >> (q-1-i) & 1 :
            for j in range(i+1) :
                circ << Rotate(x[j], np.pi * 2**(j-i), c1, c2)
    return circ

def ADD(
        x: QVec, a: int,
        c1: Qubit or None = None,
        c2: Qubit or None = None,
    ) -> QCircuit :
    # （受控）模 2^q 加法门
    # |x>  -->  |φ(x)>  -->  |φ(x+a)>  -->  |(x+a)%(2^q)>

    circ = QCircuit()
    circ << QFT(x) << PHI_ADD(x, a, c1, c2) << QFT(x).dagger()
    return circ

def MOD_ADD(
        x: QVec, mod_ancilla: QVec,
        a: int, N: int,
        c1: Qubit or None = None, 
        c2: Qubit or None = None,
    ) -> QCircuit :
    # （受控）模 N 加法门，需要两个辅助位
    # |x>  -->  |x+a-N>      -->  |(x+a)%N>    -->  |(x+a)%N-a>  -->  |(x+a)%N>
    # |0>  -->  |[x+a-N<0]>  -->  |[x+a-N<0]>  -->  |0>          -->  |0>
    # 为了减少 QFT 次数，在真实应用中使用的是 |φ(x)>  -->  |φ((x+a)%N)>

    a = (a % N + N) % N
    q = len(x)
    circ = QCircuit()

    b = QVec(x.to_list() + [mod_ancilla[1]]) # 最高位增加一位用于判断溢出

    circ <<  ADD(b, a, c1, c2)
    circ <<  ADD(b, -N)
    circ << CNOT(b[q], mod_ancilla[0])
    circ <<  ADD(b, N, mod_ancilla[0])

    circ <<  ADD(b, -a, c1, c2)
    circ <<  X(b[q]) << CNOT(b[q], mod_ancilla[0]) << X(b[q])
    circ <<  ADD(b, a, c1, c2)

    return circ

def CMULT(
        x: QVec, y: QVec, mod_ancilla: QVec,
        a: int, N: int,
        c: Qubit or None = None,
    ) -> QCircuit :
    # （受控）模 N 乘法门
    # |x>  -->  |x>
    # |y>  -->  |(y+a*x)%N>

    a = (a % N + N) % N
    q = len(x)
    circ = QCircuit()

    for i in range(q) :
        circ << MOD_ADD(y, mod_ancilla, qpow(2,i,N) * a % N, N, x[i], c)

    return circ

def U(
        x: QVec, y: QVec, mod_ancilla: QVec,
        a: int, N: int,
        c: Qubit or None = None,
    ) -> QCircuit :
    # （受控）模 N 乘法门
    # |x>  -->  |x>     -->  |ax%N>  -->  |ax%N>
    # |0>  -->  |ax%N>  -->  |x>     -->  |0>

    a = (a % N + N) % N
    b = N - inv(a, N)
    q = len(x)
    circ = QCircuit()

    circ << CMULT(x, y, mod_ancilla, a, N, c)
    for i in range(q) : circ << (CSWAP(c, x[i], y[i]) if c != None else SWAP(x[i], y[i]))
    circ << CMULT(x, y, mod_ancilla, b, N, c)

    return circ


##############################################################################################


def QPF_qft_slow_prob(a: int, N: int) : 
    # 使用 4n+2 个量子比特的量子周期查找算法，返回概率分布
    qvm = init_quantum_machine(QMachineType.CPU)

    q = 1
    while 2**q < N : q += 1

    work = qvm.qAlloc_many(q*2)
    mult = qvm.qAlloc_many(q)
    mult_ancilla = qvm.qAlloc_many(q)
    mod_ancilla = qvm.qAlloc_many(2)

    prog = QProg()
    prog << X(mult[0])
    prog << H(work)

    aa = a
    for i in range(len(work)) :
        prog << U(mult, mult_ancilla, mod_ancilla, aa, N, work[i])
        aa = aa ** 2 % N

    prog << QFT(work).dagger()
    # QFT_dagger = QCircuit()
    # for i in range(q) :
    #     QFT_dagger << SWAP(work[i], work[2*q-i-1])
    # for i in range(2*q) :
    #     QFT_dagger << H(work[i])
    #     for j in range(i+1,2*q) :
    #         QFT_dagger << CR(work[i], work[j], np.pi / 2**(j-i)).dagger()
    # prog << QFT_dagger

    result = prob_run_list(prog, work, -1)
    destroy_quantum_machine(qvm)
    return result

def QPF_qft_fast(a: int, N: int, times: int) : 
    # 使用 2n+3 个量子比特的量子周期查找算法
    # 由于使用的 QIF, 无法获得概率分布
    qvm = init_quantum_machine(QMachineType.CPU)

    q = 1
    while 2**q < N : q += 1

    work = qvm.qAlloc()
    mult = qvm.qAlloc_many(q)
    mult_ancilla = qvm.qAlloc_many(q)
    mod_ancilla = qvm.qAlloc_many(2)
    cbits = qvm.cAlloc_many(q*2)

    prog = QProg()
    prog << X(mult[0])

    A = [a]
    for i in range(q*2-1) :
        A.append(A[-1]**2 % N)

    for i in range(q*2) :
        prog << H(work)
        prog << U(mult, mult_ancilla, mod_ancilla, A[q*2-i-1], N, work)
        
        ### 这里是一个 IQFT
        for j in range(i) :
            prog << QIfProg(cbits[j], U1(work, np.pi / 2**(i-j)).dagger()) # 改为使用传统比特控制旋转
        prog << H(work)
        ###

        prog << Measure(work, cbits[i])
        prog << QIfProg(cbits[i], X(work)) # 置0

    result = run_with_configuration(prog, cbits, times)
    destroy_quantum_machine(qvm)
    return result


import matplotlib.pyplot as plt

# if __name__ == '__main__' :
#     a = 3
#     N = 7
#     P = QPF_qft_slow_prob(a, N)
#     plt.bar([i for i in range(len(P))], P)
#     plt.show()

if __name__ == '__main__' :
    a = 3
    N = 7
    times = 4096 # 这可能需要运行比较长的时间（10分钟或更多）
    Q = 1
    while Q < N :
        Q <<= 1
    Q = Q ** 2

    result = QPF_qft_fast(a, N, times)
    P = [0 for i in range(Q)]
    for (k,v) in result.items() :
        P[int(k,2)] += v / times
    plt.bar([i for i in range(len(P))], P)
    plt.show()
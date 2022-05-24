from pyqpanda import *
from simple_number_theory import *
import numpy as np

import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

def plot(result) :
    result = [(k,v) for (k,v) in result.items()]
    result.sort(key = lambda x:x[1], reverse = True)
    print(result)
    result_type = [int(i[0],2) for i in result]
    result_frequency = [i[1] for i in result]
    plt.bar(result_type, result_frequency, align = 'center')
    plt.show()

def CCR(c1: Qubit, c2: Qubit, tar: Qubit, theta: float) -> QCircuit :
    circ = QCircuit()
    circ << CR(c1, tar, theta/2) << CR(c2, tar, theta/2)
    circ << CNOT(c1, c2) << CR(c2, tar, -theta/2) << CNOT(c1, c2)
    return circ

def CSWAP(c: Qubit, x: Qubit, y: Qubit) -> QCircuit :
    circ = QCircuit()
    circ << CNOT(y,x) << Toffoli(c,x,y) << CNOT(y,x)
    return circ

def Rotate(
        tar: Qubit, theta: float,
        c1: Qubit or None,
        c2: Qubit or None,
    ) -> QGate :

    if   (c1 == None and c2 == None) : return U1(tar, theta)
    elif (c1 != None and c2 != None) : return CCR(c1, c2, tar, theta)
    else : return CR(c1 if c1 != None else c2, tar, theta)

def PHI_ADD(
        qubits: QVec, a: int,
        c1: Qubit or None = None, 
        c2: Qubit or None = None,
    ) -> QCircuit :

    q = len(qubits)
    Q = 2**q
    a = (a % Q + Q) % Q

    circ = QCircuit()
    for i in range(q) :
        if a >> (q-1-i) & 1 :
            for j in range(i+1) :
                circ << Rotate(qubits[j], np.pi * 2**(j-i), c1, c2)
    return circ

def ADD(
        qubits: QVec, a: int,
        c1: Qubit or None = None,
        c2: Qubit or None = None,
    ) -> QCircuit :

    # |b>  -->  |(b+a)%(2^q)>

    circ = QCircuit()
    circ << QFT(qubits) << PHI_ADD(qubits, a, c1, c2) << QFT(qubits).dagger()
    return circ

def MOD_ADD(
        qubits: QVec, mod_ancilla: QVec,
        a: int, N: int,
        c1: Qubit or None = None, 
        c2: Qubit or None = None,
    ) -> QCircuit :

    # |b>  -->  |(b+a)%N>
    # |0>  -->  |0>

    a = (a % N + N) % N
    q = len(qubits)
    circ = QCircuit()

    b = QVec(qubits.to_list() + [mod_ancilla[1]])

    circ <<  ADD(b, a, c1, c2)
    circ <<  ADD(b, -N)
    circ << CNOT(b[q], mod_ancilla[0])
    circ <<  ADD(b, N, mod_ancilla[0])

    circ <<  ADD(b, -a, c1, c2)
    circ <<  X(b[q]) << CNOT(b[q], mod_ancilla[0]) << X(b[q])
    circ <<  ADD(b, a, c1, c2)

    return circ

def MULT_ADD(
        x: QVec, y: QVec, mod_ancilla: QVec,
        a: int, N: int,
        c: Qubit or None = None,
    ) -> QCircuit :

    # |x>  -->  |x>
    # |y>  -->  |(y+a*x)%N>

    a = (a % N + N) % N
    q = len(x)
    circ = QCircuit()

    for i in range(q) :
        circ << MOD_ADD(y, mod_ancilla, qpow(2,i,N) * a % N, N, x[i], c)

    return circ

def MULT(
        x: QVec, y: QVec, mod_ancilla: QVec,
        a: int, N: int,
        c: Qubit or None = None,
    ) -> QCircuit :

    # |x,0>  -->  |x,ax%N>  -->  |ax%N,x>  -->  |ax%N,0>

    a = (a % N + N) % N
    b = N - inv(a, N)
    q = len(x)
    circ = QCircuit()

    circ << MULT_ADD(x, y, mod_ancilla, a, N, c)
    for i in range(q) : circ << (CSWAP(c, x[i], y[i]) if c != None else SWAP(x[i], y[i]))
    circ << MULT_ADD(x, y, mod_ancilla, b, N, c)

    return circ

def QPF(a: int, N: int) -> int :
    qvm = init_quantum_machine(QMachineType.CPU)

    q = 1
    while 2**q < N : q += 1

    work = qvm.qAlloc_many(q*2)
    mult = qvm.qAlloc_many(q)
    mult_ancilla = qvm.qAlloc_many(q)
    mod_ancilla = qvm.qAlloc_many(2)

    prog = QProg()
    prog << X(mult[0]) << H(work)

    aa = a
    for i in range(q) :
        prog << MULT(mult, mult_ancilla, mod_ancilla, aa, N, work[i])
        aa = aa ** 2 % N

    prog << QFT(work).dagger()

    result = prob_run_dict(prog, work, -1)
    plot(result)

    destroy_quantum_machine(qvm)

if __name__ == "__main__":
    QPF(4, 7)
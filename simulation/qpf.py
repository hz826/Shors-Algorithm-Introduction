from qpf_fft import qpf_fft_slow, qpf_fft_fast
from qpf_qft import qpf_qft_slow
import matplotlib.pyplot as plt

def QPF(a, N, mode='qpf_fft_fast') :
    # 使用不同算法模拟量子周期查找，这些算法会返回相同的值
    # fft 算法模拟
    if   mode == 'qpf_fft_slow' : return qpf_fft_slow(a, N) # O(r N^2 log N)
    elif mode == 'qpf_fft_fast' : return qpf_fft_fast(a, N) # O(N^2 log N)
    # pyqpanda 模拟
    elif mode == 'qpf_qft_slow' : return qpf_qft_slow(a, N) # 4n+2 qubits


if __name__ == '__main__' :
    a = 2
    N = 13

    plt.subplot(121)
    P = QPF(a, N, mode='qpf_fft_fast')
    plt.bar([i for i in range(len(P))], P)
    plt.subplot(122)
    P = QPF(a, N, mode='qpf_qft_slow')
    plt.bar([i for i in range(len(P))], P)

    plt.show()
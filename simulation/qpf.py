from qpf_fft import QPF_fft_slow_prob, QPF_fft_fast_prob
from qpf_qft import QPF_qft_slow_prob, QPF_qft_fast
import matplotlib.pyplot as plt
import random

# 量子周期查找算法

def QPF_prob(a, N, mode='qpf_fft_fast') :
    # 使用不同算法模拟量子周期查找，返回概率分布（这些算法会返回相同的概率分布）
    # fft 算法模拟
    if   mode == 'qpf_fft_slow' : return QPF_fft_slow_prob(a, N) # O(r N^2 log N)
    elif mode == 'qpf_fft_fast' : return QPF_fft_fast_prob(a, N) # O(N^2 log N)
    # pyqpanda 模拟
    elif mode == 'qpf_qft_slow' : return QPF_qft_slow_prob(a, N) # 4n+2 qubits

last_query = ()
last_result = []

def QPF(a, N, mode='qpf_fft_fast') :
    # 使用不同算法模拟量子周期查找，返回测量值
    global last_query  # (a, N, mode)
    global last_result # 缓存概率分布，加快计算
    
    if mode in ['qpf_fft_slow', 'qpf_fft_fast', 'qpf_qft_slow'] :
        if (a, N, mode) != last_query :
            last_query = (a, N, mode)
            last_result = QPF_prob(a, N, mode)
        return random.choices([i for i in range(len(last_result))], weights=last_result)[0]
    elif mode == 'qpf_qft_fast' : 
        return QPF_qft_fast(a, N, 1).keys()[0] # 2n+3 qubits


if __name__ == '__main__' :
    a = 2
    N = 13

    plt.subplot(121)
    P = QPF_prob(a, N, mode='qpf_fft_fast')
    plt.bar([i for i in range(len(P))], P)
    plt.subplot(122)
    P = QPF_prob(a, N, mode='qpf_qft_slow')
    plt.bar([i for i in range(len(P))], P)

    plt.show()
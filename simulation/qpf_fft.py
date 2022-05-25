from simple_number_theory import *
from scipy.fft import fft
import numpy as np

# 使用 fft 模拟量子计算机，返回测量得到每一个数的概率

def qpf_fft_slow(a, mod, n=None) :
    if n == None :
        n = 1
        while n < mod**2 : n <<= 1

    A = [[] for i in range(mod)]
    for i in range(n) :
        A[qpow(a, i, mod)].append(i)

    P = np.zeros(n)

    for m in range(mod) :
        if len(A[m]) == 0 :
            continue

        B = np.zeros(n)
        for i in A[m] :
            B[i] += 1/n
        B = fft(B)
        P += abs(B) ** 2
    return P


def qpf_fft_fast(a, mod, n=None) :
    if n == None :
        n = 1
        while n < mod**2 : n <<= 1
    
    r = ord(a, mod)
    P = np.zeros(n)
    # n == (n%r) * (n//r+1) + (r-n%r) * (n//r)

    if n%r > 0 :
        B = np.zeros(n)
        for i in range(n//r+1) :
            B[i*r] += 1/n
        B = fft(B)
        P += (n%r) * (abs(B)**2)
    
    B = np.zeros(n)
    for i in range(n//r) :
        B[i*r] += 1/n
    B = fft(B)
    P += (r-n%r) * (abs(B)**2)
    
    return P
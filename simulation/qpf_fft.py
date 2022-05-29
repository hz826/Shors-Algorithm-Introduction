from simple_number_theory import *
from scipy.fft import fft
import numpy as np

# 使用 fft 模拟量子计算机，返回测量得到每一个数的概率

def QPF_fft_slow_prob(a, N, Q=None) :
    if Q == None :
        Q = 1
        while Q < N : Q <<= 1
        Q = Q**2

    A = [[] for i in range(N)]
    for i in range(Q) :
        A[qpow(a, i, N)].append(i)

    P = np.zeros(Q)

    for m in range(N) :
        if len(A[m]) == 0 :
            continue

        B = np.zeros(Q)
        for i in A[m] :
            B[i] += 1/Q
        B = fft(B)
        P += abs(B) ** 2
    return P


def QPF_fft_fast_prob(a, N, Q=None) :
    if Q == None :
        Q = 1
        while Q < N**2 : Q <<= 1
    
    r = ord(a, N)
    P = np.zeros(Q)
    # Q == (Q%r) * (Q//r+1) + (r-Q%r) * (Q//r)

    if Q%r > 0 :
        B = np.zeros(Q)
        for i in range(Q//r+1) :
            B[i*r] += 1/Q
        B = fft(B)
        P += (Q%r) * (abs(B)**2)
    
    B = np.zeros(Q)
    for i in range(Q//r) :
        B[i*r] += 1/Q
    B = fft(B)
    P += (r-Q%r) * (abs(B)**2)
    
    return P
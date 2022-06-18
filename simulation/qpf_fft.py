from simple_number_theory import *
from scipy.fft import fft
import numpy as np
import random

# 使用 fft 模拟量子计算机允许结果，返回测量得到每一个数的概率

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
        while Q < N : Q <<= 1
        Q = Q**2
    
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

def QPF_fft_fast(a, N, times, width=20, Q=None) :
    if Q == None :
        Q = 1
        while Q < N : Q <<= 1
        Q = Q**2
    
    r = ord(a, N)

    def f(x,m) :
        if r*x % Q == 0 :
            return m**2 / Q**2
        theta = np.pi*r*x/Q
        return np.sin(theta*m)**2 / np.sin(theta)**2 / Q**2
    
    def g(x) :
        return (Q%r) * f(x,Q//r+1) + (r-Q%r) * f(x,Q//r)

    A = [x for x in np.unique([int(Q*i/r+0.5+j) for i in range(r) for j in range(-width+1,width)]).tolist() if 0 <= x and x < Q]
    P = [g(x) for x in A]
    return random.choices(A, weights=P, k=times)


import matplotlib.pyplot as plt
if __name__ == '__main__' :
    a = 2
    N = 7
    times = 2048

    result = QPF_fft_fast(a, N, times) 
    P = [0 for i in range(64)]
    for k in result :
        P[k] += 1 / times
    plt.bar([i for i in range(len(P))], P)
    plt.show()
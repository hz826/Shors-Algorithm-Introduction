from simple_number_theory import *
import random
import math
import numpy as np
from scipy.fft import fft
from fractions import Fraction
import matplotlib.pyplot as plt

def qft_simu_standard(a, mod, n) :
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

def qft_simu_fast(a, mod, n) :
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

def qft_simu(*args) :
    # return qft_simu_standard(*args)
    return qft_simu_fast(*args)

def period_finding(a, mod) :
    n = 1
    while n < mod**2 : n <<= 1
    P = qft_simu(a, mod, n)

    while True :
        c = random.choices([i for i in range(len(P))], weights=P)[0]
        # c/q = d/r
        f = Fraction(c,n).limit_denominator(mod) # stern brocot tree
        r = f.denominator
        print('        ', Fraction(c,n), f)

        if qpow(a, r, mod) == 1 :
            while r%2 == 0 and qpow(a, r//2, mod) == 1 :
                r //= 2
            return r


def shor(N) :
    if N%2 == 0 :
        print('  SPECIAL CASE')
        return 2
    
    if isprime(N) :
        print('  ERROR IT\'s A PRIME')
        return -1
    
    for k in range(2, int(math.log(N,3))+2) :
        sq = int(N ** (1/k) + 0.5)
        if sq**k == N :
            print('  SPECIAL CASE')
            return sq
    
    while True :
        a = random.randint(1, N-1)
        print('  TRY   a =', a)

        if gcd(a, N) != 1 :
            print('  GET  NOT-COPRIME')
            return gcd(a, N)
        
        r = period_finding(a, N)
        print('  QPF   r =', r)
        if r%2 == 1 :
            print('  FAIL  r%2==1\n')
            continue

        b = qpow(a, r//2, N)
        if b == N-1 : 
            print('  FAIL  b==N-1\n')
            continue

        print('  GET  SHOR')
        return gcd(b-1, N)


def shor_test(N) :
    if N <= 1 or isprime(N) :
        return

    print('-' * 20, end='\n\n')
    print('BEGIN  N =', N)

    d = shor(N)
    if (d <= 1 or d >= N or N % d != 0) : 
        print('!!! ERROR !!!')
        exit(1)
    
    print('END   FOUND', [d, N//d], end='\n\n')


if __name__ == '__main__' :
    for i in range(1000,1100) :
        if i%2 == 0 : continue
        # if isprime(i) : continue

        shor_test(i)
from qpf import QPF
from simple_number_theory import *
import math
from fractions import Fraction
from qpf import QPF

def period_finding(a, N) :
    # 周期查找算法，需要使用量子计算机才具有优势

    q = 1
    while 2**q < N : q += 1
    Q = 2**(q*2)

    while True :
        c = QPF(a, N) # 搭建量子电路并测量
        
        # c/Q = d/r
        f = Fraction(c,Q).limit_denominator(N) # 使用 stern brocot tree 找到分母在一定范围内时最近的一个分数
        r = f.denominator
        print('        ', Fraction(c,Q), ' -> ', f)
        # 可以证明 f 的分母是 r 或者 r 的约数，如果是 r 的约数则需要重新进行此步骤

        if qpow(a, r, N) == 1 :
            return r

def shor(N) :
    # shor 算法，传入大整数 N ，返回 N 的一个非平凡因子

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
    # 传入 N ，测试 shor 算法的正确性
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
        shor_test(i)
# 一个简单的数论函数库

def qpow(a, x, m) :  # 快速幂，O(log x) 求 a^x % m
    r = 1
    while x > 0 :
        if x & 1 : 
            r = r * a % m
        a = a * a % m
        x >>= 1
    return r

def gcd(a, b) : # 最大公约数，O(log n)
    while b > 0 :
        (a,b) = (b,a%b)
    return a

def exgcd(a, b) : # 欧几里得算法，O(log n)，对于输入的 (a,b)，找到一组 (x,y) 满足 ax+by=gcd(a,b)
    if b == 0 :
        return (1,0,a)
    (y,x,g) = exgcd(b,a%b)
    return (x,y-x*(a//b),g)

def inv(a, m) : # 求乘法逆元，O(log n)，对于与 m 互质的 a，找到 b 满足 a*b%m=1
    (x,y,g) = exgcd(a,m)
    return (x%m + m) % m

def isprime(n) : # 判断一个数是否是质数
    if n <= 1 :
        return False
    i = 2
    while i*i <= n :
        if n%i == 0 :
            return False
        i += 1
    return True

def factorize(n) : # 分解质因数
    f = []
    i = 2
    while i*i <= n :
        if n%i == 0 :
            cnt = 0
            while n%i == 0 :
                n //= i
                cnt += 1
            f.append((i,cnt))
        i += 1
    if n>1 :
        f.append((n,1))
    return f

def phi(n) : # 求欧拉函数 phi(n)
    f = factorize(n)
    for (p,a) in f :
        n //= p
        n *= (p-1)
    return n

def ord(a, n) : # 求阶，即最小的正整数 r 满足 a^r%n=1，要求 a,n 互质
    r = 1
    b = a % n
    while b != 1 :
        b = b * a % n
        r += 1
    return r

def f2(n) : # 求一个数 2 的因子次数
    return 0 if n&1 else f2(n>>1)+1
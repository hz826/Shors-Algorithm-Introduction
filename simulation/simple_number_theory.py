def qpow(a, x, m) : # a^x % m
    r = 1
    while x > 0 :
        if x & 1 : 
            r = r * a % m
        a = a * a % m
        x >>= 1
    return r

def gcd(a, b) :
    while b > 0 :
        (a,b) = (b,a%b)
    return a

def exgcd(a, b) :
    if b == 0 :
        return (1,0,a)
    (y,x,g) = exgcd(b,a%b)
    return (x,y-x*(a//b),g)

def isprime(n) :
    if n <= 1 :
        return False
    i = 2
    while i*i <= n :
        if n%i == 0 :
            return False
        i += 1
    return True

def factorize(n) :
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

def phi(n) :
    f = factorize(n)
    for (p,a) in f :
        n //= p
        n *= (p-1)
    return n

def ord(g, n) :
    cnt = 1
    a = g % n
    while a != 1 :
        a = a * g % n
        cnt += 1
    return cnt

def f2(n) :
    return 0 if n&1 else f2(n>>1)+1
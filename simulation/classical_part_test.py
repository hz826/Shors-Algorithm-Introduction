from simple_number_theory import *

def show_mod(x, f) :
    print(x, end=" | ")
    mod = []
    for (p,a) in f :
        mod.append(x % (p**a))
    print(mod)

def test_ntsr(n) :
    f = factorize(n)
    ntsr = [i for i in range(1,n) if (i*i%n == 1 and i != 1 and i != n-1)]
    print('n = ', n, ' frac = ', f, ' ntsr = ', ntsr)
    for x in ntsr : 
        show_mod(x, f)

def test_r1(n) :
    G = [(i,ord(i,n)) for i in range(1,n) if gcd(i,n)==1]
    cnt = sum(1 for (a,r) in G if r%2==0)
    print('n = ', n, 'success rate = ', cnt/len(G))

def test_r2(n) :
    G = [(i,ord(i,n)) for i in range(1,n) if gcd(i,n)==1]
    cnt = sum(1 for (a,r) in G if r%2==0 and qpow(a,r//2,n) not in [1, n-1])
    print('n = ', n, 'success rate = ', cnt/len(G))

def test_r3(n) :
    f = factorize(n)
    if len(f) <= 1 or n%2==0 : return

    G = [(i,ord(i,n)) for i in range(1,n) if gcd(i,n)==1]
    F1 = [(a,r) for (a,r) in G if r%2==1]
    F2 = [(a,r) for (a,r) in G if r%2==0 and qpow(a,r//2,n) == n-1]

    print('n=', n)
    print((len(F1)+len(F2)) / len(G))
    
    res = 0
    i = 0
    while True :
        cnt = 1
        for (p,alpha) in f :
            m = phi(p**alpha)

            if i == 0 :
                cnt *= 2**-f2(m)
            elif i <= f2(m) :
                cnt *= 2**-(f2(m)-i+1)
            else :
                cnt *= 0
        
        if cnt == 0 : break
        res += cnt
        i += 1
    
    print(res, 1/res)

if __name__ == '__main__' :
    test_r3(35)
from qft_simulate import *

def test(a, mod) :
    r = ord(a, mod)
    n = 1
    while n < mod**2 : n <<= 1

    P = qft_simu_fast(a, mod, n)
    s = 0
    for j in range(n) :
        if min(j*r%n, n-j*r%n)*2 < r :
            s += P[j]
    print(mod, '\t', a, '\t', r, '\t', s)


# for i in range(20) :
#     mod = 35
#     a = mod
#     while gcd(a, mod) != 1 :
#         a = random.randint(1,mod-1)
#     test(a, mod)

mod = 23 * 31
for a in range(1,mod) :
    if gcd(a, mod) != 1 : continue
    test(a, mod)
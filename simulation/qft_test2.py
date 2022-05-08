from qft_simulate import *

def test(a, mod) :
    r = ord(a, mod)
    Q = 1
    while Q < mod**2 : Q <<= 1

    # print('a =', a, ' mod =', mod, ' r =', r, ' Q =', Q, ' Q//r =', Q//r, ' Pmin =', round(4/(np.pi**2 * r), 5))
    # print()

    P = qft_simu_fast(a, mod, Q)
    s = 0
    for y in range(Q) :
        if min(y*r%Q, Q-y*r%Q) <= r//2 :
            if P[y] < 4/(np.pi**2 * r) - 1e-8 :
                print('ERROR!!!')
                exit(0)

            f = Fraction(y,Q).limit_denominator(mod)
            d = (r//f.denominator)*f.numerator
            # print(y, round(P[y], 5), d, f)
            if f.denominator == r :
                s += P[y]
    print('Psuccess =', round(s,5), ' phi(r)/r = ', phi(r)/r, ' Pmin =', phi(r) * round(4/(np.pi**2 * r), 5))

mod = 11 * 17
for i in range(20) :
    a = mod
    while gcd(a, mod) != 1 : 
        a = random.randint(1,mod-1)
    test(a, mod)
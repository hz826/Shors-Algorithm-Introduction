from simple_number_theory import *

def shor_simulate(n) :
    print('-' * 20)
    success = 0
    for i in range(1,n) :
        if gcd(i,n) != 1 :
            print(i,0,end='')
            print('\t\tg', gcd(i,n))
            success += 1
        else :
            r = ord(i, n)
            print(i,r,end='')
            if r%2 != 0 :
                print('\tr')
            else :
                b = qpow(i, r//2, n)
                if b == n-1 :
                    print('\tb')
                else :
                    print('\t\ts', gcd(b-1, n))
                    success += 1
    print('Success rate =', success / (n-1))

shor_simulate(11*37)
shor_simulate(19*23)
'''
r : ERROR, r%2 == 1
b : ERROR, b=a^(r/2) == n-1

g : gcd
s : shor
'''
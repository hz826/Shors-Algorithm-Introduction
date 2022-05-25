from simple_number_theory import *

def shor_simulate(N) :
    # 模拟 shor 算法的传统部分，通过对随机的 a 求阶，找到 N 的一个非平凡因子
    # 对于所有的 a 显示计算结果，并计算成功率

    print('-' * 20)
    success = 0
    for a in range(1,N) :
        if gcd(a,N) != 1 :
            print(a, 0, end='')
            print('\t\tg', gcd(a, N))
            success += 1
        else :
            r = ord(a, N) # 在实际的 shor 算法中，这里使用量子计算机高效完成
            print(a, r, end='')
            if r%2 != 0 :
                print('\tr')
            else :
                b = qpow(a, r//2, N)
                if b == N-1 :
                    print('\tb')
                else :
                    print('\t\ts', gcd(b-1, N))
                    success += 1
    
    print('Success rate =', success / (N-1))
    # 可以证明这部分的成功率 > 1/2

shor_simulate(11*37)
# shor_simulate(19*23)
'''
r : ERROR, r%2 == 1
b : ERROR, b=a^(r/2) == N-1

g : gcd
s : shor
'''
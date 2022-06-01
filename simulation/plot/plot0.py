import numpy as np
from scipy.fft import fft
import matplotlib.pyplot as plt
from simple_number_theory import *

def f(n) :
    phin = phi(n)
    A = [0 for i in range(v2(phin)+1)]
    for i in range(1,n) :
        if gcd(i,n) != 1 :
            continue
        A[v2(ord(i,n))] += 1/phin
    return A

fig, ax = plt.subplots(2, 2)
plt.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=None, hspace=0.4)

n = 27
A = f(n)
print(sum(A))
ax[0, 0].bar([i for i in range(len(A))], A)
ax[0, 0].set_title('$n = ' + str(n) + '\\ \\varphi(n) = ' + str(phi(n)) + '$')

n = 25
A = f(n)
print(sum(A))
ax[0, 1].bar([i for i in range(len(A))], A)
ax[0, 1].set_title('$n = ' + str(n) + '\\ \\varphi(n) = ' + str(phi(n)) + '$')

n = 41
A = f(n)
print(sum(A))
ax[1, 0].bar([i for i in range(len(A))], A)
ax[1, 0].set_title('$n = ' + str(n) + '\\ \\varphi(n) = ' + str(phi(n)) + '$')

n = 289
A = f(n)
print(sum(A))
ax[1, 1].bar([i for i in range(len(A))], A)
ax[1, 1].set_title('$n = ' + str(n) + '\\ \\varphi(n) = ' + str(phi(n)) + '$')

plt.show()
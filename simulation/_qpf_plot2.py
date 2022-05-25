import numpy as np
from scipy.fft import fft
import matplotlib.pyplot as plt

# def DFT(n) :
#     A = np.zeros((n,n), dtype=complex)
#     for i in range(n) :
#         for j in range(n) :
#             A[i][j] = np.exp(2*np.pi/n*i*j * 1j)
#     return A / np.sqrt(n)

# A = DFT(6)
# B = np.conjugate(A.T)
# C = np.matmul(A, B)
# # print(A.round(2))
# print(C.round(2))

n = 128
r = 5

index = [i for i in range(n)]
A = np.array([1 if i%r==1 else 0 for i in range(n)])
B = fft(A)

plt.subplot(221)
plt.bar(index, abs(A)**2)

plt.subplot(222)
plt.bar(index, abs(B)**2)

A = np.array([1 if i%r==2 else 0 for i in range(n)])
B = fft(A)

plt.subplot(223)
plt.bar(index, abs(A)**2)

plt.subplot(224)
plt.bar(index, abs(B)**2)

plt.show()
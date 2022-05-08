from simple_number_theory import *
import numpy as np
from scipy.fft import fft
from fractions import Fraction
import random
import matplotlib.pyplot as plt

# w = [np.exp(2j*np.pi * i/n) for i in range(n)]

def calc(Q, r) :
    def f(theta) :
        w = np.exp(theta*1j)
        return abs((1-w**(Q//r)) / (1-w)) ** 2

    X = np.linspace(-np.pi, np.pi, 1000)
    Y = f(X)
    plt.plot(X, Y)


Q = 1024
r = 11
calc(Q, r)
plt.show()
from simple_number_theory import *
import numpy as np
from scipy.fft import fft
from fractions import Fraction
import random
import matplotlib.pyplot as plt

def calc(Q, r) :
    def f(theta) :
        w = np.exp(theta*1j)
        return (abs((1-w**(Q//r)) / (1-w)) ** 2) / Q**2

    X = np.linspace(-np.pi, np.pi, 1000)
    Y = f(X)
    plt.plot(X, Y)


Q = 256
r = 12
calc(Q, r)
plt.show()
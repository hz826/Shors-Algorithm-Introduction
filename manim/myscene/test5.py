from turtle import circle
from manim import *
import numpy as np
from numpy import sin, cos
from math import gcd

from sympy import rad

class Test(Scene) :
    def construct(self) :
        n = 21
        a = 5

        G = [i for i in range(1,n) if gcd(i,n) == 1]
        phi = len(G)
        
        C1 = Circle(radius=2.0)
        C2 = Circle(radius=2.5)
        P1 = [C1.point_at_angle((PI/2 - 2*PI/len(G) * i) % (2*PI)) for i in range(phi)]
        P2 = [C2.point_at_angle((PI/2 - 2*PI/len(G) * i) % (2*PI)) for i in range(phi)]

        dots = [Dot(P1[i]) for i in range(phi)]
        labels = [MathTex(str(G[i]), font_size=24).move_to(P2[i]) for i in range(phi)]
        arrows = [Arrow(P1[i], P1[G.index(G[i]*a%n)]) for i in range(phi)]

        self.add(*dots)
        self.add(*labels)
        self.add(*arrows)


import os
if __name__ == '__main__' :
    os.system('manim -pql myscene/test5.py Test')
from manim import *
import numpy as np
from numpy import sin, cos

class Test(Scene) :
    def construct(self) :
        w = 1
        h = 1
        s = 30
        n = 1 # line num
        m = 1 # gate num

        def get_pos(i, j) : # 0-index, the jth gate in the ith line
            return np.array([(-(m-1)/2+j)*w, ((n-1)/2-i)*h, 0])

        def wire(p0, p1) :
            p0 = get_pos(p0[0], p0[1])
            p1 = get_pos(p1[0], p1[1])
            return Create(Line(p0, p1))
        
        def init() :
            return LaggedStart(*[wire((i,-1), (i,m)) for i in range(n)], lag_ratio=0.2)
        
        def gate(p0, p1, text) :
            p0 = get_pos(p0[0], p0[1])
            p1 = get_pos(p1[0], p1[1])

            rect1 = Rectangle(width=abs(p0[0]-p1[0])+w*0.8, height=abs(p0[1]-p1[1])+h*0.8)
            rect1.shift((p0+p1)/2)
            rect2 = rect1.copy()
            rect2.set_stroke(opacity=0)
            rect2.set_fill(BLACK, opacity=1.0)

            t = MathTex(text, font_size=s).shift((p0+p1)/2)
            return AnimationGroup(Create(rect1), Succession(GrowFromEdge(rect2, LEFT), Write(t)))
        
        n = 3
        m = 3
        self.play(init(), run_time=1)
        self.play(
            LaggedStart(
                gate((0,0), (0,0), r"H"), 
                gate((1,0), (1,0), r"R_{\frac{\pi}{4}}"), 
                gate((2,0), (2,0), r"X"), lag_ratio=0.3
            ), run_time=2)
        self.play(gate((0,1), (1,1), r"U"), run_time=2)
        self.play(gate((1,2), (2,2), r"U^{\dagger}"), run_time=2)

import os
if __name__ == '__main__' :
    os.system('manim -pql myscene/test6.py Test')
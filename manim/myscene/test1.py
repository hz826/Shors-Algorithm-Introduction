from manim import *
import numpy as np
from numpy import sin, cos
from scipy.fftpack import shift

class Test(Scene) :
    def construct(self) :
        axes = Axes(
            x_range = [-PI, PI, PI/2],
            y_range = [0, 1, 1/4],
            x_length = 8,
            y_length = 5,
            tips = False,
            color=BLUE,
        )
        axes.x_axis.add_labels({
            -PI   : r'$-\pi$',
            # -PI/2 : r'$-\pi/2$',
            0     : r'$0$',
            # PI/2  : r'$\pi/2$',
            PI    : r'$\pi$',
        })
        self.add(axes)

        def f(x, m) :
            y = m**2 if sin(x/2) == 0 else sin(m*x/2)**2/sin(x/2)**2
            return y / m**2
        
        graphs = [(m, axes.plot(lambda x : f(x,m), x_range=[-PI, PI, 2*PI / 1000])) for m in [4,8,12,16]]

        for (m,graph) in graphs :
            self.play(Create(graph), run_time=2)
            self.play(FadeOut(graph), run_time=0.3)

import os
if __name__ == '__main__' :
    os.system('manim -pql myscene/test1.py Test')
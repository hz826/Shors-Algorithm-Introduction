from manim import *
import numpy as np
from math import pi, sin, cos

class Test(Scene) :
    def construct(self) :
        axes = Axes(
            x_range = [-pi, pi, pi/2],
            y_range = [0, 1, 1/4],
            x_length = 8,
            y_length = 5,
            tips = False,
            color=BLUE,
        )
        axes.x_axis.add_labels({
            -pi   : r'$-\pi$',
            # -pi/2 : r'$-\pi/2$',
            0     : r'$0$',
            # pi/2  : r'$\pi/2$',
            pi    : r'$\pi$',
        })
        self.add(axes)

        def f(x, m) :
            y = m**2 if sin(x/2) == 0 else sin(m*x/2)**2/sin(x/2)**2
            return y / m**2
        
        graphs = [(m, axes.plot(lambda x : f(x,m), x_range=[-pi, pi, 2*pi / 1000])) for m in [4,6,8,10]]

        for (m,graph) in graphs :
            self.play(Create(graph), run_time=2)
            self.play(FadeOut(graph), run_time=0.3)

import os
if __name__ == '__main__' :
    os.system('manim -pql scene.py Test')
from manim import *
import numpy as np
from numpy import sin, cos
from scipy.fft import fft

class Test(Scene) :
    def construct(self) :
        Q = 64
        r = 6
        V = [1 if i%r==0 else 0 for i in range(Q)]
        M = sum(V)
        print(Q, r, M)

        def f(x, m) :
            y = m**2 if sin(x/2) == 0 else sin(m*x/2)**2/sin(x/2)**2
            return y / m**2

        t = ValueTracker(0)
        V = abs(fft(V) / Q) ** 2
        V = V.tolist()

        ########################################################

        axes = Axes(
            x_range = [-PI, PI, PI/2],
            y_range = [0, 1, 1/4],
            x_length = 8,
            y_length = 5,
            tips = False,
            color = BLUE,
        )
        axes.x_axis.add_labels({
            -PI   : r'$-\pi$',
            # -PI/2 : r'$-\pi/2$',
            0     : r'$0$',
            # PI/2  : r'$\pi/2$',
            PI    : r'$\pi$',
        })
        axes.scale(0.8)
        axes.shift(RIGHT * 3.5)

        graph = axes.plot(lambda x : f(x,M), x_range=[-PI, PI, 2*PI / 1000])
        self.add(axes)

        dot2 = Dot(color=GREEN)
        dot2.add_updater(lambda x: x.move_to(axes.c2p(t.get_value(),f(t.get_value(),M))))
        v_line = always_redraw(lambda : axes.get_vertical_line(axes.i2gp(t.get_value(), graph), color=YELLOW))

        ########################################################

        plane = PolarPlane(
            size = 3,
            radius_max = 1.0,
            azimuth_step = 8,
        )
        plane.scale(0.6)
        plane.shift(RIGHT*1.5+UP*1)
        self.add(plane)

        dot1 = Dot(color=RED)
        dot1.add_updater(lambda x: x.move_to(plane.c2p(cos(t.get_value()),sin(t.get_value()))))
        r_line = always_redraw(lambda : Line(plane.c2p(0,0), plane.c2p(cos(t.get_value()),sin(t.get_value()))))

        ########################################################

        def getBar(val) :
            bar = BarChart(
                values = val,
                y_range=[0, max(V), 1],
                y_length = 3.5,
                x_length = 5,
                bar_colors = ['#df8d53'],
                bar_names = [str(i) if i%10==0 else '' for i in range(Q)],
                bar_fill_opacity = 0.9,
                x_axis_config = {
                    'include_ticks' : False, 
                },
            )
            labels = {
                M**2 / Q**2 : r'$\frac{1}{r^2}$',
                4/PI**2/r**2 : r'$\frac{4}{\pi^2r^2}$',
            }
            bar.y_axis.add_labels(labels)
            for (k,v) in labels.items() :
                bar.add(bar.y_axis.get_tick(k))

            bar.scale(1.15)
            bar.shift(LEFT * 3.2)
            return bar

        bar_val = [0] * Q
        bar = getBar(bar_val)
        self.add(bar)

        ########################################################

        self.wait()
        self.play(Create(graph))
        self.play(Create(dot1), Create(dot2), Create(v_line), Create(r_line))
        self.wait()

        def move(value) :
            self.play(t.animate.set_value(value), run_time=0.2, rate_func=linear)
        
        delta = 2*PI*r / Q
        for i in range(Q) :
            v = t.get_value()
            if v + delta > PI :
                move(PI)
                t.set_value(-PI)
                move(v + delta - PI*2)
            else :
                move(v + delta)
            
            bar_val[i] = V[i]
            nbar = getBar(bar_val)
            self.play(Transform(bar, nbar), run_time=0.2)

import os
if __name__ == '__main__' :
    os.system('manim -pqh myscene/scene2.py Test')
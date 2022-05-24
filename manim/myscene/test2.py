from manim import *
import numpy as np
from numpy import sin, cos

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
        axes.shift(RIGHT * 2)

        def f(x, m) :
            y = m**2 if sin(x/2) == 0 else sin(m*x/2)**2/sin(x/2)**2
            return y / m**2
        graph = axes.plot(lambda x : f(x,6), x_range=[-PI, PI, 2*PI / 1000])
        self.add(axes, graph)

        ########################################################

        plane = PolarPlane(
            size = 3,
            radius_max = 1.0,
            azimuth_step = 8,
        )
        plane.shift(LEFT * 4)
        self.add(plane)

        t = ValueTracker(0)

        dot2 = Dot(color=GREEN)
        dot2.add_updater(lambda x: x.move_to(axes.c2p(t.get_value(),f(t.get_value(),6))))
        v_line = always_redraw(lambda : axes.get_vertical_line(axes.i2gp(t.get_value(), graph), color=YELLOW))

        dot1 = Dot(color=RED)
        dot1.add_updater(lambda x: x.move_to(plane.c2p(cos(t.get_value()),sin(t.get_value()))))
        r_line = always_redraw(lambda : Line(plane.c2p(0,0), plane.c2p(cos(t.get_value()),sin(t.get_value()))))

        # always_redraw(lambda : graph.get_vertical_lines_to_graph(dot2))

        self.wait()
        self.add(dot1, dot2)
        self.play(Create(v_line), Create(r_line))
        self.wait()

        # dot1 = Dot(plane.coords_to_point(1,0), color=RED)

        # def getline() :
        #     return Line(plane.coords_to_point(0,0), plane.coords_to_point(1,0))
            # return plane.get_vertical_lines_to_graph(dot1)
        
        # r_line = always_redraw()
        # r_line = getline()
        # self.add(plane, dot1, r_line)

        # get_vertical_lines_to_graph

        # dot2 = Dot(plane.coords_to_point(1,0), color=RED)
        # v_line = always_redraw(lambda: axes.get_h_line(dot.get_left()))

        # lines = ax.get_vertical_lines_to_graph(
        #     curve, x_range=[0, 4], num_lines=30, color=BLUE
        # )

        self.play(t.animate.set_value(PI), run_time=2, rate_func=linear)
        t.set_value(-PI)
        self.play(t.animate.set_value(0), run_time=2, rate_func=linear)

import os
if __name__ == '__main__' :
    os.system('manim -pql myscene/test2.py Test')
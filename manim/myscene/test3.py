from manim import *
import numpy as np
from numpy import sin, cos
from scipy.fft import fft

class Test(Scene) :
    def construct(self) :
        n = 64

        def normalize(A) :
            return A / np.sqrt(sum(abs(A)**2))

        def getchart(A) :
            return BarChart(
                values = abs(A)**2,
                y_length = 3,
                x_length = 5,
                bar_colors=['#003f5c'],
                bar_names=[str(i) if i%10==0 else '' for i in range(n)],
                bar_fill_opacity = 0.9,
                x_axis_config = {
                    'include_ticks' : False, 
                },
                y_axis_config = {
                    'include_ticks' : False, 
                },
            )

        charts = []

        A = np.array([1 if i%11==10 else 0 for i in range(n)], dtype=complex)
        A = normalize(A)
        B = fft(A)
        B = normalize(B)
        charts.append((getchart(A).shift(LEFT * 3), getchart(B).shift(RIGHT * 3)))
        self.add(*charts[-1])
        


        A = np.array([1 if i%6==5 else 0 for i in range(n)], dtype=complex)
        A = normalize(A)
        B = fft(A)
        B = normalize(B)
        charts.append((getchart(A).shift(LEFT * 3), getchart(B).shift(RIGHT * 3)))
        
        self.wait()
        self.play(ReplacementTransform(charts[-2][0], charts[-1][0]), ReplacementTransform(charts[-2][1], charts[-1][1]), run_time=3)
        self.wait()


        A = np.array([1 if i%6==2 else 0 for i in range(n)], dtype=complex)
        A = normalize(A)
        B = fft(A)
        B = normalize(B)
        charts.append((getchart(A).shift(LEFT * 3), getchart(B).shift(RIGHT * 3)))
        
        self.wait()
        self.play(ReplacementTransform(charts[-2][0], charts[-1][0]), ReplacementTransform(charts[-2][1], charts[-1][1]), run_time=3)
        # self.remove(charts[-2][0], charts[-2][1])
        self.wait()
        

import os
if __name__ == '__main__' :
    os.system('manim -pql myscene/test3.py Test')
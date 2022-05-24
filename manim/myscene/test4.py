from manim import *
import numpy as np
from numpy import sin, cos
from scipy.fft import fft

class Test(Scene) :
    def construct(self) :
        def Align(*strs) :
            lines = [s.replace(r'\\','').split('&') for s in strs if r'{array}' not in s]
            m = len(lines[0])
            vg = VGroup(*[MathTex(l[i], font_size=30) for l in lines for i in range(m)])
            vg.arrange_in_grid(
                col_alignments = 'l'*m,
            )
            return vg
        
        tex_l1 = (
            r'\begin{array}{lllllllll}',
            r'\ket{0,f(0)}&+&\ket{1,f(1)}    &+&\dots&+&\ket{r-1,f(r-1)}  &+&\dots\\',
            r'\ket{r,f(r)}&+&\ket{r+1,f(r+1)}&+&\dots&+&\ket{2r-1,f(2r-1)}&+&\dots\\',
            r'&&&&&&&+& \ket{Q-1,f(Q-1)}',
            r'\end{array}',
        )
        tex_l2 = (
            r'\begin{array}{lllllllll}',
            r'\ket{0,f(0)}&+&\ket{1,f(1)}    &+&\dots&+&\ket{r-1,f(r-1)}  &+&\dots\\',
            r'\ket{r,f(0)}&+&\ket{r+1,f(1)}&+&\dots&+&\ket{2r-1,f(r-1)}&+&\dots\\',
            r'&&&&&&&+& \ket{Q-1,f(Q-1\ \mathrm{mod}\ r)}',
            r'\end{array}',
        )

        l0 = MathTex(
            r'\ket{0,f(0)}+\ket{1,f(1)}+\dots+\ket{r-1,f(r-1)}+\ket{r,f(r)}+\ket{r+1,f(r+1)}+\dots+\ket{2r-1,f(2r-1)}+\dots+\ket{Q-1,f(Q-1)}',
            font_size = 24,
            # r'\ket{0,f(0)}+\ket{1,f(1)}+\dots+\ket{r-1,f(r-1)} +\dots+\ket{r,f(r)}+\ket{r+1,f(r+1)}+\dots+\ket{2r-1,f(2r-1)}+\dots+ \ket{Q-1,f(Q-1)}',
            # font_size = 24,
            # r'\sum_{i=0}^{Q-1} \ket{i,f(i)}',
            # font_size = 30,
        )

        al = Align(*(tex_l1+tex_l2))
        l1 = VGroup(*al[:27])
        l2 = VGroup(*al[27:])

        vg = VGroup(l0, l1.copy()).arrange(DOWN, buff=LARGE_BUFF)
        l0 = vg[0]

        l1.next_to(l0, DOWN, coor_mask=[0,1,0])
        l2.next_to(l0, DOWN, coor_mask=[0,1,0])

        self.play(Write(l0))
        self.play(ReplacementTransform(l0.copy(), l1))
        self.wait()
        self.play(TransformMatchingTex(l1, l2), run_time=2)
        self.wait()
        

import os
if __name__ == '__main__' :
    os.system('manim -pql myscene/test4.py Test')
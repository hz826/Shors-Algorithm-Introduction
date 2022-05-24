SceneName = 'test1'

import os
if __name__ == '__main__' :
    os.system('manim -pql myscene/' + SceneName + '.py Test')
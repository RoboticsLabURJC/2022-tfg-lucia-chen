"""
Ejemplo de planificación geometrica definiendo los obstáculos con pixeles oscuros
"""


from os.path import abspath, dirname, join
import sys
import cv2
import numpy as np
try:
    from ompl import util as ou
    from ompl import base as ob
    from ompl import geometric as og
except ImportError:
    # if the ompl module is not in the PYTHONPATH assume it is installed in a
    # subdirectory of the parent directory called "py-bindings."
    sys.path.insert(0, join(dirname(dirname(abspath(__file__))), 'py-bindings'))
    from ompl import util as ou
    from ompl import base as ob
    from ompl import geometric as og
from functools import partial

folder = "results/"
group = "B_"
img_extension = ".png"

wi = 10
hi = 10
wf = 211
hf = 233

class Plane2DEnvironment:
    def __init__(self, png_file):

        # Obtener dimensiones de la imagen en formato png
        self.im = cv2.imread(png_file)
        height, width, _ = self.im.shape

        # Instanciar el espacio e indicar las dimensiones
        space = ob.RealVectorStateSpace()
        space.addDimension(0.0, width)
        space.addDimension(0.0, height)

        # Definir 
        self.maxWidth_ = width - 1
        self.maxHeight_ = height - 1

        self.erode_img()

        # Crear un contexto de planificación simple
        self.ss_ = og.SimpleSetup(space)

        # Establecer verificación de validez de estado para este espacio
        self.ss_.setStateValidityChecker(ob.StateValidityCheckerFn(partial(Plane2DEnvironment.isStateValid, self)))
        
        space.setup()
        self.ss_.getSpaceInformation().setStateValidityCheckingResolution(1.0 / space.getMaximumExtent())

        # Indicar el planificador
        self.ss_.setPlanner(og.PRM(self.ss_.getSpaceInformation()))

    def plan(self, start_row, start_col, goal_row, goal_col):
        if not self.ss_:
            return False
        
        # Definir estado inicial y final
        start = ob.State(self.ss_.getStateSpace())
        start()[0] = start_row
        start()[1] = start_col
        goal = ob.State(self.ss_.getStateSpace())
        goal()[0] = goal_row
        goal()[1] = goal_col
        self.ss_.setStartAndGoalStates(start, goal)

        # Calcular solución
        self.ss_.solve()

        # Comprobar que se ha generado una solución
        if self.ss_.haveSolutionPath():
            self.ss_.simplifySolution() # simplificar solución, reducir el número de estado al máximo
            p = self.ss_.getSolutionPath()
            print("\nSoluction path: " + str(p))

            self.draw(p, (255, 0, 0))
            self.save(folder + group + "not_smooth" + img_extension)

            # suavizar la ruta
            ps = og.PathSimplifier(self.ss_.getSpaceInformation())
            ps.simplifyMax(p)
            ps.smoothBSpline(p)

            return True
        return False

    # Pintar la ruta solución sobre el mapa
    def recordSolution(self):
        if not self.ss_ or not self.ss_.haveSolutionPath():
            return

        p = self.ss_.getSolutionPath()  
        self.draw(p, (255, 0, 0))
        self.save(folder + group + "not_interpolate" + img_extension)

        p.interpolate()     # Crear trayectoria
        self.draw(p, (255, 0, 0))
        self.save(folder + group + "interpolate" + img_extension)

    # Pintar la solución
    def draw(self, p, color):
        for i in range(p.getStateCount()):
            w = min(self.maxWidth_, int(p.getState(i)[0]))
            h = min(self.maxHeight_, int(p.getState(i)[1]))
            self.im[h, w] = color
        for i in range(3):
            for j in range(3):
                self.im[i+hi-1,j+wi-1] = (0, 255, 0)
                self.im[i+hf-1,j+wf-1] = (0, 0, 255)

    # Guardar la solución
    def save(self, filename):
        if not self.ss_:
            return
        cv2.imwrite(filename, self.im)


    def isStateValid(self, state):
        w = min(int(state[0]), self.maxWidth_)
        h = min(int(state[1]), self.maxHeight_)

        c = self.im[h, w]
        return c[0] > 250 and c[1] > 250 and c[2] > 250

    def erode_img(self):
        kernel = np.ones((8, 8), np.uint8)
        self.im = cv2.erode(self.im, kernel)
        # cv2.imshow("Image erode", self.im)
        # cv2.waitKey(0)


if __name__ == "__main__":
    fname = join('png', 'map1.png')
    env = Plane2DEnvironment(fname)

    if env.plan(wi, hi, wf, hf):
        env.recordSolution()


# demos de gráficos
# (C) 2022 Fernando Fernandez Pedraza. 
# licencia GNU GPL v3- http://www.gnu.org/licenses/gpl-3.0.html
#
# descargar e instalar la libreria graphics.py en la misma carpeta que las demos
# graphics.py y su documentación están en https://mcsp.wartburg.edu/zelle/python/
# 
# demo de lineas
from graphics import *
from time import * 
from random import randrange

win = GraphWin(":-)",400, 400)
#pt = Point(10,10)
#pt.draw(win)

colors=['red','green','blue','yellow','orange']

for x in range(0,400,20):
        line = Line(Point(x,0), Point(0,400-x))

        rnd=randrange(4)
        line.setFill(colors[rnd])

        line.draw(win)
        sleep(0.1)

win.getMouse() # Pause to view result
win.close()    # Close window when done
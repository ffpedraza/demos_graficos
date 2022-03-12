# demos de gráficos
# (C) 2022 Fernando Fernandez Pedraza. 
# licencia GNU GPL v3- http://www.gnu.org/licenses/gpl-3.0.html
#
# descargar e instalar la libreria graphics.py en la misma carpeta que las demos
# graphics.py y su documentación están en https://mcsp.wartburg.edu/zelle/python/
# 
# un gusano
from graphics import *
from time import * 
from random import randrange

win = GraphWin("gusano :-)",400, 400)
#pt = Point(10,10)
#pt.draw(win)

colors=['red','green','blue','yellow','orange']

x1=200
y1=200

for i in range(0,100):
    x2=x1+randrange(-20,20,1)    
    y2=y1+randrange(-20,20,1)
    line = Line(Point(x1,y1), Point(x2,y2))
    line.draw(win)
    x1=x2
    y1=y2
    sleep(0.05)

win.getMouse() # Pause to view result
win.close()    # Close window when done
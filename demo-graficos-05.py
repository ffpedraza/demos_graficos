# demos de gráficos
# (C) 2022 Fernando Fernandez Pedraza. 
# licencia GNU GPL v3- http://www.gnu.org/licenses/gpl-3.0.html
#
# descargar e instalar la libreria graphics.py en la misma carpeta que las demos
# graphics.py y su documentación están en https://mcsp.wartburg.edu/zelle/python/
# 
# simulación de pelota simple
from graphics import *
from time import * 
from random import randrange

win = GraphWin("pelota :-)",400, 410)

x1=randrange(40,360)
y1=randrange(40,360)
dx=randrange(7,10)
dy=randrange(7,10)

while(   not(win.checkMouse())   ):
    circle = Circle(Point(x1,y1), 20)
    circle.setFill('green')
    circle.draw(win)

    x1+=dx
    y1+=dy

    if(x1>380): dx=dx * -1
    if(y1>380): dy=dy * -1
    if(x1<20): dx=dx * -1
    if(y1<20): dy=dy * -1
      
    sleep(0.02)
    circle.undraw()

win.close()    # Close window when done
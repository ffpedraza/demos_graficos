# demos de gráficos
# (C) 2022 Fernando Fernandez Pedraza. 
# licencia GNU GPL v3- http://www.gnu.org/licenses/gpl-3.0.html
#
# descargar e instalar la libreria graphics.py en la misma carpeta que las demos
# graphics.py y su documentación están en https://mcsp.wartburg.edu/zelle/python/
# 
# rectángulos
from graphics import *
from time import * 
from random import randrange

win = GraphWin("muchos rectángulos :-)",400, 400)
#pt = Point(10,10)
#pt.draw(win)

colors=['red','green','blue','yellow','orange']

x1=200
y1=200

for i in range(0,100):
    x1=randrange(400)    
    x2=randrange(400)    
    y1=randrange(400)    
    y2=randrange(400)    
    
    rectangle = Rectangle(Point(x1,y1), Point(x2,y2))
    rnd=randrange(5)
    rectangle.setFill(colors[rnd])
    rectangle.draw(win)
    
    sleep(0.05)

win.getMouse() # Pause to view result
win.close()    # Close window when done
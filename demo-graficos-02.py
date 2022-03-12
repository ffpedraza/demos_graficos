# demos de gráficos
# (C) 2022 Fernando Fernandez Pedraza. 
# licencia GNU GPL v3- http://www.gnu.org/licenses/gpl-3.0.html
#
# descargar e instalar la libreria graphics.py en la misma carpeta que las demos
# graphics.py y su documentación están en https://mcsp.wartburg.edu/zelle/python/
# 
# demo de varias primitivas de gráficos
from graphics import *
from time import * 
from random import randrange

win = GraphWin("varias formas :-)",400, 400)
#pt = Point(10,10)
#pt.draw(win)

colors=['red','green','blue','yellow','orange']

# una linea en color aleatorio
line = Line(Point(0,0), Point(400,400))
rnd=randrange(4)
line.setFill(colors[rnd])
line.draw(win)

# un circulo
circle = Circle(Point(200,200), 100)
rnd=randrange(4)
circle.setOutline(colors[rnd])
circle.draw(win)

# un rectángulo
rectangle = Rectangle(Point(50,70), Point(150,300))
rnd=randrange(4)
rectangle.setOutline(colors[rnd])
rectangle.draw(win)

# un polígono definido por puntos
polygon = Polygon(Point(100,20), Point(130,40), Point(50,60), Point(200,300), Point(10, 250))
rnd=randrange(4)
polygon.setOutline(colors[rnd])
polygon.draw(win)

#texto 
message = Text(Point(200,200), "Hello!")
message.draw(win)

sleep(0.1)

win.getMouse() # Pause to view result
win.close()    # Close window when done
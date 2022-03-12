# demos de gráficos
# (C) 2022 Fernando Fernandez Pedraza. 
# licencia GNU GPL v3- http://www.gnu.org/licenses/gpl-3.0.html
#
# descargar e instalar la libreria graphics.py en la misma carpeta que las demos
# graphics.py y su documentación están en https://mcsp.wartburg.edu/zelle/python/
# 
# simulacion de pelota realista

# primero importamos las librerías de tortuga, mates y de tiempo
from math import sin, cos, radians
from time import sleep
from graphics import *
from random import randrange

v=60        # velocidad
a=85        # angulo de tiro, entre 0 y 90

g=9.81      # gravedad
t=0         # inicializamos tiempo
tstep=0.05   # resolucion de tiempo
y0=5         # altura inicial
x0=0
v0=v
x=0
y=0


vx = v * cos(radians(a))
vy = v * sin(radians(a))
vy0 = vy

win = GraphWin("pelota 2 :-)",600, 400)
win.setCoords(0,0,600,400)
circle = Circle(Point(x,y), 5)
circle.setFill('green')
    
# calculamos la posición en instantes de tiempo

while (vy > vy0/15): # seguimos botando hasta que la velocidad inicial se divide por 15
    while(y>=0):
        circle = Circle(Point(x,y), 5)
        circle.setFill('green')
        circle.draw(win)
        sleep(0.005)

        t = t + tstep
        x = x0 + vx * t
        y = y0 + vy *t - (1/2)*g*t**2
     
        #print(f"t:{t}  x:{x}  y:{y}")
        circle.undraw()

    x0=x
    t=0
    y=0
    vy *= 0.8

circle = Circle(Point(x,5), 5)
circle.setFill('green')
circle.draw(win)

win.getMouse() # Pause to view result
win.close()    # Close window when done
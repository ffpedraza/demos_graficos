# demos de gráficos
# (C) 2022 Fernando Fernandez Pedraza. 
# licencia GNU GPL v3- http://www.gnu.org/licenses/gpl-3.0.html
#
# descargar e instalar la libreria graphics.py en la misma carpeta que las demos
# graphics.py y su documentación están en https://mcsp.wartburg.edu/zelle/python/
# 
# celulas. ponemos comida (puntos) y las celulas se mueven aleatoriamente y van comiendo
# 
from graphics import *
from time import * 
from random import randrange

windl= 600
win = GraphWin("células :-)",windl, windl)
win.setCoords(0,0,windl, windl)

maxf = 200
maxc = 50
food=[]
cells=[]
csize=5

# comida
for i in range(0,maxf):
    f=Point(randrange(windl),randrange(windl))
    f.setFill('red')
    food.append( f )
    f.draw(win)

# celulas
for i in range(0,maxc):
    c=Circle(Point(randrange(windl),randrange(windl)),csize)
    c.setFill('green')
    cells.append(c)
    c.draw(win)

while( not(win.checkMouse()) ) :
    #mover células
    for c in cells:
        dx=randrange(-5,6)
        dy=randrange(-5,6)
        #hacer que no se nos escapen de la pantalla
        cp = c.getCenter()
        if (cp.getX()>windl): dx=-1
        if (cp.getY()>windl): dy=-1
        if (cp.getX()<0): dx=1
        if (cp.getY()<0): dy=1

        c.move(dx,dy)

    #calcular si la célula tiene comida cerca
    # getP1(), getP2() Returns a clone of the corresponding corner of the 
    # circle's bounding box. These are opposite corner points of a square that 
    # circumscribes the circle. 
    cfeed=[]
    for c in cells:
        fdel=[]
        for f in food:
            c1=c.getP1()
            c2=c.getP2()
            fx=f.getX()
            fy=f.getY()
            if (fx>c1.getX() and fx<c2.getX() and fy>c1.getY() and fy<c2.getY() ):
                fdel.append(f)
                cfeed.append(c)

        #retiro la comida consumida
        for fd in fdel:
            try:
                food.remove(fd)
                fd.undraw()
            except:
                pass

    # las celulas que han comido crecen
    for cf in cfeed:
        try:
            cells.remove(cf)
            cf.undraw()
        except:
            pass
        ncf=Circle(cf.getCenter(),cf.getRadius()+1)
        ncf.setFill('green')

        cells.append(ncf)
        ncf.draw(win)
    

win.getMouse() # Pause to view result
win.close()    # Close window when done
# demos de gráficos
# (C) 2022 Fernando Fernandez Pedraza. 
# licencia GNU GPL v3- http://www.gnu.org/licenses/gpl-3.0.html
#
# descargar e instalar la libreria graphics.py en la misma carpeta que las demos
# graphics.py y su documentación están en https://mcsp.wartburg.edu/zelle/python/
# 
# un arbol
from graphics import *
from time import * 
from random import randrange

win = GraphWin("árbol :-)",600, 600)
win.setCoords(0,0,600,600)

ptscur=[(300,60)]
ptsnew=[]
dtx=35
dty=40
iter=10

# tronco
line = Line( Point(300,0), Point( ptscur[0][0],ptscur[0][1]) )
line.setWidth(12)
line.draw(win)

for i in range(iter): # num de niveles
    ptsnew=[] 
    for p in ptscur:
        
        np=( (p[0]+randrange(-dtx,0),p[1]+randrange(0,dty)) )
        ptsnew.append( np )
        line = Line( Point(p[0],p[1]), Point(np[0],np[1]) )
        line.setWidth(iter-i)
        line.draw(win)      

        np=( (p[0]+randrange(0,dtx),p[1]+randrange(0,dty)) )
        ptsnew.append( np )
        line = Line( Point(p[0],p[1]), Point(np[0],np[1]) )      
        line.setWidth(iter-i)
        line.draw(win)
    
    ptscur=ptsnew.copy()
    
    #print("--fin for ext")
    #print("len: ",len(ptscur))
    

win.getMouse() # Pause to view result
win.close()    # Close window when done
#Coursework 01 - INTPROG
#UP849868

from graphics import *


#-------DrawShapes------------

def drawRect(win,p1,p2,fill = None,outline= None):
        
   Rect = Rectangle(p1,p2)
   
   if fill != None: Rect.setFill(fill)
   #Fill will be transparent if not specified
   if outline != None: Rect.setOutline(outline)
   #Outline of shape will be black unless specified
   Rect.draw(win)
   return Rect

def drawTria(win,p1,p2,p3,fill = None,outline= None):

   Tria = Polygon(p1,p2,p3)
   if fill != None: Tria.setFill(fill)
   #Fill will be transparent if not specified
   if outline != None: Tria.setOutline(outline)
   #Outline of shape will be black unless specified
   Tria.draw(win)


def drawCircle(win,center,radius,fill = None,outline= None):

   Cir = Circle(center,radius)
   if fill != None: Cir.setFill(fill)
   #Fill will be transparent if not specified
   if outline != None: Cir.setOutline(outline)
   #Outline of shape will be black unless specified
   Cir.draw(win)



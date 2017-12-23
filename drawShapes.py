
from graphics import *


#-------DrawShapes------------

def drawLine(win,p1,p2,fill=None,size=None):
    
    line = Line(p1,p2)
    if fill != None: line.setFill(fill)
    if size != None: line.setWidth(int(size))
    line.draw(win)
    return line

def drawRect(win,p1,p2,fill = None,outline= None):
        
    rect = Rectangle(p1,p2)
   
    if fill != None: rect.setFill(fill)
    #Fill will be transparent if not specified
    if outline != None: rect.setOutline(outline)
    #Outline of shape will be black unless specified
    rect.draw(win)
    return rect

def drawTria(win,p1,p2,p3,fill = None,outline= None):

    tria = Polygon(p1,p2,p3)
    if fill != None: tria.setFill(fill)
    #Fill will be transparent if not specified
    if outline != None: tria.setOutline(outline)
    #Outline of shape will be black unless specified
    tria.draw(win)
    return tria

def drawCircle(win,center,radius,fill = None,outline= None):

    cir= Circle(center,radius)
    if fill != None: cir.setFill(fill)
    #Fill will be transparent if not specified
    if outline != None: cir.setOutline(outline)
    #Outline of shape will be black unless specified
    cir.draw(win)
    return cir

def drawPolygon(win,p1,p2,p3,p4,fill= None, outline= None):
    poly = Polygon(p1,p2,p3,p4)
    if fill != None: poly.setFill(fill)
    #Fill will be transparent if not specified
    if outline != None: poly.setOutline(outline)
    #Outline of shape will be black unless specified
    poly.draw(win)
    return poly

def drawOval(win,p1,p2,fill=None,outline=None):
    oval = Oval(p1,p2)
    if fill != None: oval.setFill(fill)
    #Fill will be transparent if not specified
    if outline != None: oval.setOutline(outline)
    #Outline of shape will be black unless specified
    oval.draw(win)
    return oval

def drawText(win,txt,center,size,colour=None,face=None,style=None):
    text = Text(center,str(txt))
    text.setSize(size)
    if colour != None: text.setOutline(colour)
    if face != None: text.setFace(face)
    if style != None: text.setStyle(style)
    text.draw(win)
    return text

#-------MakeShapes------------

def makeLine(win,p1,p2,fill=None,size=None):
    
    line = Line(p1,p2)
    if fill != None: line.setFill(fill)
    if size != None: line.setWidth(int(size))
    return line


def makeRect(win,p1,p2,fill = None,outline= None):
        
    rect = Rectangle(p1,p2)
   
    if fill != None: rect.setFill(fill)
    #Fill will be transparent if not specified
    if outline != None: rect.setOutline(outline)
    #Outline of shape will be black unless specified
    return rect

def makeTria(win,p1,p2,p3,fill = None,outline= None):

    tria = Polygon(p1,p2,p3)
    if fill != None: tria.setFill(fill)
    #Fill will be transparent if not specified
    if outline != None: tria.setOutline(outline)
    #Outline of shape will be black unless specified
    return tria

def makeCircle(win,center,radius,fill = None,outline= None):

    cir= Circle(center,radius)
    if fill != None: cir.setFill(fill)
    #Fill will be transparent if not specified
    if outline != None: cir.setOutline(outline)
    #Outline of shape will be black unless specified
    return cir

def makePolygon(win,p1,p2,p3,p4,fill= None, outline= None):
    poly = Polygon(p1,p2,p3,p4)
    if fill != None: poly.setFill(fill)
    #Fill will be transparent if not specified
    if outline != None: poly.setOutline(outline)
    #Outline of shape will be black unless specified
    return poly

def makeOval(win,p1,p2,fill=None,outline=None):
    oval = Oval(p1,p2)
    if fill != None: oval.setFill(fill)
    #Fill will be transparent if not specified
    if outline != None: oval.setOutline(outline)
    #Outline of shape will be black unless specified
    return oval



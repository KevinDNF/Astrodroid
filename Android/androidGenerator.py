from graphics import *
from drawShapes import *

#Android related functions
##To do 
#+ Turn every rectangle in a polygon (for animations)
#+ Add arms&&legs animations (2 frames)
#+ Delete experiments

def animateWalk(android,frame):
    if frame == 0:
       android[2].move(5,0)
       android[3].move(3,0)
       android[4].move(-3,0)
       android[5].move(2,0)
    
    if frame == 1:
       
       android[2].move(-5,0)
       android[3].move(-3,0)
       android[4].move(3,0) 
       android[5].move(-2,0)

def death(android,score):
       print("You Lost :( ", "At least you got {0} apples :)".format(score))
       speed = 0
       while True:
           speed += 0.0001 
           android[0].move(speed/2,speed)
           android[1].move(speed/2,speed)
           android[2].move(speed,-speed)
           android[3].move(-speed,speed)
           android[4].move(speed,speed) 
           android[5].move(-speed,-speed)
           android[7].move(-speed,speed)

def createAndroid(win,x,y,color):
    
    head = drawCircle(win, Point(x+50,y+20), 15, color, "black")
    body = drawRect(win, Point(x+35,y+20), Point(x+65,y+60), color, "white")

    arm = drawRect(win, Point(x+47,y+25), Point(x+57,y+55),color, "black")
 
    legL = drawRect(win, Point(x+47,y+60), Point(x+55,y+75),color, "black")
    legR = drawRect(win, Point(x+45,y+60), Point(x+53,y+75), color, "black")

    eye = drawCircle(win, Point(x+57,y+12), 3, "white","black")
    block = Point(-10000000,-1000000)
   
    jetpack = Rectangle(Point(body.p1.x-10,body.p1.y+3),
                        Point(body.p1.x,body.p2.y-5)).draw(win)
    jetpack.setFill("gray")
    jetpack.setOutline("black")
   
    #block = drawRect(win,Point(body.p1.x,body.p1.y -15),Point(body.p2.x,body.p2.y+15))
    #uncomment to see the collision block around the player
    #(testing purposes)
    return [head,body,arm,legL,legR,eye,block,jetpack]

def move(android, x,y):
    for part in android:
        part.move(x,y)

def checkJetpack(android):
    if len(android) == 9:
        return True
    else:
        return False

def toggleJetpack(android,win,direction):
    body = android[1]
    jetpack = android[7]

    fire = Polygon(Point(jetpack.p1.x,jetpack.p2.y+2),
            Point(jetpack.p1.x+5,jetpack.p2.y+27),
            Point(jetpack.p2.x,jetpack.p2.y+2))

    fire.setFill("red")
    fire.setOutline("yellow")

    if checkJetpack(android):  #its there 
        android[8].undraw() 
        android.remove(android[8])
    else: #Its not there

        android.append(fire)
        fire.draw(win)

def invertPoscition(android,direction):

    if direction == "right":
        android[2].move(-4,0)
        android[3].move(-4,0)
       #legR 
        android[5].move(-12,0)
        android[7].move(40,0) #jetpack
        if checkJetpack(android):
            android[8].move(40,0)
        return "left"

    elif direction == "left":
        android[2].move(4,0)
        android[3].move(4,0)
       #LegR 
        android[5].move(12,0)
        android[7].move(-40,0) #jetpack
        if checkJetpack(android):
            android[8].move(-40,0)
        return "right"

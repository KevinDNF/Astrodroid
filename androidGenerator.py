from graphics import *
from drawShapes import *

#Android related functions


# To-do
# Change the way the jetpack is checked
# Animate jetpack with walking animation
# Add second eye + animate
# Animate fire

def animateWalk(android,frame):
    if frame == 0:
       android[2].move(5,0)
       android[3].move(3,0)
       android[4].move(-3,0)
       android[5].move(2,0)
 
#      android[7].move(3,0) #Limited by z axis...
#      android[8].move(3,0) #Jetpack will always be on top
#      android[9].move(3,0) #So left walking won't work.....
#      android[10].move(3,0)#.....
#      android[11].move(3,0)#.......
#      android[12].move(3,0)#........Unless
#      android[13].move(3,0)#Movement is consistent in both directions 
#      if checkJetpack(android):android[14].move(3,0)# So jetpack never goes "behind"
    if frame == 1:
       
       android[2].move(-5,0)
       android[3].move(-3,0)
       android[4].move(3,0) 
       android[5].move(-2,0)

#      android[7].move(-3,0)
#      android[8].move(-3,0)
#      android[9].move(-3,0)
#      android[10].move(-3,0)
#      android[11].move(-3,0)
#      android[12].move(-3,0)
#      android[13].move(-3,0)
#      if checkJetpack(android):android[14].move(-3,0)

def death(win,android,score):
       print("You Lost :( ", "At least you got {0} apples :)".format(score))
       speed = 0
       drawText(win,
               "You Lost  :( \n "
               "At least you got {0} apples".format(score),
               Point(win.width/2,win.height/2),30,"white","times roman","bold")
       while True:
           speed += 0.0005 
           android[0].move(speed/2,speed)
           android[1].move(speed/2,speed)
           android[2].move(speed,-speed)
           android[3].move(-speed,speed)
           android[4].move(speed,speed) 
           android[5].move(-speed,-speed)
           android[7].move(-speed,speed)
           
           android[12].move(-speed,speed)
           android[13].move(-speed,speed)

           if checkJetpack(android): 
               android[8].move(0,-speed*10) # Jetpack
               android[9].move(0,-speed*10) # Jetpack
               android[10].move(0,-speed*10)# Jetpack
               android[11].move(0,-speed*10)# Jetpack
               android[14].move(0,-speed*10) # Fire
           else:
               android[8].move(-speed,speed*2) # Jetpack
               android[9].move(-speed,speed*2) # Jetpack
               android[10].move(-speed,speed*2)# Jetpack
               android[11].move(-speed,speed*2)# Jetpack


def createJetpack(win,body):

    block = drawRect(win,Point(body.p1.x-10,body.p1.y+3) 
                ,Point(body.p1.x,body.p2.y-5),"dark gray","black")
    
    prop = drawRect(win,Point(body.p1.x-9.5,body.p2.y-5) 
                ,Point(body.p1.x-1.9,body.p2.y),"gray","black")
    
    det1 = drawLine(win,Point(body.p1.x-7,body.p2.y-5),Point(body.p1.x-7,body.p2.y))
    det2 = drawLine(win,Point(body.p1.x-5,body.p2.y-5),Point(body.p1.x-5,body.p2.y))
    det3 = drawLine(win,Point(body.p1.x-3,body.p2.y-5),Point(body.p1.x-3,body.p2.y))
    
    det4 = drawLine(win,Point(body.p1.x-10,body.p1.y+6),
                 Point(body.p1.x,body.p1.y+6),"dark blue",1)
    det5 = drawLine(win,Point(body.p1.x-10,body.p1.y+8),
                Point(body.p1.x,body.p1.y+8),"blue",1)

    jetpack = [block,prop,det1,det2,det3,det4,det5] # len == 7
    
    return jetpack

def createAndroid(win,x,y,color):
    
    head = drawCircle(win, Point(x+50,y+20), 15, color, "black")
    body = drawRect(win, Point(x+35,y+20), Point(x+65,y+60), color, "black")

   # =  drawLine(win, Point(x+35,y+20), Point(x+65,y+20),"white")
    arm = drawRect(win, Point(x+47,y+25), Point(x+57,y+55),color, "black")
 
    legL = drawRect(win, Point(x+47,y+60), Point(x+55,y+75),color, "black")
    legR = drawRect(win, Point(x+45,y+60), Point(x+53,y+75), color, "black")

    eye = drawCircle(win, Point(x+57,y+12), 3, "white","black")
    block = Point(-10000000,-1000000)
    
    android = [head,body,arm,legL,legR,eye,block]
    jetpack = createJetpack(win,body)
    android.extend(jetpack)
   
   #block = drawRect(win,Point(body.p1.x,body.p1.y -15),Point(body.p2.x,body.p2.y+15))
    #uncomment to see the collision block around the player
    #(testing purposes)
    return android

def move(android, x,y):
    for part in android:
        part.move(x,y)

def checkJetpack(android):
    if len(android) == 15:
        return True
    else:
        return False

def toggleJetpack(android,win,direction):
    body = android[1]
    jetpack = android[7]

    fire = Polygon(Point(jetpack.p1.x,jetpack.p2.y+7),
            Point(jetpack.p1.x+4,jetpack.p2.y+32),
            Point(jetpack.p2.x-2,jetpack.p2.y+7))

    fire.setFill("red")
    fire.setOutline("yellow")

    if checkJetpack(android):  #its there 
        android[14].undraw() 
        android.remove(android[14])
    else: #Its not there

        android.append(fire)
        fire.draw(win)

def invertPoscition(android,direction):

    if direction == "right":
        android[2].move(-4,0)
        android[3].move(-4,0)
       #legR 
        android[5].move(-12,0)
        android[7].move(40,0)#jetpack
        android[8].move(40,0)#jetpack
        android[9].move(40,0)#jetpack
        android[10].move(40,0)#jetpack
        android[11].move(40,0)#jetpack
        android[12].move(40,0)#jetpack
        android[13].move(40,0)#jetpack
        if checkJetpack(android):
            android[14].move(40,0)
        return "left"

    elif direction == "left":
        android[2].move(4,0)
        android[3].move(4,0)
       #LegR 
        android[5].move(12,0)
        android[7].move(-40,0) #jetpack
        android[8].move(-40,0)#jetpack
        android[9].move(-40,0)#jetpack
        android[10].move(-40,0)#jetpack
        android[11].move(-40,0)#jetpack
        android[12].move(-40,0)#jetpack
        android[13].move(-40,0)#jetpack
        if checkJetpack(android):
            android[14].move(-40,0)
        return "right"



#win = GraphWin("",200,200)
#android = createAndroid(win,100,100,"green")
#toggleJetpack(android,win,"right")


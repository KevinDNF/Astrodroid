from graphics import *


WALL_THICKNESS = 20
BALL_RADIUS    = 10


def init():

    global Player1
    global Player2 
    global ball

    makeMap() 
       
    Player1 = drawRectangle(Point(20,500),Point(40,520), "red", "white")
    Player2 = drawRectangle(Point(1000,500),Point(1020,520), "blue", "white")
    ball    = Circle(Point(500,500),BALL_RADIUS)
    ball.draw(win)

def makeMap():

    global win
    win = GraphWin("game" , 1280, 720)
    win.setBackground("grey")

    drawRectangle(Point(0,0),Point(1280, WALL_THICKNESS ),"black")
    drawRectangle(Point(0,0),Point(WALL_THICKNESS , 720),"black" )
    drawRectangle(Point(0,720 - WALL_THICKNESS),Point(1280,720),"black")

def drawRectangle(p1, p2, color, outline = None):
    r = Rectangle(p1,p2)
    r.setFill(color)

    if outline != None:
        r.setOutline(outline)
    else:
        r.setOutline(color)
    
    r.draw(win)
    return r

def keyBinds(userKey):

#--------------Player 1-------------    
    if userKey == "d": 
        Player1.move(20,0)
    elif userKey == "a": 
        Player1.move(-20,0)
    elif userKey == "space":
        Player1.move(0,10)


#--------------Player 2-------------    

    if userKey == "d": 
        Player2.move(20,0)
    elif userKey == "a": 
        Player2.move(-20,0)
    elif userKey == "space":
        Player2.move(0,-10)


def jump(player):

    ground = player.x
    ground 
    if jumping = True:
        accel += 1
        if accel  10


def moveBall():

    speed_x = 0
    speed_y = 0
    
    
    ball.move(speed_x,speed_y)    

def updateGame():
  
    keyBinds(win.checkKey())
    


def main():

    init()
    
    while True:
        
        updateGame()
   


main()



#KevinDNF - Astrodroid

from graphics import *
from drawShapes import *
from androidGenerator import *
from mapGenerator import *
import os
#-----------------------
#-To-Do
#
# Get rid of CLI use GUI
# Read number of files in Level folder for "infinite" levels
# Fix air walking
#
#------------------------UI-------------------------------------

def getIntputs():

    avalColor = ["red","green","blue","magenta"
              ,"cyan","orange","brown","pink"]
    color = ""
    
    while color not in avalColor:
        
        color = input(
         "\n Pick a colour for you android from the following... "
         "\n Color {0}: ".format(avalColor)).lower()

    return color 

#------------------------DrawGame-------------------------------------

def drawScene(win,color,x,y,path):
   
    clearScene(win)
    drawStars(win) 
    gameMap, apples = drawMap(win,path) 
    player1 = createAndroid(win,x,y,color) 

    return win , player1 , gameMap ,apples

def clearScene(win):
    for item in win.items[:]:
        item.undraw()

#------------------------Movement-------------------------------------

def checkKeys(win,android,gameMap,speedX,speedY,direction,frame):
    speedChange = 0.06
    key = win.checkKey()

    if checkJetpack(android) == True: 
        speedX,speedY,direction,frame = movementFlying(android,speedX,speedY
                                            ,speedChange,key,direction,frame) 
    else: #NOT FLYING
        speedX,speedY,direction,frame = movementGround(android,speedX,speedY
                                            ,key,direction,frame,win,gameMap)
    if key == "space": toggleJetpack(android,win,direction)
    if key == "u":death(win,android,0)

    return speedX, speedY, direction, frame

def movementFlying(android,speedX,speedY,speedChange,key,direction,frame):
    
    if key == "Left" or key == "a":
        speedX = speedX - speedChange
        if speedX <= -1: speedX = -1
        
        #-----------Animation------- 
        if direction != "left": #change to Left then check outside loop
            direction = invertPoscition(android,direction) 
        frame = frame + 0.5
        if frame >= 2 :
            frame = 0
        animateWalk(android,frame)
        #-----------Animation------- 

    elif key == "Right" or key == "d":
        speedX = speedX + speedChange
        if speedX >= 1: speedX = 1
        
        #-----------Animation------- 
        if direction != "right": 
            direction = invertPoscition(android,direction)
        frame = frame + 0.5
        if frame >= 2 :
            frame = 0
        animateWalk(android,frame)
        #-----------Animation------- 
   
    speedY = speedY - 0.01
    if speedY <= -0.3: speedY = -0.3 


    return speedX,speedY,direction,frame

def movementGround(android,speedX,speedY,key,direction,frame,win,gameMap):
    speedX = 0
    if key == "Left" or key == "a":
        
        for smoothMove in range(7):
            side = collisionDetection(win,gameMap,android,"1")
            if side == False:
                move(android,-0.7,0)
            elif "left" in side:
                move(android,0.8,0)

        #-----------Animation------- 
        frame = frame + 0.5
        if frame >= 2 :
            frame = 0
        
        animateWalk(android,frame)
        if direction != "left":
           direction = invertPoscition(android,direction)        
        
        #-----------Animation------- 
        
              
    elif key == "Right" or key == "d":

        for smoothMove in range(7):
            side = collisionDetection(win,gameMap,android,"1")
            if side == False:
                move(android,0.7,0)
            elif "right" in side:
                move(android,-0.8,0) 
         
        #-----------Animation------- 
        frame = frame + 0.5
        if frame >= 2:
            frame = 0
        animateWalk(android,frame)
        if direction != "right": 
            direction = invertPoscition(android,direction)

        #-----------Animation------- 

    return speedX,speedY,direction,frame

def gravity(speedY):
    
    force = 0.003
    speedY += force 
    if speedY >= 1: speedY = 1
    return speedY

#------------------------Collision-------------------------------------

def appleCollide(win,android,gameMap,apples,score):
    for y in range(len(gameMap)):
        for x in range(len(gameMap[0])-1):
            if gameMap[y][x] == "a":
                if blockToBlock(win,gameMap,x,y,android) != False:
                    apples ,score = deleteApple(win,x,y,gameMap,apples,score)

    return apples , score

def onMapCollide(android,side,speedX,speedY):

    if side != False:

        x = 0
        y = 0

        if "bottom" in side:
            speedY = 0
            y = -0.5

        if "top" in side:
            speedY = 0
            y = 0.5

        if "left" in side:
            speedX = 0
            x = 0.5

        if "right" in side:
            speedX = 0 
            x = -0.5

        move(android,x,y)
        
    return speedX, speedY

#------------------------GameLoop-------------------------------------

def playGame(win, android, gameMap, apples,color,score):
    speedX =    0
    speedY = 0
    direction = "right"
    won = False
    lost = False

    frame = 1

    while not won and not lost:
        speedX , speedY, direction ,frame = checkKeys(win,android,gameMap,
                                            speedX,speedY,direction,frame)

        speedX, speedY = onMapCollide(android,
                collisionDetection(win,gameMap,android,"1"),speedX,speedY) 
        
        apples , score = appleCollide(win,android,gameMap,apples,score)
        if collisionDetection(win,gameMap,android,"2") != False: lost = True
        if collisionDetection(win,gameMap,android,"e") != False: won = True

        speedY = gravity(speedY) 
        move(android,speedX,speedY) 
    
    if won == True:
        print("You Won! ","Score = {0}".format(score) )
    if lost == True:
        death(win,android,score)

    return score

def loadLevels(path):
    levels = os.listdir(path)
    levels.sort()
    return levels, path

def main():
    levels, path = loadLevels("Levels/")
    color = getIntputs()
    win = GraphWin("Astrodroid" , 800, 600)
   
    score = 0

    for level in levels:
        win , player1, gameMap, apples = drawScene(win,color,200,300,path + str(level)) 
        score = playGame(win, player1, gameMap,apples,color,score) 
   
    clearScene(win)
    print("Congratulation, You won the game")
    drawText(win,"Congratulations, \n"
                "You Won  :) \n " +
                "Score: {0}".format(score),
                Point(win.width/2,win.height/2),30,"white","times roman","bold")

main() 

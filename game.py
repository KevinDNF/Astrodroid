#KevinDNF - Python Game Competition 
#UP849868

from graphics import *
from random import random
from drawShapes import *
from androidGenerator import *
from mapGenerator import *
#------------------------------------

#------------------------------------

def getIntputs():

    #same code that i used in my coursework :)
    avalColor = ["red","green","blue","magenta"
              ,"cyan","orange","brown","pink"]
   
    selectedColors = [] #def var for loops
    color = ""
    
    while color not in avalColor:
        
        color = input(
         "\n Pick a colour for you android from the following... "
         "\n Color {0}: ".format(avalColor)).lower()
        #Users can now enter Red, green or even gReEn

    selectedColors.append(avalColor.pop(avalColor.index(color))) 
    #Pops color and appends it to selectedColors
    return selectedColors 

def drawAndroid(win,color):
     
    player1 = createAndroid(win,200,300,color) #androidGenerator.py
 #   player2 = createAndroid(win,100,200,"blue")
    
    return player1
    
# def drawApples(win, numberOfApples): #Change to a random enemy generator
# 
#     apples = []
#     for i in range(numberOfApples):
#         x = random() * 1000
#         y = random() * 1000
#         apple = Circle(Point(x,y), 10)
#         apple.setFill("red")
#         apple.setOutline("red")
#         apple.draw(win)
#         apples.append(apple)
#     return apples

def drawScene(color,path):
    
    win = GraphWin("Apple Chaser" , 800, 600)
    drawStars(win) 
    gameMap ,apples = drawMap(win,path) #mapGenerator.py
    player1 = drawAndroid(win,color) 

    return win , player1 , gameMap ,apples

def checkKeys(win, speedX, speedY, android,gameMap,direction,frame):
    speedChange = 0.06
    key = win.checkKey()

    if checkJetpack(android) == True: 
        speedX,speedY,direction,frame = movementFlying(speedChange,key,android,direction,speedX,speedY,frame) 
    else: #NOT FLYING
        speedX,speedY,direction,frame = movementGround(key,android,direction,speedX,speedY,frame,gameMap,win)
    if key == "space": toggleJetpack(android,win,direction)
    
    if key == "u":death(android)

    return speedX, speedY , direction, frame


def movementFlying(speedChange,key,android,direction,speedX,speedY,frame):
    
    if key == "Left" or key == "a":
        if direction != "left": 
            direction = invertPoscition(android,direction) 
        speedX = speedX - speedChange
        if speedX <= -1: speedX = -1
        frame = frame + 0.5
        if frame >= 2 :
            frame = 0
        
        animateWalk(android,frame)

    elif key == "Right" or key == "d":
        if direction != "right": 
            direction = invertPoscition(android,direction)
        speedX = speedX + speedChange
        if speedX >= 1: speedX = 1
        frame = frame + 0.5
        if frame >= 2 :
            frame = 0
        
        animateWalk(android,frame)
   
    speedY = speedY - 0.01
    if speedY <= -0.3: speedY = -0.3 


    return speedX,speedY,direction,frame

def movementGround(key,android,direction,speedX,speedY,frame,gameMap,win):
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

def appleCollide(win,android,gameMap,apples,score):
    for y in range(len(gameMap)):
        for x in range(len(gameMap[0])-1):
            if gameMap[y][x] == "a":
                if blockToBlock(win,gameMap,x,y,android) != False:
                    apples ,score = deleteApple(win,x,y,gameMap,apples,score)

    return apples , score

def playGame(win, android, map, apples,currentLevel,color):
    speedX = 0
    speedY = 0
    direction = "right"
    score = 0
    won = False
    lost = False

    frame = 1

    while not won and not lost:
        speedX , speedY, direction ,frame = checkKeys(win, speedX, speedY, 
                                                    android,map,direction,frame)

        speedX, speedY = onMapCollide(android,
                collisionDetection(win,map,android,"1"),speedX,speedY) 
        
        apples , score = appleCollide(win,android,map,apples,score)
        if collisionDetection(win,map,android,"2") != False: lost = True
        if collisionDetection(win,map,android,"e") != False: won = True

        speedY = gravity(speedY) 
        move(android,speedX,speedY) 
    
    if won == True:
        print("You Won! ","Score = {0}".format(score) )
        nextLevel(currentLevel,win,color)
    if lost == True:
        death(android,score)
        

def nextLevel(currentLevel,win,color):
    
    
    win.close()
    currentLevel += 1
    
    if currentLevel == 2:
        path = "Levels/level2.txt"
        win , player1, gameMap, apples = drawScene(color,path) 
        playGame(win, player1, gameMap,apples,currentLevel,color) 

    elif currentLevel == 3:
        path = "Levels/level3.txt"
        win , player1, gameMap, apples = drawScene(color,path) 
        playGame(win, player1, gameMap,apples,currentLevel,color) 

    if currentLevel == 4:
        print("Congratulation, You won the game")


def onMapCollide(android,side,speedX,speedY):

    if side != False:

        #print(side)
        x = 0
        y = 0

        if "bottom" in side:
            #print("bottom")
            speedY = 0
            y = -0.5
            #move
            #speedY = 1 for bouncy walls

        if "top" in side:
            #print("top")
            speedY = 0
            y = 0.5

        if "left" in side:
            #print("left")
            speedX = 0
            x = 0.5

        if "right" in side:
            #print("right")
            speedX = 0 
            x = -0.5

        move(android,x,y)
        
    return speedX, speedY

def main():
    level = 1
    color = getIntputs()
    win , player1, gameMap, apples = drawScene(color,"Levels/level1.txt") 
    playGame(win, player1, gameMap,apples,level,color) 
    
main() 

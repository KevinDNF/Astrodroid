#KevinDNF - Python Game Competition 
#UP849868

from graphics import *
from drawing import *
from mathEquations import *
from random import random

#------------------------------------

#------------------------------------

def getIntputs():
    numberOfApples = eval(input("Enter # of Apples: "))
    return numberOfApples

def drawAndroid(win):
    
#  head = drawCircle(win,Point(0.5, 0.5), 0.03,"green")
#  body = drawRect(win,Point(0.47, 0.45), Point(0.53, 0.5,"green"))
#  leg1 = drawRect(win,Point(0.48, 0.42), Point(0.49, 0.45,"green"))
#  leg2 = drawRect(win,Point(0.52, 0.42), Point(0.51, 0.45,"green"))
#  arm1 = drawRect(win,Point(0.53, 0.46), Point(0.54, 0.5,"green"))
#  arm2 = drawRect(win,Point(0.46, 0.46), Point(0.47, 0.5,"green"))
#  eye1 = drawCircle(win,Point(0.49, 0.51), 0.005,"white")
#  eye2 = drawCircle(win,Point(0.51, 0.51), 0.005,"white")
#  android = [head, body, leg1, leg2, 
#              arm1, arm2, eye1, eye2]


    
    body = drawRect(win,Point(50,50),Point(90,100),"forest green")

    android = [body]
    return android


def drawApples(win, numberOfApples):

    apples = []
    for i in range(numberOfApples):
        x = random() * 1000
        y = random() * 1000
        apple = Circle(Point(x,y), 10)
        apple.setFill("red")
        apple.setOutline("red")
        apple.draw(win)
        apples.append(apple)
    return apples

       
def drawScene():
    
    global win
    win = GraphWin("Android" , 800, 500)
    win.setBackground("dark orange")
    android = drawAndroid(win)
    apples = drawApples(win, 20)
    drawRect(win,Point(0,0),Point(1280,20),"black")
    return win , android,apples


def checkKeys(win, speedX, speedY):
    speedChange = 0.003
    key = win.checkKey()
    if key == "Left":
        speedX = speedX - speedChange
    elif key == "Right":
        speedX = speedX + speedChange
    elif key == "Down":
        speedY = speedY - speedChange
    elif key == "Up":
        speedY = speedY + speedChange
    return speedX, speedY


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


def playGame(win, android , apples):
    speedX = 0
    speedY = 0 
    won = False
    lost = False
    while not won and not lost:
        speedX , speedY = checkKeys(win, speedX, speedY)

        for part in android:
            part.move(speedX, speedY)




def main():

    win , android, apples = drawScene() 
    playGame(win, android, apples) 


main()



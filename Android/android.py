#KevinDNF - Python Game Competition 
#UP849868

from graphics import *
from drawing import *


#------------------------------------

#------------------------------------

def createAndroid(win):
    
   head = drawCircle(win,Point(0.5, 0.5), 0.03,"green")
   body = drawRect(win,Point(0.47, 0.45), Point(0.53, 0.5,"green"))
   leg1 = drawRect(win,Point(0.48, 0.42), Point(0.49, 0.45,"green"))
   leg2 = drawRect(win,Point(0.52, 0.42), Point(0.51, 0.45,"green"))
   arm1 = drawRect(win,Point(0.53, 0.46), Point(0.54, 0.5,"green"))
   arm2 = drawRect(win,Point(0.46, 0.46), Point(0.47, 0.5,"green"))
   eye1 = drawCircle(win,Point(0.49, 0.51), 0.005,"white")
   eye2 = drawCircle(win,Point(0.51, 0.51), 0.005,"white")
   android = [head, body, leg1, leg2, 
              arm1, arm2, eye1, eye2]

   return android

def init():

    makeMap() 
       
def makeMap():

    global win
    win = GraphWin("game" , 700, 700)
    win.setBackground("grey")
    win.setCoords(0,0,1,1)
    drawRect(win,Point(0,0),Point(1280,20),"black", "white")

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


def updateGame():
  
    keyBinds(win.checkKey())

def main():

    init()
    createAndroid(win) 
    while True:
        
        updateGame()
   


main()



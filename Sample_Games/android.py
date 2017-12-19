#==============================================================================
# android.py
# in-class demo of design using lists
#==============================================================================

from graphics import *

def getInputs():
    numberOfapples = eval(input("Enter number of apples: "))
    return numberOfapples


def drawAndroid(win):
    head = Circle(Point(0.5, 0.5), 0.03)
    body = Rectangle(Point(0.47, 0.45), Point(0.53, 0.5))
    leg1 = Rectangle(Point(0.48, 0.42), Point(0.49, 0.45))
    leg2 = Rectangle(Point(0.52, 0.42), Point(0.51, 0.45))
    arm1 = Rectangle(Point(0.53, 0.46), Point(0.54, 0.5))
    arm2 = Rectangle(Point(0.46, 0.46), Point(0.47, 0.5))
    eye1 = Circle(Point(0.49, 0.51), 0.005)
    eye2 = Circle(Point(0.51, 0.51), 0.005)
    android = [head, body, leg1, leg2, 
               arm1, arm2, eye1, eye2]
    for part in android:
        if part in [eye1, eye2]:
            colour = "white"
        else:
            colour = "green"
        part.setFill(colour)
        part.setOutline(colour)
        part.draw(win)
    return android


def drawApples(win, numberOfApples):
    from random import random
    apples = []
    for i in range(numberOfApples):
        x = random()
        y = random()
        apple = Circle(Point(x, y), 0.03)
        apple.setFill("red")
        apple.setOutline("red")
        apple.draw(win)
        apples.append(apple)
    return apples

    
def drawScene(numberOfApples):
    win = GraphWin("Android", 700, 700)
    win.setCoords(0, 0, 1, 1)
    android = drawAndroid(win)
    apples = drawApples(win, numberOfApples)
    return win, android, apples


def checkKeys(win, speedX, speedY):
    speedChange = 0.00003
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


def distanceBetweenPoints(p1, p2):
    import math
    return math.sqrt((p1.getX() - p2.getX()) ** 2 + 
                     (p1.getY() - p2.getY()) ** 2)

def playGame(win, android, apples):
    speedX = 0
    speedY = 0
    won = False
    lost = False
    while not won and not lost:
        # check speed change via key press
        speedX, speedY = checkKeys(win, speedX, speedY)

        # move android
        for part in android:
            part.move(speedX, speedY)

        # check hit edge
        centre = android[0].getCenter()
        lost = centre.getX() < 0 or centre.getX() > 1 or \
               centre.getY() < 0 or centre.getY() > 1

        # check hit apple
        # should replace (we shouldn't remove on element from sequence
        # that we're looping over)
        for apple in apples:
            if distanceBetweenPoints(centre, apple.getCenter()) < 0.04:
                apple.undraw()
                apples.remove(apple)
        
        # check whether won
        won = len(apples) == 0
    
    # game over message
    message = Text(Point(0.5, 0.5), "")
    message.setSize(20)
    if won:
        message.setText("You've won!")
    else:
        message.setText("Game over!")
    message.draw(win)
        
       
def main():
    numberOfApples = getInputs()
    win, android, apples = drawScene(numberOfApples)
    playGame(win, android, apples)
    
main()

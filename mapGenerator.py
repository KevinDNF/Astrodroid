from graphics import *
from drawShapes import *

#To-Do
#Add a spawn point to the map file

def readFile(path):
   
    dataInFile = open(path, "r") 
    content = dataInFile.readlines()
    return content 

def drawMap(win,path):
    apples = []
    gameMap = readFile(path)
    win.setBackground("darkblue")
    #Integer Division to keep in inside the screen
    blockH = win.height // len(gameMap) 
    blockW = (win.width // len(gameMap[0]))+1

    for y in range(len(gameMap)):
        for x in range(len(gameMap[0])-1):
            if gameMap[y][x] == "x": #change to 0 to see AIR
                drawRect(win,Point(x*blockW,y*blockH),
                        Point((x+1)*blockW,(y+1)*blockH),None,"black") 
                
            elif gameMap[y][x] == "1": #Collision Block 
                drawRect(win,Point(x*blockW,y*blockH),
                        Point((x+1)*blockW,(y+1)*blockH),"light blue","darkblue")
            
            elif gameMap[y][x] == "2": #Spikes
                drawMine(win,x,y,blockW,blockH)                
            elif gameMap[y][x] == "a": # Apples
                apples.append(drawApple(win,x*blockW,y*blockH,"red"))

            elif gameMap[y][x] == "e": #End
                drawRect(win,Point(x*blockW,y*blockH),
                        Point((x+1)*blockW,(y+1)*blockH),"white","white")
 
    return gameMap , apples

def drawMine(win,ix,iy,blockW,blockH):
    
    wMid = (blockW*ix) + (blockW/2)
    hMid = (blockH*iy) + (blockH/2)

    drawCircle(win,Point(wMid,hMid),8,"dark cyan","black")
    drawCircle(win,Point(wMid,iy*blockH+4),3,"light blue","black")
    drawCircle(win,Point(wMid,((iy+1)*blockH)-4),3,"light blue","black")
    drawCircle(win,Point(ix*blockW+4,hMid),3,"cyan","black")
    drawCircle(win,Point(((ix+1)*blockW)-4,hMid),3,"cyan","black")

#    drawRect(win,Point(ix*25,iy*25),Point((ix+1)*25,(iy+1)*25),None,"black")

def drawApple(win,x1,y1,colour):

    leaf = drawOval(win,Point(x1+9,y1+5),Point(x1+18,y1+0),"green","green")
    stem = drawRect(win,Point(x1+8.5,y1+7),Point(x1+11,y1-2),"black","black")
    body1 = drawOval(win,Point(x1,y1+25),Point(x1+11.5,y1+5),"red","red")
    body2 = drawOval(win,Point(x1+8.5,y1+25),Point(x1+20,y1+5),"red","red")
    extra = drawRect(win,Point(x1+6.25,y1+25),Point(x1+14.75,y1+20),"red","red")
    highlight = drawOval(win,Point(x1+15,y1+13),Point(x1+17,y1+10),"white","white")
    apple = [leaf,stem,body1,body2,extra,highlight]

    return apple


def deleteApple(win,x,y,gameMap,apples,score):

    x1 = x*((win.width // len(gameMap[0]))+1)
    y1 = y*(win.height // len(gameMap))

    for apple in apples:
        if apple[4].p1.x == x1+6.25:
            #print("found")
            for part in apple:
                part.undraw()
            apples.remove(apple)
            score += 1
            print("Well Done! you got an apple!",
                    " \n Current score: ",score)
    return apples ,score 


def collisionDetection(win,gameMap,android,blockType):
    
    sides = []
    for y in range(len(gameMap)):
        for x in range(len(gameMap[0])-1):
            if gameMap[y][x] == blockType:
                checkSides = blockToBlock(win,gameMap,x,y,android)
                if checkSides != False : sides.append(checkSides)
    
    if len(sides) == 0:
        return False
    else:
        return sides

def blockToBlock(win,gameMap,ix,iy,android): #ix = block index x

    bW = (win.width // len(gameMap[0]))+1
    bH = win.height // len(gameMap) 

    bx1 = ix * bW
    by1 = iy * bH
    
    bx2 = bx1 + bW
    by2 = by1 + bH 
    
    ax1 = android[1].p1.x  
    ax2 = android[1].p2.x 
   
    ay1 = android[1].p1.y -15
    ay2 = android[1].p2.y +15
    
    if ax1<=bx2 and ax2>=bx1 and ay1<=by2 and ay2>=by1:
       

        if int(ay2) == int(by1): 
            return "bottom"

        if int(ay1)+1 == int(by2): 

            return "top"          
        if int(ax1)+1 == int(bx2):
            return "left"
        
        if int(ax2) >= int(bx1):
            return "right"
    
        return True
    return False


def drawStars(win):
    from random import random
    for i in range(500):
        x = random() * 1000
        y = random() * 1000
        star = Point(x,y).draw(win)
        star.setFill("white")


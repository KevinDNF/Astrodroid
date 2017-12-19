#==============================================================================
# squash.py
# In-class program design demo
# k moves bat up, m moves bat down
#==============================================================================

from graphics import *

WALL_THICKNESS = 0.05
BAT_WIDTH = 0.15
BAT_X = 0.85
BAT_THICKNESS = 0.05
BALL_RADIUS = 0.03

def main():
    court = makeCourt()
    ball = makeBall(court)
    bat = makeBat(court)
    playGame(court, ball, bat)

def makeCourt():
    court = GraphWin("Squash", 500, 500)
    court.setCoords(0, 0, 1, 1)
    drawRectangle(court, Point(0, 0), Point(1, WALL_THICKNESS), "black")
    drawRectangle(court, Point(0, 1), Point(1, 1 - WALL_THICKNESS), "black")
    drawRectangle(court, Point(0, WALL_THICKNESS),
                  Point(WALL_THICKNESS, 1 - WALL_THICKNESS), "black")
    return court
    
def playGame(court, ball, bat):
    speedX = -0.00004
    speedY = 0.00002
    gameOver = False
    while not gameOver:
        speedX, speedY = checkBallHitWall(ball, speedX, speedY)
        speedX = checkBallHitBat(ball, bat, speedX)
        ball.move(speedX, speedY)
        checkMoveBat(court, bat)
        gameOver = ball.getCenter().getX() > 1
        
def checkBallHitWall(ball, speedX, speedY):
    centre = ball.getCenter()
    if centre.getX() - BALL_RADIUS < WALL_THICKNESS:
        speedX = -speedX
    if centre.getY() + BALL_RADIUS >= 1 - WALL_THICKNESS or \
       centre.getY() - BALL_RADIUS <= WALL_THICKNESS:
        speedY = -speedY
    return speedX, speedY

def checkBallHitBat(ball, bat, speedX):
    ballCentre = ball.getCenter()
    ballX = ballCentre.getX() + BALL_RADIUS
    ballY = ballCentre.getY()
    topBat = bat.getP2().getY()
    botBat = bat.getP1().getY()
    
    if ballX >= BAT_X and ballX <= BAT_X + speedX and \
       ballY >= botBat and ballY <= topBat:
        speedX = -speedX
    return speedX

def checkMoveBat(court, bat):
    key = court.checkKey()
    if key == "k":
        bat.move(0, 0.05)
    elif key == "m":
        bat.move(0, -0.05)
    
def makeBat(court):
    bat = drawRectangle(court, Point(BAT_X, 0.5 - BAT_WIDTH / 2),
                        Point(BAT_X + BAT_THICKNESS, 0.5 + BAT_WIDTH / 2),
                        "blue")
    return bat

def makeBall(court):
    ball = Circle(Point(0.5, 0.5), BALL_RADIUS)
    ball.setFill("red")
    ball.setOutline("red")
    ball.draw(court) 
    return ball

def drawRectangle(win, point1, point2, colour):
    rectangle = Rectangle(point1, point2)
    rectangle.setFill(colour)
    rectangle.setOutline(colour)
    rectangle.draw(win)  
    return rectangle  
    
main()


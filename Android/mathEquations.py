from math import *

def distanceBetweenPoints(p1,p2):
    return math.sqrt((p1.getX() - p2.getX()) ** 2 +
            (p1.getY() - p2.getY()) ** 2)



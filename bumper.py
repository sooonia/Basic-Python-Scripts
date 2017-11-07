#Sonia Kopel
#Bumper.py
#This is a random bumper car simulation
#cars stay in window and change color on collision 
#There are no inputs or outputs

from graphics import *
from random import *

def randCircCenter(height, width, radius):
    yCoord = randrange(radius, height-radius)
    xCoord = randrange(radius, width-radius)
    center = Point(xCoord, yCoord)
    return center
    
def dx():
    num = choice([-4,-3,3,4])
    return num

def dy():
    num = choice([-4,-3,3,4])
    return num

def collide(circ1, circ2, radius):
    cent1=circ1.getCenter()
    cent2=circ2.getCenter()
    X1 = cent1.getX()
    X2 = cent2.getX()
    Y1 = cent1.getY()
    Y2 = cent2.getY()
    if ((X1-X2)**2+(Y1-Y2)**2)<(2*radius)**2:
        result = True
    else:
        result = False
    return result
    
def vertHit(circ,height,radius):
    center = circ.getCenter()
    y = center.getY()
    if y < radius or y > height-radius:
        result = True
    else:
        result = False
    return result
    
def horHit(circ,width,radius):
    center = circ.getCenter()
    x = center.getX()
    if x<radius or x > (width-radius):
        result = True
    else:
        result = False
    return result

def randColor():
    color=color_rgb(randrange(0,256),randrange(0,256),randrange(0,256))
    return color
        
def main():
    height = 400
    width = 500
    win=GraphWin("Bumper Cars", width, height)
    radius = 20
    circ1=Circle(randCircCenter(height, width, radius),radius)
    circ1.draw(win)
    circ1.setFill(randColor())
    circ2=Circle(randCircCenter(height, width, radius),radius)
    circ2.draw(win)
    circ2.setFill(randColor())
    numReps= 1000
    dx1=dx()
    dx2=dx()
    dy1=dy()
    dy2=dy()
    
    for i in range(numReps):
        circ1.move(dx1,dy1)
        if vertHit(circ1,height, radius):
            dy1= -1*dy1
            circ1.setFill(randColor())
        else:
            dy1= dy1 
        if horHit(circ1,width,radius):
            dx1= -1*dx1
            circ1.setFill(randColor())
        else:
            dx1=dx1
            
        circ2.move(dx2,dy2)
        if vertHit(circ2,height, radius):
            dy2= -1*dy2
            circ2.setFill(randColor())
        else:
            dy2= dy2
        if horHit(circ2,width,radius):
            dx2= -1*dx2
            circ2.setFill(randColor())
        else:
            dx2=dx2
        if collide(circ1, circ2, radius):
            dx1= -1*dx1
            dx2= -1*dx2
            dy1= -1*dy1
            dy2= -1*dy2
            circ1.setFill(randColor())
            circ2.setFill(randColor())
        else:
            dx1= dx1
            dx2= dx2
            dy1= dy1
            dy2= dy2
        time.sleep(.015)
    txtPt= Point(width/2,height-10)
    closeText=Text(txtPt,"Click to Close")
    closeText.setTextColor("black")
    closeText.draw(win)
    win.getMouse()
    win.close()
        
        
main()
    

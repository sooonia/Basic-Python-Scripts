#Sonia Kopel
#valentineGreeting.py
#I certify that this is entirely my own work
#This is a cute little greeting card program
#There are no inputs or outputs

from graphics import *
def valentineGreeting():
    
    #To make window
    width = 600
    length = 600
    win = GraphWin("Card",width,length)
    win.setBackground("Thistle")
    
    #To make heart and arrow
    circ1Cent = Point(width/3,length/3)
    circ1 = Circle(circ1Cent, 130)
    circ1.setFill("PaleVioletRed")
    circ1.setOutline("PaleVioletRed")
    circ1.draw(win)
    pointy = Polygon(Point(100,283),Point(500,283),Point(300,490))
    pointy.setFill("PaleVioletRed")
    pointy.setOutline("PaleVioletRed")
    pointy.draw(win)

    arrowPt1 = Point(30,500)
    arrowPt2 = Point(500,100)
    arrow=Line(arrowPt1,arrowPt2)
    arrow.setArrow("last")
    arrow.setWidth(5)
    arrow.setFill("white")
    arrow.setOutline("white")
    arrow.draw(win)
    arrow.move(-505,505)
    
    #to get 3D effect, draw circ2 last
    circ2Cent = Point(2*width/3,length/3)
    circ2 = Circle(circ2Cent, 130)
    circ2.setFill("PaleVioletRed")
    circ2.setOutline("PaleVioletRed")
    circ2.draw(win)
    

    #Text
    textPt = Point(width/2,length/3)
    text = Text(textPt, "Happy Valentines Day")
    text.setTextColor("white")
    text.setFace("courier")
    text.setStyle("italic")
    text.setSize(20)
    text.draw(win)

    #Heartbeat Animation
    pointy2=pointy.clone()
    circ3=circ1.clone()
    circ4=circ2.clone()
    pointy2.draw(win)
    circ3.draw(win)
    circ4.draw(win)
    for j in range(3):
        for i in range(15):
            pointy2.setWidth(i*2)
            circ3.setWidth(i*2)
            circ4.setWidth(i*2)
            time.sleep(.05)
        for i in range(30,0,-2):
            pointy2.setWidth(i)
            circ3.setWidth(i)
            circ4.setWidth(i)
            time.sleep(.05)
    circ3.undraw()
    circ4.undraw()
    pointy2.undraw()

    #Arrow Animation 
    for i in range(285):
        arrow.move(2,-2)
        time.sleep(.01)

    #To close
    time.sleep(1)
    txtPt= Point(width/2,length-10)
    closeText=Text(txtPt,"Click to Close")
    text.setTextColor("white")
    text.setFace("courier")
    closeText.draw(win)
    win.getMouse()
    win.close()
    
valentineGreeting()

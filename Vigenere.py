#Sonia Kopel
#Vigenere.py
#This program uses a graphical user interface to accept a message
##to be encoded and a key phrase
#Upon clicking in a button “Encode” the program will encode the message
##and then display the encoded message in a text area
#Clicking “Decode” results in the message being decoded
#Input: Keyword and message to en/decode
#output: en/decoding

from graphics import *

def code(encodeType, message, keyword):
    if encodeType=="encode":
        message=message.upper()
        messageList=message.split()
        charListM=[]
        for word in messageList:
            for char in word:
                charListM.append(ord(char)-ord("A"))
        keyword=keyword.upper()
        charListK=[]
        multiplier=len(charListM)//len(keyword) +1
        keyword=keyword*multiplier
        for char in keyword:
            charListK.append(ord(char)-ord("A"))
        charListC=[]
        for i in range(len(charListM)):
            codeNum = charListM[i]+charListK[i]+ord("A")
            if codeNum >=91:
                codeNum=codeNum-26
            charListC.append(codeNum)
        for i in range(len(charListC)):
            charListC[i]=chr(charListC[i])
        code=''.join(charListC)
    
    if encodeType == "decode":
        message=message.upper()
        charListM=[]
        for char in message:
            charListM.append(ord(char)-ord("A"))
        keyword=keyword.upper()
        charListK=[]
        multiplier=len(message)//len(keyword) +1
        keyword=keyword*multiplier
        for char in keyword:
            charListK.append(ord(char)-ord("A"))
        charListC=[]
        for i in range(len(message)):
            codeNum=charListM[i]-charListK[i]+ord("A")
            if codeNum < 65:
                codeNum=codeNum+26
            charListC.append(codeNum)
        for i in range(len(charListC)):
            charListC[i]=chr(charListC[i])
        code=''.join(charListC)
    return code


def main():
    height = 275
    width = 350
    win=GraphWin("Vigenere",width, height)
    win.setBackground("lightsteelblue")

    #draws buttons
    encodeRect=Rectangle(Point(90,190),Point(150,225))
    encodeRect.setFill("aliceblue")
    encodeRect.draw(win)
    encodeText=Text(encodeRect.getCenter(),"encode")
    encodeText.draw(win)
    
    decodeRect=Rectangle(Point(260,190),Point(200,225))
    decodeRect.setFill("aliceblue")
    decodeRect.draw(win)
    decodeText=Text(decodeRect.getCenter(),"decode")
    decodeText.draw(win)

    #draws input boxes and messages
    messageText=Text(Point(55,height/8),"Message to code:")
    messageText.setSize(9)
    messageText.draw(win)
    messageEntry=Entry(Point(225,height/8),26)
    messageEntry.draw(win)

    keywordText=Text(Point(55,height/4),"Enter Keyword:")
    keywordText.setSize(9)
    keywordText.draw(win)
    keywordEntry=Entry(Point(225,height/4),26)
    keywordEntry.draw(win)

    codeText=Text(Point(width/2,155),"")
    codeText.draw(win)
    subText=Text(Point(width/2,250),"")
    subText.draw(win)

    #Allows user to interact with system
    clickPt=win.getMouse()
    clickPtx=clickPt.getX()
    clickPty=clickPt.getY()
    message=messageEntry.getText()
    while message == "":
        codeText.setText("Enter a message.")
        clickPt=win.getMouse()
        message=messageEntry.getText()
    keyword=keywordEntry.getText()
    while keyword == "":
        codeText.setText("Enter a keyword.")
        clickPt=win.getMouse()
        keyword=keywordEntry.getText()
    if clickPtx >90 and clickPtx < 150 and clickPty < 225 and clickPty > 190:
        userCode=code("encode", str(message), str(keyword))
        codeText.setText("your code is " + userCode)
    elif clickPtx >200 and clickPtx < 260 and clickPty < 225 and clickPty > 190:
        userCode=code("decode", str(message), str(keyword))
        codeText.setText("your code is " + userCode)
    else:
        codeText.setText("You must click a box. Close window and try again.")
    subText.setText("click again to close")
    clickPt= win.getMouse()
    win.close()
    

main()

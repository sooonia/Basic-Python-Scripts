#Sonia Kopel
#hangman.py
#inputs: letters specified by user
#outputs: word reveal, hangman figure, prompts

import random
from graphics import *

def randomWord():
    infile=open("wordlist.txt")
    allWords = []
    for line in infile:
        wordList=line.split()
        for word in wordList:
            allWords.append(word)
    word = random.choice(allWords)
    return word

def letterFound(guess,secretWord):
    found = False
    for i in range(len(secretWord)):
        if secretWord[i] == guess:
            found = True
    return found

def letterPos(guess, secretWord):
    posList=[]
    i=0
    for char in secretWord:
        if char == guess:
            posList.append(i)
        i+=1
    return posList

def guessWord(guess,secretWord,guessedWord):
    if letterFound(guess,secretWord):
        posList=letterPos(guess, secretWord)
        for position in posList:
            guessedWord[position]=guess 
    return guessedWord

def letterGuessed(guess,guessList):
    value=False
    for char in guessList:
        if char==guess:
            value = True
    return value

def finished(secretWord,guessedWord):
    value=False
    secretWordList = []
    for char in secretWord:
        secretWordList.append(char)
    if secretWordList == guessedWord:
        value = True
    return value
    
def main():
    secretWord = randomWord()
    guessedWord=[]
    lettersGuessed=[]
    numGuesses = 7
        
    for char in secretWord:
        guessedWord.append("_")
    print(guessedWord)
    print("Number Guesses Remaing: " + str(numGuesses))
    guess = input("Guess a letter: ")
    
    while numGuesses > 1 and not finished(secretWord,guessedWord):
        if letterGuessed(guess,lettersGuessed):
            print("Letter already guessed")
            guess = input("Guess another letter: ")
            print()
        elif letterFound(guess,secretWord):
            guessedWord=guessWord(guess,secretWord,guessedWord)
            print(guessedWord)
            print("Number Guesses Remaing: " + str(numGuesses))
            lettersGuessed.append(guess)
            if not finished(secretWord,guessedWord):
                guess = input("Guess another letter: ")
            else:
                print("You Win!!")
            print()
        else:
            numGuesses -=1
            print("Number Guesses Remaing: " + str(numGuesses))
            lettersGuessed.append(guess)
            guess = input("Guess another letter: ")
            print()
    if numGuesses == 1:
        print("You Lose")
        print("the word was " + secretWord)
#main()
    
def userInterface():
    width=400
    height=550
    win=GraphWin("Hangman",width,height)
    win.setBackground("lightsteelblue")
    
    #Gallows
    base = Line(Point(width/3,height/2),Point(2*width/3,height/2))
    base.setWidth(3)
    base.draw(win)
    pole1= Line(Point(9*width/15,height/2),Point(9*width/15,height/6))
    pole1.setWidth(2)
    pole1.draw(win)
    pole2=Line(Point(9*width/15,height/6),Point(7*width/15,height/6))
    pole2.setWidth(2)
    
    pole2.draw(win)
    pole3=Line(Point(7*width/15,height/6),Point(7*width/15,5*height/24))
    pole3.setWidth(2)
    pole3.draw(win)

    #Man
    head=Circle(Point(7*width/15,5*height/24-10),10)
    head.setFill("black")
    neck=Line(Point(7*width/15,5*height/24-10),Point(7*width/15,5*height/24+10))
    body=Line(Point(7*width/15,5*height/24+10),Point(7*width/15,5*height/24+50))
    lArm=Line(Point(7*width/15-20,5*height/24+30),Point(7*width/15,5*height/24+20))
    rArm=Line(Point(7*width/15+20,5*height/24+30),Point(7*width/15,5*height/24+20))
    rLeg=Line(Point(7*width/15+30,5*height/24+90),Point(7*width/15,5*height/24+50))
    lLeg=Line(Point(7*width/15-30,5*height/24+90),Point(7*width/15,5*height/24+50))

    button=Rectangle(Point(width/2-30,2*height/3+40),Point(width/2+30,2*height/3+65))
    button.setFill("aliceblue")
    buttonText=Text(button.getCenter(),"Guess")
    button.draw(win)
    buttonText.draw(win)
    
    secretWord=randomWord()
    guessedWord=[]
    lettersGuessed=[]
    numGuesses = 7
        
    for char in secretWord:
        guessedWord.append("_")
    guessText=Text(Point(width/2,height/2+35),guessedWord)
    guessText.setSize(20)
    guessText.draw(win)
    numGuessText=Text(Point(width/2,height/2+68),"Number Guesses Remaing: " + str(numGuesses))
    numGuessText.setSize(10)
    numGuessText.draw(win)
    promptText=Text(Point(width/2,height/2+88),"Guess a letter:")
    guessLetter = Entry(Point(width/2,height/2+105),1)
    guessLetter.draw(win)
    win.getMouse()
    guess=guessLetter.getText()
    otherText=Text(Point(width/2,height/2+125),"")
    otherText.setSize(10)
    otherText.draw(win)
    

    while numGuesses >= 1 and not finished(secretWord,guessedWord):
        if letterGuessed(guess,lettersGuessed):
            otherText.setText("Letter already guessed")
            guessLetter = Entry(Point(width/2,height/2+105),1)
            guessLetter.draw(win)
            win.getMouse()
            guess=guessLetter.getText()
            otherText.setText("")
        elif letterFound(guess,secretWord):
            guessedWord=guessWord(guess,secretWord,guessedWord)
            guessText.setText(guessedWord)
            numGuessText.setText("Number Guesses Remaing: " + str(numGuesses))
            lettersGuessed.append(guess)
            if not finished(secretWord,guessedWord):
                guessLetter = Entry(Point(width/2,height/2+105),1)
                guessLetter.draw(win)
                win.getMouse()
                guess=guessLetter.getText()
            
            else:
                otherText.setText("You Win!!")
        else:
            numGuesses -=1
            numGuessText.setText("Number Guesses Remaing: " + str(numGuesses))
            lettersGuessed.append(guess)
            if numGuesses == 6:
                head.draw(win)
            elif numGuesses == 5:
                neck.draw(win)
            elif numGuesses == 4:
                body.draw(win)
            elif numGuesses == 3:
                rArm.draw(win)
            elif numGuesses == 2:
                lArm.draw(win)
            elif numGuesses == 1:
                rLeg.draw(win)
            if numGuesses == 0:   
                lLeg.draw(win)
                otherText.setText("You Lose; the word was " + secretWord)
            else:
                guessLetter = Entry(Point(width/2,height/2+105),1)
                guessLetter.draw(win)
                win.getMouse()
                guess=guessLetter.getText()


    if numGuesses>0:
        otherText.setText("You win!!!!")
    
    txtPt= Point(width/2,height-10)
    closeText=Text(txtPt,"Click to Close")
    closeText.setTextColor("black")
    closeText.draw(win)
    win.getMouse()
    win.close()    
    
userInterface()

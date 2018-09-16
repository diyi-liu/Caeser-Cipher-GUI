# Caesar Cipher Program v2.0
from graphics import *

def encode(plaintext, key):
    cipherlist = []
    length = len(plaintext)
    for i in range(0, length, 1):
        if ord(plaintext[i]) == 32:
            cipherNum = 32
            cipherlist.append(chr(cipherNum))
        else:
            cipherNum = ord(plaintext[i]) + key
            if 65 <= cipherNum <= 90 or 97 <= cipherNum <= 122:
                cipherlist.append(chr(cipherNum))
            else:
                cipherlist.append(chr(cipherNum))
    ciphertext = "".join(cipherlist)
    return ciphertext

def getWin(name, width, height):
    win = GraphWin(name, width, height)
    return win

def greenText(x, y, text):
    text = Text(Point(x, y), text)
    text.setTextColor("green")
    return text

def greenButton(point, text):
    text = Text(point, text)
    text.setTextColor("green")
    return text

def getEntry(x, y, width):
    entry = Entry(Point(x, y), width)
    return entry

def encoder(response):
    win = getWin("Caesar Cipher Program", 400, 300)
    win.setCoords(0, 0, 4.0, 4.0)
    win.setBackground("black")
    plainIcon = greenText(1, 3, "Input Plaintext here:")
    plainIcon.draw(win)
    input1 = getEntry(3, 3, 20)
    input1.draw(win)
    keyIcon = greenText(1, 2.5, "Input Key here:")
    keyIcon.draw(win)
    input2 = getEntry(3, 2.5, 20)
    input2.draw(win)
    rect = Rectangle(Point(1.65, 2), Point(2.35, 1.5))
    rect.setFill("black")
    rect.setOutline("green")
    rect.draw(win)
    rectCenter = rect.getCenter()
    encodeIcon = greenButton(rectCenter, "Encode")
    encodeIcon.draw(win)
    outputIcon = greenText(1, 1, "Ciphertext:")
    outputIcon.draw(win)
    while response == "Y":
        win.getMouse()
        plaintext = input1.getText()
        key = eval(input2.getText())
        output = greenText(3, 1, encode(plaintext, key))
        output.draw(win)
        encodeIcon.undraw()
        resetIcon = greenButton(rectCenter, "Reset")
        resetIcon.draw(win)
        continueIcon = greenText(1, 0.5, "Encode another message? Y/N: ")
        continueIcon.draw(win)
        continueEntry = getEntry(3, 0.5, 5)
        continueEntry.draw(win)
        win.getMouse()
        response = continueEntry.getText()
        output.undraw()
        resetIcon.undraw()
        encodeIcon.draw(win)
        input1.undraw()
        input2.undraw()
        input1 = getEntry(3, 3, 20)
        input2 = getEntry(3, 2.5, 20)
        input1.draw(win)
        input2.draw(win)
        continueIcon.undraw()
        continueEntry.undraw()
    plainIcon.undraw()
    input1.undraw()
    keyIcon.undraw()
    input2.undraw()
    rect.undraw()
    resetIcon.undraw()
    encodeIcon.undraw()
    outputIcon.undraw()
    continueIcon.undraw()
    continueEntry.undraw()
    thanks = Text(Point(2, 2), "Thanks for Using!")
    thanks.setTextColor("green")
    thanks.setSize(20)
    thanks.draw(win)
    win.getMouse()
    win.close()

def main():
    encoder("Y")

main()

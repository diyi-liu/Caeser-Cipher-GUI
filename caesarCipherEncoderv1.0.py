# Caesar Cipher Program v1.0
from graphics import *

def encode(plaintext, key):
    cipherlist = []
    length = len(plaintext)
    for i in range(0, length, 1):
        cipherNum = ord(plaintext[i]) + key
        if 65 <= cipherNum <= 90 or 97 <= cipherNum <= 122:
            cipherlist.append(chr(cipherNum))
        else:
            cipherlist.append(chr(cipherNum))
    ciphertext = "".join(cipherlist)
    return ciphertext

def main():
    win = GraphWin("Caesar Cipher Program", 400, 300)
    win.setCoords(0, 0, 4.0, 4.0)
    win.setBackground("black")
    plainIcon = Text(Point(1, 3), "Input Plaintext here:")
    plainIcon.setTextColor("green")
    plainIcon.draw(win)
    input1 = Entry(Point(3, 3), 20)
    input1.draw(win)
    keyIcon = Text(Point(1, 2.5), "Input Key here:")
    keyIcon.setTextColor("green")
    keyIcon.draw(win)
    input2 = Entry(Point(3, 2.5), 20)
    input2.draw(win)
    rect = Rectangle(Point(1.65, 2), Point(2.35, 1.5))
    rect.setFill("black")
    rect.setOutline("green")
    rect.draw(win)
    rectCenter = rect.getCenter()
    encodeIcon = Text(rectCenter, "Encode")
    encodeIcon.setTextColor("green")
    encodeIcon.draw(win)
    outputIcon = Text(Point(1, 1), "Ciphertext:")
    outputIcon.setTextColor("green")
    outputIcon.draw(win)
    win.getMouse()
    plaintext = input1.getText()
    key = eval(input2.getText())
    output = Text(Point(3, 1), encode(plaintext, key))
    output.setTextColor("green")
    output.draw(win)
    encodeIcon.undraw()
    restartIcon = Text(rectCenter, "Restart")
    restartIcon.setTextColor("green")
    restartIcon.draw(win)
    win.getMouse()
    win.close()
    main()
    
main()

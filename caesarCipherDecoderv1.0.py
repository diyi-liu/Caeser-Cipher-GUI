# Caesar Cipher Decoder v1.0
from graphics import *

def decode(ciphertext, key):
    plainlist = []
    length = len(ciphertext)
    for i in range(0, length, 1):
        if 65 <= (ord(ciphertext[i])-key) <= 90 or 97 <= (ord(ciphertext[i])-key) <= 122:
            plainlist.append(chr(ord(ciphertext[i]) - key))
        else:
            plainlist.append(chr(ord(ciphertext[i]) - key + 26))
    plaintext = "".join(plainlist)
    return plaintext

def caesarCipherDecoder():
    win = GraphWin("Caesar Cipher Decoder", 400, 300)
    win.setBackground("black")
    win.setCoords(0, 0, 4.0, 4.0)
    cipherIcon = Text(Point(1, 3), "Input Cipheretext here:")
    cipherIcon.setTextColor("green")
    cipherIcon.draw(win)
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
    decodeIcon = Text(rectCenter, "Decode")
    decodeIcon.setTextColor("green")
    decodeIcon.draw(win)
    plainIcon = Text(Point(1, 1), "Plaintext:")
    plainIcon.setTextColor("green")
    plainIcon.draw(win)
    win.getMouse()
    ciphertext = input1.getText()
    key = eval(input2.getText())
    output = Text(Point(3, 1), decode(ciphertext, key))
    output.setTextColor("green")
    output.draw(win)
    decodeIcon.undraw()
    restartIcon = Text(rectCenter, "Restart")
    restartIcon.setTextColor("green")
    restartIcon.draw(win)
    win.getMouse()
    win.close()
    caesarCipherDecoder()

caesarCipherDecoder()

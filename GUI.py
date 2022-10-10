from cgitb import text
from distutils import text_file
from glob import glob
import random
import time
from tkinter import *
from tkinter import ttk

from solver import Solver
from bfs import BFS

root = Tk()
root.geometry("1000x600+0+0")
root.title("8 Puzzle Game")
root.configure(background = 'beige')

Tops = Frame(root, bg = 'white', width = 900, height = 50)
Tops.grid(row = 0, column = 0)
    
lblTitle = Label(Tops, font = ('mathsans', 40, 'italic'), text = "8 Puzzle Game", bd = 0, bg = 'beige'
,fg = 'black', justify = CENTER)
lblTitle.grid(row = 0, column = 0)  

MainFrame = Frame(root, bg = 'beige', bd = 10, width = 1100, height = 700)
MainFrame.grid(row = 1, column = 0, padx = 40, pady = 40)

LeftFrame = Frame(MainFrame, bd = 0, width = 400, height = 300, padx = 1, pady = 2, bg = "beige")
LeftFrame.pack(side = LEFT)

RightFrame = Frame(MainFrame, bd = 0, width = 540, height = 500, padx = 1, pady = 4, bg = "beige")
RightFrame.pack(side = RIGHT)

RightFrame1 = Frame(RightFrame, bd = 0, width = 540, height = 100, padx = 30, pady = 4, bg = "beige")
RightFrame1.grid(row = 0, column = 0)

RightFrame2a = Frame(RightFrame, bd = 0, width = 540, height = 100, padx = 30, pady = 4, bg = "beige")
RightFrame2a.grid(row = 1, column = 0)

RightFrame2b = Frame(RightFrame, bd = 0, width = 540, height = 100, padx = 30, pady = 4, bg = "beige")
RightFrame2b.grid(row = 2, column = 0)

RightFrame2c = Frame(RightFrame, bd = 0, width = 540, height = 100, padx = 30, pady = 4, bg = "beige")
RightFrame2c.grid(row = 3, column = 0)

numberOfClicks = 0  
displayClicks = StringVar()
displayClicks.set("Number of Clicks" + "\n" + "0")

gameStatesString = StringVar()

def upDateCounter():
    global numberOfClicks, displayClicks

    displayClicks.set("Number of Clicks" + "\n" + str(numberOfClicks))

def gameStateUpdate(gameState):
    global gameStatesString
    gameStatesString.set(gameState)

class Button_:
    def __init__(self, text_, x, y):
        self.enterValue = text_
        self.textTaken = StringVar()
        self.textTaken.set(text_)
        self.x = x
        self.y = y
        self.btnNumber = Button(LeftFrame, textvariable = self.textTaken, bg = "khaki", font = ('arial', 40), bd = 3,
                command = lambda i = self.x, j = self.y : emptySpotChecker(i, j))
        self.btnNumber.place(x = self.x*100, y = self.y*100, width = 100, height = 100)

def shuffle():
    global btnNumbers, numberOfClicks
    nums = []
    for x in range (9):
        x += 1
        if x == 9:
            nums.append("")
        else:
            nums.append(str(x))
    for y in range(len (btnNumbers)):
        for x in range(len (btnNumbers[y])):
            num = random.choice(nums)
            btnNumbers[y][x].textTaken.set(num)
            nums.remove(num)
    numberOfClicks = 0
    upDateCounter()
    gameStateUpdate("")

lblDisplayClicks = Label(RightFrame1, textvariable = displayClicks, bg = "grey", font = ('arial', 20)).place(x = 0, y = 10, width = 480, height = 100)
btnShuffle = Button(RightFrame2a, text = "Shuffle", font = ('arial', 20), bg = "grey", command = shuffle).place(x = 0, y = 10, width = 480, height = 100)
btnSolve = Button(RightFrame2b, text = "Solve", font = ('arial', 20), bg = "grey", command = BFS).place(x = 0, y = 10, width = 480, height = 100)
lblDisplayClicks = Label(RightFrame2c, textvariable = gameStatesString, bg = "grey", font = ('arial', 40)).place(x = 0, y = 10, width = 480, height = 100)

btnNumbers = []

name = 0

for y in range(3):
    btnNumbers_ = []
    for x in range(3):
        name += 1
        if name == 9:
            name = ""
        
        btnNumbers_.append(Button_(str(name), x, y))
    btnNumbers.append(btnNumbers_)

shuffle()

#def solve():


def emptySpotChecker(y, x):
    global btnNumbers, numberOfClicks

    if not btnNumbers[x][y].textTaken.get() == "":
        for i in range(-1,2):
            newX = x + i

            if not(newX < 0 or len(btnNumbers) - 1 < newX or i == 0):
                if btnNumbers[newX][y].textTaken.get() == "":
                    text = btnNumbers[x][y].textTaken.get()
                    btnNumbers[x][y].textTaken.set(btnNumbers[newX][y].textTaken.get())
                    btnNumbers[newX][y].textTaken.set(text)
                    winCheck()
                    break
        for j in range(-1,2):
            newY = y + j

            if not(newY < 0 or len(btnNumbers[0]) - 1 < newY or j == 0):
                if btnNumbers[x][newY].textTaken.get() == "":
                    text = btnNumbers[x][y].textTaken.get()
                    btnNumbers[x][y].textTaken.set(btnNumbers[x][newY].textTaken.get())
                    btnNumbers[x][newY].textTaken.set(text)
                    winCheck()
                    break
        numberOfClicks += 1
        upDateCounter()

def winCheck():
    lost = False
    for y in range(len(btnNumbers)):
        for x in range(len(btnNumbers[y])):
            if btnNumbers[y][x].enterValue != btnNumbers[y][x].textTaken.get():
                lost = True
                break
            if not lost:
                gameStateUpdate("You are a winner!")    


root.mainloop()

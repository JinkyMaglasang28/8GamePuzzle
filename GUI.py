import random
import time
from tkinter import *
from tkinter import ttk

root = Tk()
root.geometry("1350x700+0+0")
root.title("8 Puzzle Game")
root.configure(background = 'white')



Tops = Frame(root, bg = 'black', pady = 2, width = 1350, height = 100, relief = RIDGE)
Tops.grid(row = 0, column = 0)

lblTitle = Label(Tops, font = ('arial', 80, 'bold'), text = "Advanced Puzzle Game", bd = 10, bg = 'black'
,fg = 'Cornsilk', justify = CENTER)
lblTitle.grid(row = 0, column = 0)

MainFrame = Frame(root, bg = 'pink', bd = 10, width = 1350, height = 600, relief = RIDGE)
MainFrame.grid(row = 1, column = 0, padx = 30)

LeftFrame = Frame(MainFrame, bd = 10, width = 700, height = 500, pady = 2, bg = 'pink', relief = RIDGE)
LeftFrame.pack(side = LEFT)

RightFrame = Frame(MainFrame, bd = 10, width = 540, height = 500, padx = 1, pady = 2, bg = "pink", relief = RIDGE)
RightFrame.pack(side = RIGHT)

RightFrame1 = Frame(RightFrame, bd = 10, width = 540, height = 200, padx = 10, pady = 2, bg = "pink", relief = RIDGE)
RightFrame1.grid(row = 0, column = 0)

RightFrame2a = Frame(RightFrame, bd = 10, width = 540, height = 140, padx = 10, pady = 2, bg = "pink", relief = RIDGE)
RightFrame2a.grid(row = 1, column = 0)

RightFrame2b = Frame(RightFrame, bd = 10, width = 540, height = 140, padx = 10, pady = 2, bg = "pink", relief = RIDGE)
RightFrame2b.grid(row = 2, column = 0)

numberOfClicks = 0
displayClicks = StringVar()
displayClicks.set("Number of Clicks" + "/n" + str(numberOfClicks)

gameStatesString = StringVar()

def upDateCounter():
    


root.mainloop()

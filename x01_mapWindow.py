#! python3
import tkinter as tk
from tkinter import *
from x07_windowTime import *
import pyautogui as m

#window = Tk()
window.attributes('-topmost',True)
window.title('Board')
occupied = [[[1, 1], [2, 1]], [[4, 0], [5, 0], [6, 0]], [[0, 1], [0, 2], [0, 3]], [[1, 8], [2, 8], [3, 8], [4, 8]], [[4, 3], [4, 4], [4, 5], [4, 6], [4, 7]]]

boatshow =  PhotoImage(file='boat.png')

l1 = Label(window, text='01')
l2 = Label(window, text='02')
l3 = Label(window, text='03')
l4 = Label(window, text='04')
l5 = Label(window, text='05')
l6 = Label(window, text='06')
l7 = Label(window, text='07')
l8 = Label(window, text='08')
l9 = Label(window, text='09')
l10 = Label(window, text='10')
l11 = Label(window, text='A ')
l12 = Label(window, text='B ')
l13 = Label(window, text='C ')
l14 = Label(window, text='D ')
l15 = Label(window, text='E ')
l16 = Label(window, text='F ')
l17 = Label(window, text='G ')
l18 = Label(window, text='H ')
l19 = Label(window, text='I ')
l20 = Label(window, text='J ')
b1 = Button(window)
b2 = Button(window)
boat11 = Label(window, image=boatshow)
boat12 = Label(window, image=boatshow)
boat21 = Label(window, image=boatshow)
boat22 = Label(window, image=boatshow)
boat23 = Label(window, image=boatshow)
boat31 = Label(window, image=boatshow)
boat32 = Label(window, image=boatshow)
boat33 = Label(window, image=boatshow)
boat41 = Label(window, image=boatshow)
boat42 = Label(window, image=boatshow)
boat43 = Label(window, image=boatshow)
boat44 = Label(window, image=boatshow)
boat51 = Label(window, image=boatshow)
boat52 = Label(window, image=boatshow)
boat53 = Label(window, image=boatshow)
boat54 = Label(window, image=boatshow)
boat55 = Label(window, image=boatshow)
boatlables = (boat11, boat12, boat21, boat22, boat23, boat31, boat32, boat33, boat41, boat42, boat43, boat44, boat51, boat52, boat53, boat54, boat55)

l1.grid(row=1, column=1, padx=2)
l2.grid(row=2, column=1, padx=2)
l3.grid(row=3, column=1, padx=2)
l4.grid(row=4, column=1, padx=2)
l5.grid(row=5, column=1, padx=2)
l6.grid(row=6, column=1, padx=2)
l7.grid(row=7, column=1, padx=2)
l8.grid(row=8, column=1, padx=2)
l9.grid(row=9, column=1, padx=2)
l10.grid(row=10, column=1, padx=2)
l11.grid(row=11, column=2, padx=3)
l12.grid(row=11, column=3, padx=3)
l13.grid(row=11, column=4, padx=3)
l14.grid(row=11, column=5, padx=3)
l15.grid(row=11, column=6, padx=3)
l16.grid(row=11, column=7, padx=3)
l17.grid(row=11, column=8, padx=3)
l18.grid(row=11, column=9, padx=3)
l19.grid(row=11, column=10, padx=3)
l20.grid(row=11, column=11, padx=3)

def go(event):
    showBoard(boatB1)
b1.bind("<Button>", go)
b1.grid(row=12, column=1)

def die(event):
    #setup()
    gameLoop()
b2.bind("<Button>", die)
b2.grid(row=12, column=2)

def cord(event):
    print(event)
    looko = m.position()
    hg = round(((looko.x - window.winfo_x())-20)/22)
    yg = round((looko.y - window.winfo_y())/21)-1
    if 0 < hg < 11:
        if 0 < yg < 11:
            print(hg,yg)
window.bind("<Button-1>",cord)

'''def click():
    print(window.winfo_x(), window.winfo_y())
h = Button(command=click)
h.grid(row=12, column=3)'''

def showBoard(oc=[]):
    r = 0
    print(oc)
    for i in oc:
        for I in i:
            boatlables[r].place(x=(I[0]*22+20), y=(189-I[1]*21))
            r = r + 1

if __name__ == "__main__":
    window.mainloop()
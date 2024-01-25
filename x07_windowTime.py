#!python3

import random#, x03_create, x04_checkConflicts
import tkinter as tk
from tkinter import *

def g():
    global boatDatat
    global cboat
    global ccord
    global recentcord
    global boatB1
    global hitB1
    global missB1
    global sink1
    global boatB2
    global hitB2
    global missB2
    global sink2
    boatDatat = (('tugboat',2),('sumbarine',3),('destroyer',3),('battelship',4),('carrier',5))
    cboat = 0
    ccord = None
    recentcord = None
    boatB1 = []
    hitB1 = []
    missB1 = []
    sink1 = 0
    boatB2 = []
    hitB2 = []
    missB2 = []
    sink2 = 0

    def offBoard(cheek):
        global boatDatat
        global cboat
        global ccord
        global recentcord
        global boatB1
        global hitB1
        global missB1
        global sink1
        global boatB2
        global hitB2
        global missB2
        global sink2
        for i in cheek:
            if i[0] < 0:
                return False
            elif i[0] > 9:
                return False
            elif i[1] < 0:
                return False
            elif i[1] > 9:
                return False
        else:
            return True


    def winning():
        global boatDatat
        global cboat
        global ccord
        global recentcord
        global boatB1
        global hitB1
        global missB1
        global sink1
        global boatB2
        global hitB2
        global missB2
        global sink2
        if sink2 == 5:
            #print('win player 1')
            window.destroy()
            winboard = tk.Tk()
            winboard.attributes('-topmost',True)
            winboard.title('WIN')
            labb = Label(winboard, text='You Win!', font=('Comic Sans MS', 160))
            labb.grid(row=1, column=1)
            ab = Button(winboard, text='Play agen?', font=('Comic Sans MS', 30), border=15)
            ab.grid(row=2, column=1)
            def vhuyj(l):
                winboard.destroy()
                g()
            ab.bind('<Button>', vhuyj)
            winboard.mainloop()
        if sink1 == 5:
            #print('win player 2')
            window.destroy()
            winboard = tk.Tk()
            winboard.attributes('-topmost',True)
            winboard.title('WIN')
            labb = Label(winboard, text='Oponet Wins!', font=('Comic Sans MS', 160))
            labb.grid(row=1, column=1)
            ab = Button(winboard, text='Play agen?', font=('Comic Sans MS', 30), border=15)
            ab.grid(row=2, column=1)
            def vhuyj(l):
                winboard.destroy()
                g()
            ab.bind('<Button>', vhuyj)
            winboard.mainloop()

    def fullList(ships,ocupied):
        global boatDatat
        global cboat
        global ccord
        global recentcord
        global boatB1
        global hitB1
        global missB1
        global sink1
        global boatB2
        global hitB2
        global missB2
        global sink2
        boat = ships[2]
        boatsquare = [ships[0]]
        #print(boatsquare)
        if ships[1] <= 1:
            for i in range(boatDatat[boat][1] - 1):
                #print(boatsquare)
                c = [boatsquare[-1][0],boatsquare[-1][1] + 1]
                boatsquare.append(c)
        elif ships[1] <= 2:
            for i in range(boatDatat[boat][1] - 1):
                #print(boatsquare)
                c = [boatsquare[-1][0],boatsquare[-1][1] - 1]
                boatsquare.append(c)
        elif ships[1] <= 3:
            for i in range(boatDatat[boat][1] - 1):
                #print(boatsquare)
                c = [boatsquare[-1][0] - 1,boatsquare[-1][1]]
                boatsquare.append(c)
        elif ships[1] <= 4:
            for i in range(boatDatat[boat][1] - 1):
                #print(boatsquare)
                c = [boatsquare[-1][0] + 1,boatsquare[-1][1]]
                boatsquare.append(c)
        else:
            xy = [random.randrange(10), random.randrange(10)]
            boatsquare = fullList([xy,ships[1],boat],ocupied)
        failed = False
        for i in ocupied:
            for I in i:
                if I in boatsquare:
                    failed = True
        for i in boatsquare:
            for I in i:
                if I < 0 or I > 9:
                    failed = True
        if failed:
            xy = [random.randrange(10), random.randrange(10)]
            boatsquare = fullList([xy,ships[1],boat],ocupied)
        return boatsquare

    def run(bord):
        global boatDatat
        global cboat
        global ccord
        global recentcord
        global boatB1
        global hitB1
        global missB1
        global sink1
        global boatB2
        global hitB2
        global missB2
        global sink2
        boatsquare = []
        if cboat < 5 and ccord == None and bord == 1:
            #print(ccord, recentcord)
            ccord = recentcord
        elif cboat < 5 and ccord != None and recentcord != ccord and bord == 1:
            #print(ccord, recentcord)
            for i in range(10):
                if recentcord == [ccord[0]+i,ccord[1]]:
                    #print('U')
                    for i in range(boatDatat[cboat][1]):
                        c = [ccord[0]+i,ccord[1]]
                        boatsquare.append(c)
                elif recentcord == [ccord[0],ccord[1]+i]:
                    #print('R')
                    for i in range(boatDatat[cboat][1]):
                        c = [ccord[0],ccord[1]+i]
                        boatsquare.append(c)
                elif recentcord == [ccord[0]-i,ccord[1]]:
                    #print('D')
                    for i in range(boatDatat[cboat][1]):
                        c = [ccord[0]-i,ccord[1]]
                        boatsquare.append(c)
                elif recentcord == [ccord[0],ccord[1]-i]:
                    #print('L')
                    for i in range(boatDatat[cboat][1]):
                        c = [ccord[0],ccord[1]-i]
                        boatsquare.append(c)
            #print(boatsquare)
            if boatHere(boatsquare) and boatsquare != [] and offBoard(boatsquare):
                boatB1.append(boatsquare)
                cboat = cboat + 1
            ccord = None
        elif cboat > 5 and bord == 2:
            #after creat square hit enamy bord
            for i in boatB2:
                if recentcord in i and recentcord not in hitB2:
                    i.remove(recentcord)
                    hitB2.append(recentcord)
                    for i in range(len(hitB1)):
                        k = len(hitB1) - i - 1
                        #print(k)
                        if hitB1 != []:
                            #print(hitB1)
                            aicord = [hitB1[k][0]+1,hitB1[k][1]]
                            #print(aicord)
                            if aicord in hitB1 or aicord in missB1 or aicord[0] < 0 or aicord[0] > 9 or aicord[1] < 0 or aicord[1] > 9:
                                aicord = [hitB1[k][0]-1,hitB1[k][1]]
                                #print(aicord)
                                if aicord in hitB1 or aicord in missB1 or aicord[0] < 0 or aicord[0] > 9 or aicord[1] < 0 or aicord[1] > 9:
                                    aicord = [hitB1[k][0],hitB1[k][1]+1]
                                    #print(aicord)
                                    if aicord in hitB1 or aicord in missB1 or aicord[0] < 0 or aicord[0] > 9 or aicord[1] < 0 or aicord[1] > 9:
                                        aicord = [hitB1[k][0],hitB1[k][1]-1]
                                        #print(aicord)
                        else:
                            while aicord in missB1 or aicord in hitB1 or aicord[0] < 0 or aicord[0] > 9 or aicord[1] < 0 or aicord[1] > 9:
                                #print(777)
                                aicord = [random.randrange(10), random.randrange(10)]
                        if aicord not in missB1 and aicord not in hitB1 and type(aicord) == list and -1 < aicord[0] < 10 and -1 < aicord[1] < 10:
                            #print(aicord)
                            break
                    else:
                        #print(888)
                        aicord = [random.randrange(10), random.randrange(10)]
                        while aicord in missB1 or aicord in hitB1 or aicord[0] < 0 or aicord[0] > 9 or aicord[1] < 0 or aicord[1] > 9:
                            aicord = [random.randrange(10), random.randrange(10)]
                    #print(aicord)
                    for i in boatB1:
                        if aicord in i:
                            i.remove(aicord)
                            hitB1.append(aicord)
                            break
                    else:
                        missB1.append(aicord)
                    for i in boatB1:
                        if i == []:
                            boatB1.remove([])
                            sink1 = sink1 + 1
                    for i in boatB2:
                        if i == []:
                            boatB2.remove([])
                            sink2 = sink2 + 1 
                    break
            else:
                if recentcord not in hitB2 and recentcord not in missB2:
                    missB2.append(recentcord)
                    #print(666)
                    for i in range(len(hitB1)):
                        k = len(hitB1) - i - 1
                        #print(k)
                        if hitB1 != []:
                            #print(hitB1)
                            aicord = [hitB1[k][0]+1,hitB1[k][1]]
                            #print(aicord)
                            if aicord in hitB1 or aicord in missB1 or aicord[0] < 0 or aicord[0] > 9 or aicord[1] < 0 or aicord[1] > 9:
                                aicord = [hitB1[k][0]-1,hitB1[k][1]]
                                #print(aicord)
                                if aicord in hitB1 or aicord in missB1 or aicord[0] < 0 or aicord[0] > 9 or aicord[1] < 0 or aicord[1] > 9:
                                    aicord = [hitB1[k][0],hitB1[k][1]+1]
                                    #print(aicord)
                                    if aicord in hitB1 or aicord in missB1 or aicord[0] < 0 or aicord[0] > 9 or aicord[1] < 0 or aicord[1] > 9:
                                        aicord = [hitB1[k][0],hitB1[k][1]-1]
                                        #print(aicord)
                        else:
                            while aicord in missB1 or aicord in hitB1 or aicord[0] < 0 or aicord[0] > 9 or aicord[1] < 0 or aicord[1] > 9:
                                #print(777)
                                aicord = [random.randrange(10), random.randrange(10)]
                        if aicord not in missB1 and aicord not in hitB1 and type(aicord) == list and -1 < aicord[0] < 10 and -1 < aicord[1] < 10:
                            #print(aicord)
                            break
                    else:
                        #print(888)
                        aicord = [random.randrange(10), random.randrange(10)]
                        while aicord in missB1 or aicord in hitB1 or aicord[0] < 0 or aicord[0] > 9 or aicord[1] < 0 or aicord[1] > 9:
                            aicord = [random.randrange(10), random.randrange(10)]
                    #print(aicord)
                    for i in boatB1:
                        #print(aicord)
                        if aicord in i:
                            i.remove(aicord)
                            hitB1.append(aicord)
                            break
                    else:
                        missB1.append(aicord)
                    for i in boatB1:
                        if i == []:
                            boatB1.remove([])
                            sink1 = sink1 + 1
                    for i in boatB2:
                        if i == []:
                            boatB2.remove([])
                            sink2 = sink2 + 1 
        elif cboat > 5 and bord == 1:
            #after creat square hit player bord
            #print(recentcord)
            for i in boatB1:
                if i == []:
                    boatB1.remove([])
                    sink1 = sink1 + 1
            for i in boatB2:
                if i == []:
                    boatB2.remove([])
                    sink2 = sink2 + 1        
        if cboat == 5:
            for i in range(5):
                xy = [random.randrange(10), random.randrange(10)]
                direc = random.randrange(5)
                newboat = [xy,direc,i]

                boatB2.append(fullList(newboat,boatB2))
            cboat = cboat + 1
        #print(boatB1, boatB2, sink1, sink2)
        updateBoard()
        if sink1 == 5:
            winning()
        if sink2 == 5:
            winning()

    window = tk.Tk()
    #print("die")
    window.attributes('-topmost',True)
    window.title('Board')

    bordlable1 = Label(window, text='Your Bord', font=('Comic sans MS', 10))
    bordlable1.grid(row=1,column=5, columnspan=4)
    bordlable2 = Label(window, text='Oponet Bord', font=('Comic sans MS', 10))
    bordlable2.grid(row=1,column=16, columnspan=4)

    instructions = StringVar(window)
    instructions.set("Place boat")
    instructionshow = Label(window, textvariable=instructions)
    instructionshow.grid(row=13, column=1, columnspan=22)

    #---------- Deju Vu land 3205 lines -----------------#
    l1 = Label(window, text='10')
    l2 = Label(window, text='09')
    l3 = Label(window, text='08')
    l4 = Label(window, text='07')
    l5 = Label(window, text='06')
    l6 = Label(window, text='05')
    l7 = Label(window, text='04')
    l8 = Label(window, text='03')
    l9 = Label(window, text='02')
    l10 = Label(window, text='01')
    l11 = Label(window, text=' A ')
    l12 = Label(window, text=' B ')
    l13 = Label(window, text=' C ')
    l14 = Label(window, text=' D ')
    l15 = Label(window, text=' E ')
    l16 = Label(window, text=' F ')
    l17 = Label(window, text=' G ')
    l18 = Label(window, text=' H ')
    l19 = Label(window, text=' I ')
    l20 = Label(window, text=' J ')

    ll1 = Label(window, text='10')
    ll2 = Label(window, text='09')
    ll3 = Label(window, text='08')
    ll4 = Label(window, text='07')
    ll5 = Label(window, text='06')
    ll6 = Label(window, text='05')
    ll7 = Label(window, text='04')
    ll8 = Label(window, text='03')
    ll9 = Label(window, text='02')
    ll10 = Label(window, text='01')
    ll11 = Label(window, text=' A ')
    ll12 = Label(window, text=' B ')
    ll13 = Label(window, text=' C ')
    ll14 = Label(window, text=' D ')
    ll15 = Label(window, text=' E ')
    ll16 = Label(window, text=' F ')
    ll17 = Label(window, text=' G ')
    ll18 = Label(window, text=' H ')
    ll19 = Label(window, text=' I ')
    ll20 = Label(window, text=' J ')
    
    l1.grid(row=2, column=1, padx=2)
    l2.grid(row=3, column=1, padx=2)
    l3.grid(row=4, column=1, padx=2)
    l4.grid(row=5, column=1, padx=2)
    l5.grid(row=6, column=1, padx=2)
    l6.grid(row=7, column=1, padx=2)
    l7.grid(row=8, column=1, padx=2)
    l8.grid(row=9, column=1, padx=2)
    l9.grid(row=10, column=1, padx=2)
    l10.grid(row=11, column=1, padx=2)
    l11.grid(row=12, column=2, padx=3)
    l12.grid(row=12, column=3, padx=3)
    l13.grid(row=12, column=4, padx=3)
    l14.grid(row=12, column=5, padx=3)
    l15.grid(row=12, column=6, padx=3)
    l16.grid(row=12, column=7, padx=3)
    l17.grid(row=12, column=8, padx=3)
    l18.grid(row=12, column=9, padx=3)
    l19.grid(row=12, column=10, padx=3)
    l20.grid(row=12, column=11, padx=3)
    
    ll1.grid(row=2, column=12, padx=2)
    ll2.grid(row=3, column=12, padx=2)
    ll3.grid(row=4, column=12, padx=2)
    ll4.grid(row=5, column=12, padx=2)
    ll5.grid(row=6, column=12, padx=2)
    ll6.grid(row=7, column=12, padx=2)
    ll7.grid(row=8, column=12, padx=2)
    ll8.grid(row=9, column=12, padx=2)
    ll9.grid(row=10, column=12, padx=2)
    ll10.grid(row=11, column=12, padx=2)
    ll11.grid(row=12, column=13, padx=3)
    ll12.grid(row=12, column=14, padx=3)
    ll13.grid(row=12, column=15, padx=3)
    ll14.grid(row=12, column=16, padx=3)
    ll15.grid(row=12, column=17, padx=3)
    ll16.grid(row=12, column=18, padx=3)
    ll17.grid(row=12, column=19, padx=3)
    ll18.grid(row=12, column=20, padx=3)
    ll19.grid(row=12, column=21, padx=3)
    ll20.grid(row=12, column=22, padx=3)

    boatshow11 = StringVar(window)
    boatshow11.set('   ')
    boat11 = Button(window, textvariable=boatshow11)
    boat11.grid(row=11, column=2, padx=3)
    boatshow12 = StringVar(window)
    boatshow12.set('   ')
    boat12 = Button(window, textvariable=boatshow12)
    boat12.grid(row=11, column=3, padx=3)
    boatshow13 = StringVar(window)
    boatshow13.set('   ')
    boat13 = Button(window, textvariable=boatshow13)
    boat13.grid(row=11, column=4, padx=3)
    boatshow14 = StringVar(window)
    boatshow14.set('   ')
    boat14 = Button(window, textvariable=boatshow14)
    boat14.grid(row=11, column=5, padx=3)
    boatshow15 = StringVar(window)
    boatshow15.set('   ')
    boat15 = Button(window, textvariable=boatshow15)
    boat15.grid(row=11, column=6, padx=3)
    boatshow16 = StringVar(window)
    boatshow16.set('   ')
    boat16 = Button(window, textvariable=boatshow16)
    boat16.grid(row=11, column=7, padx=3)
    boatshow17 = StringVar(window)
    boatshow17.set('   ')
    boat17 = Button(window, textvariable=boatshow17)
    boat17.grid(row=11, column=8, padx=3)
    boatshow18 = StringVar(window)
    boatshow18.set('   ')
    boat18 = Button(window, textvariable=boatshow18)
    boat18.grid(row=11, column=9, padx=3)
    boatshow19 = StringVar(window)
    boatshow19.set('   ')
    boat19 = Button(window, textvariable=boatshow19)
    boat19.grid(row=11, column=10, padx=3)
    boatshow110 = StringVar(window)
    boatshow110.set('   ')
    boat110 = Button(window, textvariable=boatshow110)
    boat110.grid(row=11, column=11, padx=3)
    boatshow21 = StringVar(window)
    boatshow21.set('   ')
    boat21 = Button(window, textvariable=boatshow21)
    boat21.grid(row=10, column=2, padx=3)
    boatshow22 = StringVar(window)
    boatshow22.set('   ')
    boat22 = Button(window, textvariable=boatshow22)
    boat22.grid(row=10, column=3, padx=3)
    boatshow23 = StringVar(window)
    boatshow23.set('   ')
    boat23 = Button(window, textvariable=boatshow23)
    boat23.grid(row=10, column=4, padx=3)
    boatshow24 = StringVar(window)
    boatshow24.set('   ')
    boat24 = Button(window, textvariable=boatshow24)
    boat24.grid(row=10, column=5, padx=3)
    boatshow25 = StringVar(window)
    boatshow25.set('   ')
    boat25 = Button(window, textvariable=boatshow25)
    boat25.grid(row=10, column=6, padx=3)
    boatshow26 = StringVar(window)
    boatshow26.set('   ')
    boat26 = Button(window, textvariable=boatshow26)
    boat26.grid(row=10, column=7, padx=3)
    boatshow27 = StringVar(window)
    boatshow27.set('   ')
    boat27 = Button(window, textvariable=boatshow27)
    boat27.grid(row=10, column=8, padx=3)
    boatshow28 = StringVar(window)
    boatshow28.set('   ')
    boat28 = Button(window, textvariable=boatshow28)
    boat28.grid(row=10, column=9, padx=3)
    boatshow29 = StringVar(window)
    boatshow29.set('   ')
    boat29 = Button(window, textvariable=boatshow29)
    boat29.grid(row=10, column=10, padx=3)
    boatshow210 = StringVar(window)
    boatshow210.set('   ')
    boat210 = Button(window, textvariable=boatshow210)
    boat210.grid(row=10, column=11, padx=3)
    boatshow31 = StringVar(window)
    boatshow31.set('   ')
    boat31 = Button(window, textvariable=boatshow31)
    boat31.grid(row=9, column=2, padx=3)
    boatshow32 = StringVar(window)
    boatshow32.set('   ')
    boat32 = Button(window, textvariable=boatshow32)
    boat32.grid(row=9, column=3, padx=3)
    boatshow33 = StringVar(window)
    boatshow33.set('   ')
    boat33 = Button(window, textvariable=boatshow33)
    boat33.grid(row=9, column=4, padx=3)
    boatshow34 = StringVar(window)
    boatshow34.set('   ')
    boat34 = Button(window, textvariable=boatshow34)
    boat34.grid(row=9, column=5, padx=3)
    boatshow35 = StringVar(window)
    boatshow35.set('   ')
    boat35 = Button(window, textvariable=boatshow35)
    boat35.grid(row=9, column=6, padx=3)
    boatshow36 = StringVar(window)
    boatshow36.set('   ')
    boat36 = Button(window, textvariable=boatshow36)
    boat36.grid(row=9, column=7, padx=3)
    boatshow37 = StringVar(window)
    boatshow37.set('   ')
    boat37 = Button(window, textvariable=boatshow37)
    boat37.grid(row=9, column=8, padx=3)
    boatshow38 = StringVar(window)
    boatshow38.set('   ')
    boat38 = Button(window, textvariable=boatshow38)
    boat38.grid(row=9, column=9, padx=3)
    boatshow39 = StringVar(window)
    boatshow39.set('   ')
    boat39 = Button(window, textvariable=boatshow39)
    boat39.grid(row=9, column=10, padx=3)
    boatshow310 = StringVar(window)
    boatshow310.set('   ')
    boat310 = Button(window, textvariable=boatshow310)
    boat310.grid(row=9, column=11, padx=3)
    boatshow41 = StringVar(window)
    boatshow41.set('   ')
    boat41 = Button(window, textvariable=boatshow41)
    boat41.grid(row=8, column=2, padx=3)
    boatshow42 = StringVar(window)
    boatshow42.set('   ')
    boat42 = Button(window, textvariable=boatshow42)
    boat42.grid(row=8, column=3, padx=3)
    boatshow43 = StringVar(window)
    boatshow43.set('   ')
    boat43 = Button(window, textvariable=boatshow43)
    boat43.grid(row=8, column=4, padx=3)
    boatshow44 = StringVar(window)
    boatshow44.set('   ')
    boat44 = Button(window, textvariable=boatshow44)
    boat44.grid(row=8, column=5, padx=3)
    boatshow45 = StringVar(window)
    boatshow45.set('   ')
    boat45 = Button(window, textvariable=boatshow45)
    boat45.grid(row=8, column=6, padx=3)
    boatshow46 = StringVar(window)
    boatshow46.set('   ')
    boat46 = Button(window, textvariable=boatshow46)
    boat46.grid(row=8, column=7, padx=3)
    boatshow47 = StringVar(window)
    boatshow47.set('   ')
    boat47 = Button(window, textvariable=boatshow47)
    boat47.grid(row=8, column=8, padx=3)
    boatshow48 = StringVar(window)
    boatshow48.set('   ')
    boat48 = Button(window, textvariable=boatshow48)
    boat48.grid(row=8, column=9, padx=3)
    boatshow49 = StringVar(window)
    boatshow49.set('   ')
    boat49 = Button(window, textvariable=boatshow49)
    boat49.grid(row=8, column=10, padx=3)
    boatshow410 = StringVar(window)
    boatshow410.set('   ')
    boat410 = Button(window, textvariable=boatshow410)
    boat410.grid(row=8, column=11, padx=3)
    boatshow51 = StringVar(window)
    boatshow51.set('   ')
    boat51 = Button(window, textvariable=boatshow51)
    boat51.grid(row=7, column=2, padx=3)
    boatshow52 = StringVar(window)
    boatshow52.set('   ')
    boat52 = Button(window, textvariable=boatshow52)
    boat52.grid(row=7, column=3, padx=3)
    boatshow53 = StringVar(window)
    boatshow53.set('   ')
    boat53 = Button(window, textvariable=boatshow53)
    boat53.grid(row=7, column=4, padx=3)
    boatshow54 = StringVar(window)
    boatshow54.set('   ')
    boat54 = Button(window, textvariable=boatshow54)
    boat54.grid(row=7, column=5, padx=3)
    boatshow55 = StringVar(window)
    boatshow55.set('   ')
    boat55 = Button(window, textvariable=boatshow55)
    boat55.grid(row=7, column=6, padx=3)
    boatshow56 = StringVar(window)
    boatshow56.set('   ')
    boat56 = Button(window, textvariable=boatshow56)
    boat56.grid(row=7, column=7, padx=3)
    boatshow57 = StringVar(window)
    boatshow57.set('   ')
    boat57 = Button(window, textvariable=boatshow57)
    boat57.grid(row=7, column=8, padx=3)
    boatshow58 = StringVar(window)
    boatshow58.set('   ')
    boat58 = Button(window, textvariable=boatshow58)
    boat58.grid(row=7, column=9, padx=3)
    boatshow59 = StringVar(window)
    boatshow59.set('   ')
    boat59 = Button(window, textvariable=boatshow59)
    boat59.grid(row=7, column=10, padx=3)
    boatshow510 = StringVar(window)
    boatshow510.set('   ')
    boat510 = Button(window, textvariable=boatshow510)
    boat510.grid(row=7, column=11, padx=3)
    boatshow61 = StringVar(window)
    boatshow61.set('   ')
    boat61 = Button(window, textvariable=boatshow61)
    boat61.grid(row=6, column=2, padx=3)
    boatshow62 = StringVar(window)
    boatshow62.set('   ')
    boat62 = Button(window, textvariable=boatshow62)
    boat62.grid(row=6, column=3, padx=3)
    boatshow63 = StringVar(window)
    boatshow63.set('   ')
    boat63 = Button(window, textvariable=boatshow63)
    boat63.grid(row=6, column=4, padx=3)
    boatshow64 = StringVar(window)
    boatshow64.set('   ')
    boat64 = Button(window, textvariable=boatshow64)
    boat64.grid(row=6, column=5, padx=3)
    boatshow65 = StringVar(window)
    boatshow65.set('   ')
    boat65 = Button(window, textvariable=boatshow65)
    boat65.grid(row=6, column=6, padx=3)
    boatshow66 = StringVar(window)
    boatshow66.set('   ')
    boat66 = Button(window, textvariable=boatshow66)
    boat66.grid(row=6, column=7, padx=3)
    boatshow67 = StringVar(window)
    boatshow67.set('   ')
    boat67 = Button(window, textvariable=boatshow67)
    boat67.grid(row=6, column=8, padx=3)
    boatshow68 = StringVar(window)
    boatshow68.set('   ')
    boat68 = Button(window, textvariable=boatshow68)
    boat68.grid(row=6, column=9, padx=3)
    boatshow69 = StringVar(window)
    boatshow69.set('   ')
    boat69 = Button(window, textvariable=boatshow69)
    boat69.grid(row=6, column=10, padx=3)
    boatshow610 = StringVar(window)
    boatshow610.set('   ')
    boat610 = Button(window, textvariable=boatshow610)
    boat610.grid(row=6, column=11, padx=3)
    boatshow71 = StringVar(window)
    boatshow71.set('   ')
    boat71 = Button(window, textvariable=boatshow71)
    boat71.grid(row=5, column=2, padx=3)
    boatshow72 = StringVar(window)
    boatshow72.set('   ')
    boat72 = Button(window, textvariable=boatshow72)
    boat72.grid(row=5, column=3, padx=3)
    boatshow73 = StringVar(window)
    boatshow73.set('   ')
    boat73 = Button(window, textvariable=boatshow73)
    boat73.grid(row=5, column=4, padx=3)
    boatshow74 = StringVar(window)
    boatshow74.set('   ')
    boat74 = Button(window, textvariable=boatshow74)
    boat74.grid(row=5, column=5, padx=3)
    boatshow75 = StringVar(window)
    boatshow75.set('   ')
    boat75 = Button(window, textvariable=boatshow75)
    boat75.grid(row=5, column=6, padx=3)
    boatshow76 = StringVar(window)
    boatshow76.set('   ')
    boat76 = Button(window, textvariable=boatshow76)
    boat76.grid(row=5, column=7, padx=3)
    boatshow77 = StringVar(window)
    boatshow77.set('   ')
    boat77 = Button(window, textvariable=boatshow77)
    boat77.grid(row=5, column=8, padx=3)
    boatshow78 = StringVar(window)
    boatshow78.set('   ')
    boat78 = Button(window, textvariable=boatshow78)
    boat78.grid(row=5, column=9, padx=3)
    boatshow79 = StringVar(window)
    boatshow79.set('   ')
    boat79 = Button(window, textvariable=boatshow79)
    boat79.grid(row=5, column=10, padx=3)
    boatshow710 = StringVar(window)
    boatshow710.set('   ')
    boat710 = Button(window, textvariable=boatshow710)
    boat710.grid(row=5, column=11, padx=3)
    boatshow81 = StringVar(window)
    boatshow81.set('   ')
    boat81 = Button(window, textvariable=boatshow81)
    boat81.grid(row=4, column=2, padx=3)
    boatshow82 = StringVar(window)
    boatshow82.set('   ')
    boat82 = Button(window, textvariable=boatshow82)
    boat82.grid(row=4, column=3, padx=3)
    boatshow83 = StringVar(window)
    boatshow83.set('   ')
    boat83 = Button(window, textvariable=boatshow83)
    boat83.grid(row=4, column=4, padx=3)
    boatshow84 = StringVar(window)
    boatshow84.set('   ')
    boat84 = Button(window, textvariable=boatshow84)
    boat84.grid(row=4, column=5, padx=3)
    boatshow85 = StringVar(window)
    boatshow85.set('   ')
    boat85 = Button(window, textvariable=boatshow85)
    boat85.grid(row=4, column=6, padx=3)
    boatshow86 = StringVar(window)
    boatshow86.set('   ')
    boat86 = Button(window, textvariable=boatshow86)
    boat86.grid(row=4, column=7, padx=3)
    boatshow87 = StringVar(window)
    boatshow87.set('   ')
    boat87 = Button(window, textvariable=boatshow87)
    boat87.grid(row=4, column=8, padx=3)
    boatshow88 = StringVar(window)
    boatshow88.set('   ')
    boat88 = Button(window, textvariable=boatshow88)
    boat88.grid(row=4, column=9, padx=3)
    boatshow89 = StringVar(window)
    boatshow89.set('   ')
    boat89 = Button(window, textvariable=boatshow89)
    boat89.grid(row=4, column=10, padx=3)
    boatshow810 = StringVar(window)
    boatshow810.set('   ')
    boat810 = Button(window, textvariable=boatshow810)
    boat810.grid(row=4, column=11, padx=3)
    boatshow91 = StringVar(window)
    boatshow91.set('   ')
    boat91 = Button(window, textvariable=boatshow91)
    boat91.grid(row=3, column=2, padx=3)
    boatshow92 = StringVar(window)
    boatshow92.set('   ')
    boat92 = Button(window, textvariable=boatshow92)
    boat92.grid(row=3, column=3, padx=3)
    boatshow93 = StringVar(window)
    boatshow93.set('   ')
    boat93 = Button(window, textvariable=boatshow93)
    boat93.grid(row=3, column=4, padx=3)
    boatshow94 = StringVar(window)
    boatshow94.set('   ')
    boat94 = Button(window, textvariable=boatshow94)
    boat94.grid(row=3, column=5, padx=3)
    boatshow95 = StringVar(window)
    boatshow95.set('   ')
    boat95 = Button(window, textvariable=boatshow95)
    boat95.grid(row=3, column=6, padx=3)
    boatshow96 = StringVar(window)
    boatshow96.set('   ')
    boat96 = Button(window, textvariable=boatshow96)
    boat96.grid(row=3, column=7, padx=3)
    boatshow97 = StringVar(window)
    boatshow97.set('   ')
    boat97 = Button(window, textvariable=boatshow97)
    boat97.grid(row=3, column=8, padx=3)
    boatshow98 = StringVar(window)
    boatshow98.set('   ')
    boat98 = Button(window, textvariable=boatshow98)
    boat98.grid(row=3, column=9, padx=3)
    boatshow99 = StringVar(window)
    boatshow99.set('   ')
    boat99 = Button(window, textvariable=boatshow99)
    boat99.grid(row=3, column=10, padx=3)
    boatshow910 = StringVar(window)
    boatshow910.set('   ')
    boat910 = Button(window, textvariable=boatshow910)
    boat910.grid(row=3, column=11, padx=3)
    boatshow101 = StringVar(window)
    boatshow101.set('   ')
    boat101 = Button(window, textvariable=boatshow101)
    boat101.grid(row=2, column=2, padx=3)
    boatshow102 = StringVar(window)
    boatshow102.set('   ')
    boat102 = Button(window, textvariable=boatshow102)
    boat102.grid(row=2, column=3, padx=3)
    boatshow103 = StringVar(window)
    boatshow103.set('   ')
    boat103 = Button(window, textvariable=boatshow103)
    boat103.grid(row=2, column=4, padx=3)
    boatshow104 = StringVar(window)
    boatshow104.set('   ')
    boat104 = Button(window, textvariable=boatshow104)
    boat104.grid(row=2, column=5, padx=3)
    boatshow105 = StringVar(window)
    boatshow105.set('   ')
    boat105 = Button(window, textvariable=boatshow105)
    boat105.grid(row=2, column=6, padx=3)
    boatshow106 = StringVar(window)
    boatshow106.set('   ')
    boat106 = Button(window, textvariable=boatshow106)
    boat106.grid(row=2, column=7, padx=3)
    boatshow107 = StringVar(window)
    boatshow107.set('   ')
    boat107 = Button(window, textvariable=boatshow107)
    boat107.grid(row=2, column=8, padx=3)
    boatshow108 = StringVar(window)
    boatshow108.set('   ')
    boat108 = Button(window, textvariable=boatshow108)
    boat108.grid(row=2, column=9, padx=3)
    boatshow109 = StringVar(window)
    boatshow109.set('   ')
    boat109 = Button(window, textvariable=boatshow109)
    boat109.grid(row=2, column=10, padx=3)
    boatshow1010 = StringVar(window)
    boatshow1010.set('   ')
    boat1010 = Button(window, textvariable=boatshow1010)
    boat1010.grid(row=2, column=11, padx=3)

    boatshow112 = StringVar(window)
    boatshow112.set('   ')
    boat112 = Button(window, textvariable=boatshow112)
    boat112.grid(row=11, column=13, padx=3)
    boatshow122 = StringVar(window)
    boatshow122.set('   ')
    boat122 = Button(window, textvariable=boatshow122)
    boat122.grid(row=11, column=14, padx=3)
    boatshow132 = StringVar(window)
    boatshow132.set('   ')
    boat132 = Button(window, textvariable=boatshow132)
    boat132.grid(row=11, column=15, padx=3)
    boatshow142 = StringVar(window)
    boatshow142.set('   ')
    boat142 = Button(window, textvariable=boatshow142)
    boat142.grid(row=11, column=16, padx=3)
    boatshow152 = StringVar(window)
    boatshow152.set('   ')
    boat152 = Button(window, textvariable=boatshow152)
    boat152.grid(row=11, column=17, padx=3)
    boatshow162 = StringVar(window)
    boatshow162.set('   ')
    boat162 = Button(window, textvariable=boatshow162)
    boat162.grid(row=11, column=18, padx=3)
    boatshow172 = StringVar(window)
    boatshow172.set('   ')
    boat172 = Button(window, textvariable=boatshow172)
    boat172.grid(row=11, column=19, padx=3)
    boatshow182 = StringVar(window)
    boatshow182.set('   ')
    boat182 = Button(window, textvariable=boatshow182)
    boat182.grid(row=11, column=20, padx=3)
    boatshow192 = StringVar(window)
    boatshow192.set('   ')
    boat192 = Button(window, textvariable=boatshow192)
    boat192.grid(row=11, column=21, padx=3)
    boatshow1102 = StringVar(window)
    boatshow1102.set('   ')
    boat1102 = Button(window, textvariable=boatshow1102)
    boat1102.grid(row=11, column=22, padx=3)
    boatshow212 = StringVar(window)
    boatshow212.set('   ')
    boat212 = Button(window, textvariable=boatshow212)
    boat212.grid(row=10, column=13, padx=3)
    boatshow222 = StringVar(window)
    boatshow222.set('   ')
    boat222 = Button(window, textvariable=boatshow222)
    boat222.grid(row=10, column=14, padx=3)
    boatshow232 = StringVar(window)
    boatshow232.set('   ')
    boat232 = Button(window, textvariable=boatshow232)
    boat232.grid(row=10, column=15, padx=3)
    boatshow242 = StringVar(window)
    boatshow242.set('   ')
    boat242 = Button(window, textvariable=boatshow242)
    boat242.grid(row=10, column=16, padx=3)
    boatshow252 = StringVar(window)
    boatshow252.set('   ')
    boat252 = Button(window, textvariable=boatshow252)
    boat252.grid(row=10, column=17, padx=3)
    boatshow262 = StringVar(window)
    boatshow262.set('   ')
    boat262 = Button(window, textvariable=boatshow262)
    boat262.grid(row=10, column=18, padx=3)
    boatshow272 = StringVar(window)
    boatshow272.set('   ')
    boat272 = Button(window, textvariable=boatshow272)
    boat272.grid(row=10, column=19, padx=3)
    boatshow282 = StringVar(window)
    boatshow282.set('   ')
    boat282 = Button(window, textvariable=boatshow282)
    boat282.grid(row=10, column=20, padx=3)
    boatshow292 = StringVar(window)
    boatshow292.set('   ')
    boat292 = Button(window, textvariable=boatshow292)
    boat292.grid(row=10, column=21, padx=3)
    boatshow2102 = StringVar(window)
    boatshow2102.set('   ')
    boat2102 = Button(window, textvariable=boatshow2102)
    boat2102.grid(row=10, column=22, padx=3)
    boatshow312 = StringVar(window)
    boatshow312.set('   ')
    boat312 = Button(window, textvariable=boatshow312)
    boat312.grid(row=9, column=13, padx=3)
    boatshow322 = StringVar(window)
    boatshow322.set('   ')
    boat322 = Button(window, textvariable=boatshow322)
    boat322.grid(row=9, column=14, padx=3)
    boatshow332 = StringVar(window)
    boatshow332.set('   ')
    boat332 = Button(window, textvariable=boatshow332)
    boat332.grid(row=9, column=15, padx=3)
    boatshow342 = StringVar(window)
    boatshow342.set('   ')
    boat342 = Button(window, textvariable=boatshow342)
    boat342.grid(row=9, column=16, padx=3)
    boatshow352 = StringVar(window)
    boatshow352.set('   ')
    boat352 = Button(window, textvariable=boatshow352)
    boat352.grid(row=9, column=17, padx=3)
    boatshow362 = StringVar(window)
    boatshow362.set('   ')
    boat362 = Button(window, textvariable=boatshow362)
    boat362.grid(row=9, column=18, padx=3)
    boatshow372 = StringVar(window)
    boatshow372.set('   ')
    boat372 = Button(window, textvariable=boatshow372)
    boat372.grid(row=9, column=19, padx=3)
    boatshow382 = StringVar(window)
    boatshow382.set('   ')
    boat382 = Button(window, textvariable=boatshow382)
    boat382.grid(row=9, column=20, padx=3)
    boatshow392 = StringVar(window)
    boatshow392.set('   ')
    boat392 = Button(window, textvariable=boatshow392)
    boat392.grid(row=9, column=21, padx=3)
    boatshow3102 = StringVar(window)
    boatshow3102.set('   ')
    boat3102 = Button(window, textvariable=boatshow3102)
    boat3102.grid(row=9, column=22, padx=3)
    boatshow412 = StringVar(window)
    boatshow412.set('   ')
    boat412 = Button(window, textvariable=boatshow412)
    boat412.grid(row=8, column=13, padx=3)
    boatshow422 = StringVar(window)
    boatshow422.set('   ')
    boat422 = Button(window, textvariable=boatshow422)
    boat422.grid(row=8, column=14, padx=3)
    boatshow432 = StringVar(window)
    boatshow432.set('   ')
    boat432 = Button(window, textvariable=boatshow432)
    boat432.grid(row=8, column=15, padx=3)
    boatshow442 = StringVar(window)
    boatshow442.set('   ')
    boat442 = Button(window, textvariable=boatshow442)
    boat442.grid(row=8, column=16, padx=3)
    boatshow452 = StringVar(window)
    boatshow452.set('   ')
    boat452 = Button(window, textvariable=boatshow452)
    boat452.grid(row=8, column=17, padx=3)
    boatshow462 = StringVar(window)
    boatshow462.set('   ')
    boat462 = Button(window, textvariable=boatshow462)
    boat462.grid(row=8, column=18, padx=3)
    boatshow472 = StringVar(window)
    boatshow472.set('   ')
    boat472 = Button(window, textvariable=boatshow472)
    boat472.grid(row=8, column=19, padx=3)
    boatshow482 = StringVar(window)
    boatshow482.set('   ')
    boat482 = Button(window, textvariable=boatshow482)
    boat482.grid(row=8, column=20, padx=3)
    boatshow492 = StringVar(window)
    boatshow492.set('   ')
    boat492 = Button(window, textvariable=boatshow492)
    boat492.grid(row=8, column=21, padx=3)
    boatshow4102 = StringVar(window)
    boatshow4102.set('   ')
    boat4102 = Button(window, textvariable=boatshow4102)
    boat4102.grid(row=8, column=22, padx=3)
    boatshow512 = StringVar(window)
    boatshow512.set('   ')
    boat512 = Button(window, textvariable=boatshow512)
    boat512.grid(row=7, column=13, padx=3)
    boatshow522 = StringVar(window)
    boatshow522.set('   ')
    boat522 = Button(window, textvariable=boatshow522)
    boat522.grid(row=7, column=14, padx=3)
    boatshow532 = StringVar(window)
    boatshow532.set('   ')
    boat532 = Button(window, textvariable=boatshow532)
    boat532.grid(row=7, column=15, padx=3)
    boatshow542 = StringVar(window)
    boatshow542.set('   ')
    boat542 = Button(window, textvariable=boatshow542)
    boat542.grid(row=7, column=16, padx=3)
    boatshow552 = StringVar(window)
    boatshow552.set('   ')
    boat552 = Button(window, textvariable=boatshow552)
    boat552.grid(row=7, column=17, padx=3)
    boatshow562 = StringVar(window)
    boatshow562.set('   ')
    boat562 = Button(window, textvariable=boatshow562)
    boat562.grid(row=7, column=18, padx=3)
    boatshow572 = StringVar(window)
    boatshow572.set('   ')
    boat572 = Button(window, textvariable=boatshow572)
    boat572.grid(row=7, column=19, padx=3)
    boatshow582 = StringVar(window)
    boatshow582.set('   ')
    boat582 = Button(window, textvariable=boatshow582)
    boat582.grid(row=7, column=20, padx=3)
    boatshow592 = StringVar(window)
    boatshow592.set('   ')
    boat592 = Button(window, textvariable=boatshow592)
    boat592.grid(row=7, column=21, padx=3)
    boatshow5102 = StringVar(window)
    boatshow5102.set('   ')
    boat5102 = Button(window, textvariable=boatshow5102)
    boat5102.grid(row=7, column=22, padx=3)
    boatshow612 = StringVar(window)
    boatshow612.set('   ')
    boat612 = Button(window, textvariable=boatshow612)
    boat612.grid(row=6, column=13, padx=3)
    boatshow622 = StringVar(window)
    boatshow622.set('   ')
    boat622 = Button(window, textvariable=boatshow622)
    boat622.grid(row=6, column=14, padx=3)
    boatshow632 = StringVar(window)
    boatshow632.set('   ')
    boat632 = Button(window, textvariable=boatshow632)
    boat632.grid(row=6, column=15, padx=3)
    boatshow642 = StringVar(window)
    boatshow642.set('   ')
    boat642 = Button(window, textvariable=boatshow642)
    boat642.grid(row=6, column=16, padx=3)
    boatshow652 = StringVar(window)
    boatshow652.set('   ')
    boat652 = Button(window, textvariable=boatshow652)
    boat652.grid(row=6, column=17, padx=3)
    boatshow662 = StringVar(window)
    boatshow662.set('   ')
    boat662 = Button(window, textvariable=boatshow662)
    boat662.grid(row=6, column=18, padx=3)
    boatshow672 = StringVar(window)
    boatshow672.set('   ')
    boat672 = Button(window, textvariable=boatshow672)
    boat672.grid(row=6, column=19, padx=3)
    boatshow682 = StringVar(window)
    boatshow682.set('   ')
    boat682 = Button(window, textvariable=boatshow682)
    boat682.grid(row=6, column=20, padx=3)
    boatshow692 = StringVar(window)
    boatshow692.set('   ')
    boat692 = Button(window, textvariable=boatshow692)
    boat692.grid(row=6, column=21, padx=3)
    boatshow6102 = StringVar(window)
    boatshow6102.set('   ')
    boat6102 = Button(window, textvariable=boatshow6102)
    boat6102.grid(row=6, column=22, padx=3)
    boatshow712 = StringVar(window)
    boatshow712.set('   ')
    boat712 = Button(window, textvariable=boatshow712)
    boat712.grid(row=5, column=13, padx=3)
    boatshow722 = StringVar(window)
    boatshow722.set('   ')
    boat722 = Button(window, textvariable=boatshow722)
    boat722.grid(row=5, column=14, padx=3)
    boatshow732 = StringVar(window)
    boatshow732.set('   ')
    boat732 = Button(window, textvariable=boatshow732)
    boat732.grid(row=5, column=15, padx=3)
    boatshow742 = StringVar(window)
    boatshow742.set('   ')
    boat742 = Button(window, textvariable=boatshow742)
    boat742.grid(row=5, column=16, padx=3)
    boatshow752 = StringVar(window)
    boatshow752.set('   ')
    boat752 = Button(window, textvariable=boatshow752)
    boat752.grid(row=5, column=17, padx=3)
    boatshow762 = StringVar(window)
    boatshow762.set('   ')
    boat762 = Button(window, textvariable=boatshow762)
    boat762.grid(row=5, column=18, padx=3)
    boatshow772 = StringVar(window)
    boatshow772.set('   ')
    boat772 = Button(window, textvariable=boatshow772)
    boat772.grid(row=5, column=19, padx=3)
    boatshow782 = StringVar(window)
    boatshow782.set('   ')
    boat782 = Button(window, textvariable=boatshow782)
    boat782.grid(row=5, column=20, padx=3)
    boatshow792 = StringVar(window)
    boatshow792.set('   ')
    boat792 = Button(window, textvariable=boatshow792)
    boat792.grid(row=5, column=21, padx=3)
    boatshow7102 = StringVar(window)
    boatshow7102.set('   ')
    boat7102 = Button(window, textvariable=boatshow7102)
    boat7102.grid(row=5, column=22, padx=3)
    boatshow812 = StringVar(window)
    boatshow812.set('   ')
    boat812 = Button(window, textvariable=boatshow812)
    boat812.grid(row=4, column=13, padx=3)
    boatshow822 = StringVar(window)
    boatshow822.set('   ')
    boat822 = Button(window, textvariable=boatshow822)
    boat822.grid(row=4, column=14, padx=3)
    boatshow832 = StringVar(window)
    boatshow832.set('   ')
    boat832 = Button(window, textvariable=boatshow832)
    boat832.grid(row=4, column=15, padx=3)
    boatshow842 = StringVar(window)
    boatshow842.set('   ')
    boat842 = Button(window, textvariable=boatshow842)
    boat842.grid(row=4, column=16, padx=3)
    boatshow852 = StringVar(window)
    boatshow852.set('   ')
    boat852 = Button(window, textvariable=boatshow852)
    boat852.grid(row=4, column=17, padx=3)
    boatshow862 = StringVar(window)
    boatshow862.set('   ')
    boat862 = Button(window, textvariable=boatshow862)
    boat862.grid(row=4, column=18, padx=3)
    boatshow872 = StringVar(window)
    boatshow872.set('   ')
    boat872 = Button(window, textvariable=boatshow872)
    boat872.grid(row=4, column=19, padx=3)
    boatshow882 = StringVar(window)
    boatshow882.set('   ')
    boat882 = Button(window, textvariable=boatshow882)
    boat882.grid(row=4, column=20, padx=3)
    boatshow892 = StringVar(window)
    boatshow892.set('   ')
    boat892 = Button(window, textvariable=boatshow892)
    boat892.grid(row=4, column=21, padx=3)
    boatshow8102 = StringVar(window)
    boatshow8102.set('   ')
    boat8102 = Button(window, textvariable=boatshow8102)
    boat8102.grid(row=4, column=22, padx=3)
    boatshow912 = StringVar(window)
    boatshow912.set('   ')
    boat912 = Button(window, textvariable=boatshow912)
    boat912.grid(row=3, column=13, padx=3)
    boatshow922 = StringVar(window)
    boatshow922.set('   ')
    boat922 = Button(window, textvariable=boatshow922)
    boat922.grid(row=3, column=14, padx=3)
    boatshow932 = StringVar(window)
    boatshow932.set('   ')
    boat932 = Button(window, textvariable=boatshow932)
    boat932.grid(row=3, column=15, padx=3)
    boatshow942 = StringVar(window)
    boatshow942.set('   ')
    boat942 = Button(window, textvariable=boatshow942)
    boat942.grid(row=3, column=16, padx=3)
    boatshow952 = StringVar(window)
    boatshow952.set('   ')
    boat952 = Button(window, textvariable=boatshow952)
    boat952.grid(row=3, column=17, padx=3)
    boatshow962 = StringVar(window)
    boatshow962.set('   ')
    boat962 = Button(window, textvariable=boatshow962)
    boat962.grid(row=3, column=18, padx=3)
    boatshow972 = StringVar(window)
    boatshow972.set('   ')
    boat972 = Button(window, textvariable=boatshow972)
    boat972.grid(row=3, column=19, padx=3)
    boatshow982 = StringVar(window)
    boatshow982.set('   ')
    boat982 = Button(window, textvariable=boatshow982)
    boat982.grid(row=3, column=20, padx=3)
    boatshow992 = StringVar(window)
    boatshow992.set('   ')
    boat992 = Button(window, textvariable=boatshow992)
    boat992.grid(row=3, column=21, padx=3)
    boatshow9102 = StringVar(window)
    boatshow9102.set('   ')
    boat9102 = Button(window, textvariable=boatshow9102)
    boat9102.grid(row=3, column=22, padx=3)
    boatshow1012 = StringVar(window)
    boatshow1012.set('   ')
    boat1012 = Button(window, textvariable=boatshow1012)
    boat1012.grid(row=2, column=13, padx=3)
    boatshow1022 = StringVar(window)
    boatshow1022.set('   ')
    boat1022 = Button(window, textvariable=boatshow1022)
    boat1022.grid(row=2, column=14, padx=3)
    boatshow1032 = StringVar(window)
    boatshow1032.set('   ')
    boat1032 = Button(window, textvariable=boatshow1032)
    boat1032.grid(row=2, column=15, padx=3)
    boatshow1042 = StringVar(window)
    boatshow1042.set('   ')
    boat1042 = Button(window, textvariable=boatshow1042)
    boat1042.grid(row=2, column=16, padx=3)
    boatshow1052 = StringVar(window)
    boatshow1052.set('   ')
    boat1052 = Button(window, textvariable=boatshow1052)
    boat1052.grid(row=2, column=17, padx=3)
    boatshow1062 = StringVar(window)
    boatshow1062.set('   ')
    boat1062 = Button(window, textvariable=boatshow1062)
    boat1062.grid(row=2, column=18, padx=3)
    boatshow1072 = StringVar(window)
    boatshow1072.set('   ')
    boat1072 = Button(window, textvariable=boatshow1072)
    boat1072.grid(row=2, column=19, padx=3)
    boatshow1082 = StringVar(window)
    boatshow1082.set('   ')
    boat1082 = Button(window, textvariable=boatshow1082)
    boat1082.grid(row=2, column=20, padx=3)
    boatshow1092 = StringVar(window)
    boatshow1092.set('   ')
    boat1092 = Button(window, textvariable=boatshow1092)
    boat1092.grid(row=2, column=21, padx=3)
    boatshow10102 = StringVar(window)
    boatshow10102.set('   ')
    boat10102 = Button(window, textvariable=boatshow10102)
    boat10102.grid(row=2, column=22, padx=3)

    def gogrt11(event):
        print(event)
        global recentcord
        recentcord = [0,0]
        run(1)
    boat11.bind('<Button>', gogrt11)
    def gogrt12(event):
        print(event)
        global recentcord
        recentcord = [0,1]
        run(1)
    boat12.bind('<Button>', gogrt12)
    def gogrt13(event):
        print(event)
        global recentcord
        recentcord = [0,2]
        run(1)
    boat13.bind('<Button>', gogrt13)
    def gogrt14(event):
        print(event)
        global recentcord
        recentcord = [0,3]
        run(1)
    boat14.bind('<Button>', gogrt14)
    def gogrt15(event):
        print(event)
        global recentcord
        recentcord = [0,4]
        run(1)
    boat15.bind('<Button>', gogrt15)
    def gogrt16(event):
        print(event)
        global recentcord
        recentcord = [0,5]
        run(1)
    boat16.bind('<Button>', gogrt16)
    def gogrt17(event):
        print(event)
        global recentcord
        recentcord = [0,6]
        run(1)
    boat17.bind('<Button>', gogrt17)
    def gogrt18(event):
        print(event)
        global recentcord
        recentcord = [0,7]
        run(1)
    boat18.bind('<Button>', gogrt18)
    def gogrt19(event):
        print(event)
        global recentcord
        recentcord = [0,8]
        run(1)
    boat19.bind('<Button>', gogrt19)
    def gogrt110(event):
        print(event)
        global recentcord
        recentcord = [0,9]
        run(1)
    boat110.bind('<Button>', gogrt110)
    def gogrt21(event):
        print(event)
        global recentcord
        recentcord = [1,0]
        run(1)
    boat21.bind('<Button>', gogrt21)
    def gogrt22(event):
        print(event)
        global recentcord
        recentcord = [1,1]
        run(1)
    boat22.bind('<Button>', gogrt22)
    def gogrt23(event):
        print(event)
        global recentcord
        recentcord = [1,2]
        run(1)
    boat23.bind('<Button>', gogrt23)
    def gogrt24(event):
        print(event)
        global recentcord
        recentcord = [1,3]
        run(1)
    boat24.bind('<Button>', gogrt24)
    def gogrt25(event):
        print(event)
        global recentcord
        recentcord = [1,4]
        run(1)
    boat25.bind('<Button>', gogrt25)
    def gogrt26(event):
        print(event)
        global recentcord
        recentcord = [1,5]
        run(1)
    boat26.bind('<Button>', gogrt26)
    def gogrt27(event):
        print(event)
        global recentcord
        recentcord = [1,6]
        run(1)
    boat27.bind('<Button>', gogrt27)
    def gogrt28(event):
        print(event)
        global recentcord
        recentcord = [1,7]
        run(1)
    boat28.bind('<Button>', gogrt28)
    def gogrt29(event):
        print(event)
        global recentcord
        recentcord = [1,8]
        run(1)
    boat29.bind('<Button>', gogrt29)
    def gogrt210(event):
        print(event)
        global recentcord
        recentcord = [1,9]
        run(1)
    boat210.bind('<Button>', gogrt210)
    def gogrt31(event):
        print(event)
        global recentcord
        recentcord = [2,0]
        run(1)
    boat31.bind('<Button>', gogrt31)
    def gogrt32(event):
        print(event)
        global recentcord
        recentcord = [2,1]
        run(1)
    boat32.bind('<Button>', gogrt32)
    def gogrt33(event):
        print(event)
        global recentcord
        recentcord = [2,2]
        run(1)
    boat33.bind('<Button>', gogrt33)
    def gogrt34(event):
        print(event)
        global recentcord
        recentcord = [2,3]
        run(1)
    boat34.bind('<Button>', gogrt34)
    def gogrt35(event):
        print(event)
        global recentcord
        recentcord = [2,4]
        run(1)
    boat35.bind('<Button>', gogrt35)
    def gogrt36(event):
        print(event)
        global recentcord
        recentcord = [2,5]
        run(1)
    boat36.bind('<Button>', gogrt36)
    def gogrt37(event):
        print(event)
        global recentcord
        recentcord = [2,6]
        run(1)
    boat37.bind('<Button>', gogrt37)
    def gogrt38(event):
        print(event)
        global recentcord
        recentcord = [2,7]
        run(1)
    boat38.bind('<Button>', gogrt38)
    def gogrt39(event):
        print(event)
        global recentcord
        recentcord = [2,8]
        run(1)
    boat39.bind('<Button>', gogrt39)
    def gogrt310(event):
        print(event)
        global recentcord
        recentcord = [2,9]
        run(1)
    boat310.bind('<Button>', gogrt310)
    def gogrt41(event):
        print(event)
        global recentcord
        recentcord = [3,0]
        run(1)
    boat41.bind('<Button>', gogrt41)
    def gogrt42(event):
        print(event)
        global recentcord
        recentcord = [3,1]
        run(1)
    boat42.bind('<Button>', gogrt42)
    def gogrt43(event):
        print(event)
        global recentcord
        recentcord = [3,2]
        run(1)
    boat43.bind('<Button>', gogrt43)
    def gogrt44(event):
        print(event)
        global recentcord
        recentcord = [3,3]
        run(1)
    boat44.bind('<Button>', gogrt44)
    def gogrt45(event):
        print(event)
        global recentcord
        recentcord = [3,4]
        run(1)
    boat45.bind('<Button>', gogrt45)
    def gogrt46(event):
        print(event)
        global recentcord
        recentcord = [3,5]
        run(1)
    boat46.bind('<Button>', gogrt46)
    def gogrt47(event):
        print(event)
        global recentcord
        recentcord = [3,6]
        run(1)
    boat47.bind('<Button>', gogrt47)
    def gogrt48(event):
        print(event)
        global recentcord
        recentcord = [3,7]
        run(1)
    boat48.bind('<Button>', gogrt48)
    def gogrt49(event):
        print(event)
        global recentcord
        recentcord = [3,8]
        run(1)
    boat49.bind('<Button>', gogrt49)
    def gogrt410(event):
        print(event)
        global recentcord
        recentcord = [3,9]
        run(1)
    boat410.bind('<Button>', gogrt410)
    def gogrt51(event):
        print(event)
        global recentcord
        recentcord = [4,0]
        run(1)
    boat51.bind('<Button>', gogrt51)
    def gogrt52(event):
        print(event)
        global recentcord
        recentcord = [4,1]
        run(1)
    boat52.bind('<Button>', gogrt52)
    def gogrt53(event):
        print(event)
        global recentcord
        recentcord = [4,2]
        run(1)
    boat53.bind('<Button>', gogrt53)
    def gogrt54(event):
        print(event)
        global recentcord
        recentcord = [4,3]
        run(1)
    boat54.bind('<Button>', gogrt54)
    def gogrt55(event):
        print(event)
        global recentcord
        recentcord = [4,4]
        run(1)
    boat55.bind('<Button>', gogrt55)
    def gogrt56(event):
        print(event)
        global recentcord
        recentcord = [4,5]
        run(1)
    boat56.bind('<Button>', gogrt56)
    def gogrt57(event):
        print(event)
        global recentcord
        recentcord = [4,6]
        run(1)
    boat57.bind('<Button>', gogrt57)
    def gogrt58(event):
        print(event)
        global recentcord
        recentcord = [4,7]
        run(1)
    boat58.bind('<Button>', gogrt58)
    def gogrt59(event):
        print(event)
        global recentcord
        recentcord = [4,8]
        run(1)
    boat59.bind('<Button>', gogrt59)
    def gogrt510(event):
        print(event)
        global recentcord
        recentcord = [4,9]
        run(1)
    boat510.bind('<Button>', gogrt510)
    def gogrt61(event):
        print(event)
        global recentcord
        recentcord = [5,0]
        run(1)
    boat61.bind('<Button>', gogrt61)
    def gogrt62(event):
        print(event)
        global recentcord
        recentcord = [5,1]
        run(1)
    boat62.bind('<Button>', gogrt62)
    def gogrt63(event):
        print(event)
        global recentcord
        recentcord = [5,2]
        run(1)
    boat63.bind('<Button>', gogrt63)
    def gogrt64(event):
        print(event)
        global recentcord
        recentcord = [5,3]
        run(1)
    boat64.bind('<Button>', gogrt64)
    def gogrt65(event):
        print(event)
        global recentcord
        recentcord = [5,4]
        run(1)
    boat65.bind('<Button>', gogrt65)
    def gogrt66(event):
        print(event)
        global recentcord
        recentcord = [5,5]
        run(1)
    boat66.bind('<Button>', gogrt66)
    def gogrt67(event):
        print(event)
        global recentcord
        recentcord = [5,6]
        run(1)
    boat67.bind('<Button>', gogrt67)
    def gogrt68(event):
        print(event)
        global recentcord
        recentcord = [5,7]
        run(1)
    boat68.bind('<Button>', gogrt68)
    def gogrt69(event):
        print(event)
        global recentcord
        recentcord = [5,8]
        run(1)
    boat69.bind('<Button>', gogrt69)
    def gogrt610(event):
        print(event)
        global recentcord
        recentcord = [5,9]
        run(1)
    boat610.bind('<Button>', gogrt610)
    def gogrt71(event):
        print(event)
        global recentcord
        recentcord = [6,0]
        run(1)
    boat71.bind('<Button>', gogrt71)
    def gogrt72(event):
        print(event)
        global recentcord
        recentcord = [6,1]
        run(1)
    boat72.bind('<Button>', gogrt72)
    def gogrt73(event):
        print(event)
        global recentcord
        recentcord = [6,2]
        run(1)
    boat73.bind('<Button>', gogrt73)
    def gogrt74(event):
        print(event)
        global recentcord
        recentcord = [6,3]
        run(1)
    boat74.bind('<Button>', gogrt74)
    def gogrt75(event):
        print(event)
        global recentcord
        recentcord = [6,4]
        run(1)
    boat75.bind('<Button>', gogrt75)
    def gogrt76(event):
        print(event)
        global recentcord
        recentcord = [6,5]
        run(1)
    boat76.bind('<Button>', gogrt76)
    def gogrt77(event):
        print(event)
        global recentcord
        recentcord = [6,6]
        run(1)
    boat77.bind('<Button>', gogrt77)
    def gogrt78(event):
        print(event)
        global recentcord
        recentcord = [6,7]
        run(1)
    boat78.bind('<Button>', gogrt78)
    def gogrt79(event):
        print(event)
        global recentcord
        recentcord = [6,8]
        run(1)
    boat79.bind('<Button>', gogrt79)
    def gogrt710(event):
        print(event)
        global recentcord
        recentcord = [6,9]
        run(1)
    boat710.bind('<Button>', gogrt710)
    def gogrt81(event):
        print(event)
        global recentcord
        recentcord = [7,0]
        run(1)
    boat81.bind('<Button>', gogrt81)
    def gogrt82(event):
        print(event)
        global recentcord
        recentcord = [7,1]
        run(1)
    boat82.bind('<Button>', gogrt82)
    def gogrt83(event):
        print(event)
        global recentcord
        recentcord = [7,2]
        run(1)
    boat83.bind('<Button>', gogrt83)
    def gogrt84(event):
        print(event)
        global recentcord
        recentcord = [7,3]
        run(1)
    boat84.bind('<Button>', gogrt84)
    def gogrt85(event):
        print(event)
        global recentcord
        recentcord = [7,4]
        run(1)
    boat85.bind('<Button>', gogrt85)
    def gogrt86(event):
        print(event)
        global recentcord
        recentcord = [7,5]
        run(1)
    boat86.bind('<Button>', gogrt86)
    def gogrt87(event):
        print(event)
        global recentcord
        recentcord = [7,6]
        run(1)
    boat87.bind('<Button>', gogrt87)
    def gogrt88(event):
        print(event)
        global recentcord
        recentcord = [7,7]
        run(1)
    boat88.bind('<Button>', gogrt88)
    def gogrt89(event):
        print(event)
        global recentcord
        recentcord = [7,8]
        run(1)
    boat89.bind('<Button>', gogrt89)
    def gogrt810(event):
        print(event)
        global recentcord
        recentcord = [7,9]
        run(1)
    boat810.bind('<Button>', gogrt810)
    def gogrt91(event):
        print(event)
        global recentcord
        recentcord = [8,0]
        run(1)
    boat91.bind('<Button>', gogrt91)
    def gogrt92(event):
        print(event)
        global recentcord
        recentcord = [8,1]
        run(1)
    boat92.bind('<Button>', gogrt92)
    def gogrt93(event):
        print(event)
        global recentcord
        recentcord = [8,2]
        run(1)
    boat93.bind('<Button>', gogrt93)
    def gogrt94(event):
        print(event)
        global recentcord
        recentcord = [8,3]
        run(1)
    boat94.bind('<Button>', gogrt94)
    def gogrt95(event):
        print(event)
        global recentcord
        recentcord = [8,4]
        run(1)
    boat95.bind('<Button>', gogrt95)
    def gogrt96(event):
        print(event)
        global recentcord
        recentcord = [8,5]
        run(1)
    boat96.bind('<Button>', gogrt96)
    def gogrt97(event):
        print(event)
        global recentcord
        recentcord = [8,6]
        run(1)
    boat97.bind('<Button>', gogrt97)
    def gogrt98(event):
        print(event)
        global recentcord
        recentcord = [8,7]
        run(1)
    boat98.bind('<Button>', gogrt98)
    def gogrt99(event):
        print(event)
        global recentcord
        recentcord = [8,8]
        run(1)
    boat99.bind('<Button>', gogrt99)
    def gogrt910(event):
        print(event)
        global recentcord
        recentcord = [8,9]
        run(1)
    boat910.bind('<Button>', gogrt910)
    def gogrt101(event):
        print(event)
        global recentcord
        recentcord = [9,0]
        run(1)
    boat101.bind('<Button>', gogrt101)
    def gogrt102(event):
        print(event)
        global recentcord
        recentcord = [9,1]
        run(1)
    boat102.bind('<Button>', gogrt102)
    def gogrt103(event):
        print(event)
        global recentcord
        recentcord = [9,2]
        run(1)
    boat103.bind('<Button>', gogrt103)
    def gogrt104(event):
        print(event)
        global recentcord
        recentcord = [9,3]
        run(1)
    boat104.bind('<Button>', gogrt104)
    def gogrt105(event):
        print(event)
        global recentcord
        recentcord = [9,4]
        run(1)
    boat105.bind('<Button>', gogrt105)
    def gogrt106(event):
        print(event)
        global recentcord
        recentcord = [9,5]
        run(1)
    boat106.bind('<Button>', gogrt106)
    def gogrt107(event):
        print(event)
        global recentcord
        recentcord = [9,6]
        run(1)
    boat107.bind('<Button>', gogrt107)
    def gogrt108(event):
        print(event)
        global recentcord
        recentcord = [9,7]
        run(1)
    boat108.bind('<Button>', gogrt108)
    def gogrt109(event):
        print(event)
        global recentcord
        recentcord = [9,8]
        run(1)
    boat109.bind('<Button>', gogrt109)
    def gogrt1010(event):
        print(event)
        global recentcord
        recentcord = [9,9]
        run(1)
    boat1010.bind('<Button>', gogrt1010)

    def gogrt112(event):
        print(event)
        global recentcord
        recentcord = [0,0]
        run(2)
    boat112.bind('<Button>', gogrt112)
    def gogrt122(event):
        print(event)
        global recentcord
        recentcord = [0,1]
        run(2)
    boat122.bind('<Button>', gogrt122)
    def gogrt132(event):
        print(event)
        global recentcord
        recentcord = [0,2]
        run(2)
    boat132.bind('<Button>', gogrt132)
    def gogrt142(event):
        print(event)
        global recentcord
        recentcord = [0,3]
        run(2)
    boat142.bind('<Button>', gogrt142)
    def gogrt152(event):
        print(event)
        global recentcord
        recentcord = [0,4]
        run(2)
    boat152.bind('<Button>', gogrt152)
    def gogrt162(event):
        print(event)
        global recentcord
        recentcord = [0,5]
        run(2)
    boat162.bind('<Button>', gogrt162)
    def gogrt172(event):
        print(event)
        global recentcord
        recentcord = [0,6]
        run(2)
    boat172.bind('<Button>', gogrt172)
    def gogrt182(event):
        print(event)
        global recentcord
        recentcord = [0,7]
        run(2)
    boat182.bind('<Button>', gogrt182)
    def gogrt192(event):
        print(event)
        global recentcord
        recentcord = [0,8]
        run(2)
    boat192.bind('<Button>', gogrt192)
    def gogrt1102(event):
        print(event)
        global recentcord
        recentcord = [0,9]
        run(2)
    boat1102.bind('<Button>', gogrt1102)
    def gogrt212(event):
        print(event)
        global recentcord
        recentcord = [1,0]
        run(2)
    boat212.bind('<Button>', gogrt212)
    def gogrt222(event):
        print(event)
        global recentcord
        recentcord = [1,1]
        run(2)
    boat222.bind('<Button>', gogrt222)
    def gogrt232(event):
        print(event)
        global recentcord
        recentcord = [1,2]
        run(2)
    boat232.bind('<Button>', gogrt232)
    def gogrt242(event):
        print(event)
        global recentcord
        recentcord = [1,3]
        run(2)
    boat242.bind('<Button>', gogrt242)
    def gogrt252(event):
        print(event)
        global recentcord
        recentcord = [1,4]
        run(2)
    boat252.bind('<Button>', gogrt252)
    def gogrt262(event):
        print(event)
        global recentcord
        recentcord = [1,5]
        run(2)
    boat262.bind('<Button>', gogrt262)
    def gogrt272(event):
        print(event)
        global recentcord
        recentcord = [1,6]
        run(2)
    boat272.bind('<Button>', gogrt272)
    def gogrt282(event):
        print(event)
        global recentcord
        recentcord = [1,7]
        run(2)
    boat282.bind('<Button>', gogrt282)
    def gogrt292(event):
        print(event)
        global recentcord
        recentcord = [1,8]
        run(2)
    boat292.bind('<Button>', gogrt292)
    def gogrt2102(event):
        print(event)
        global recentcord
        recentcord = [1,9]
        run(2)
    boat2102.bind('<Button>', gogrt2102)
    def gogrt312(event):
        print(event)
        global recentcord
        recentcord = [2,0]
        run(2)
    boat312.bind('<Button>', gogrt312)
    def gogrt322(event):
        print(event)
        global recentcord
        recentcord = [2,1]
        run(2)
    boat322.bind('<Button>', gogrt322)
    def gogrt332(event):
        print(event)
        global recentcord
        recentcord = [2,2]
        run(2)
    boat332.bind('<Button>', gogrt332)
    def gogrt342(event):
        print(event)
        global recentcord
        recentcord = [2,3]
        run(2)
    boat342.bind('<Button>', gogrt342)
    def gogrt352(event):
        print(event)
        global recentcord
        recentcord = [2,4]
        run(2)
    boat352.bind('<Button>', gogrt352)
    def gogrt362(event):
        print(event)
        global recentcord
        recentcord = [2,5]
        run(2)
    boat362.bind('<Button>', gogrt362)
    def gogrt372(event):
        print(event)
        global recentcord
        recentcord = [2,6]
        run(2)
    boat372.bind('<Button>', gogrt372)
    def gogrt382(event):
        print(event)
        global recentcord
        recentcord = [2,7]
        run(2)
    boat382.bind('<Button>', gogrt382)
    def gogrt392(event):
        print(event)
        global recentcord
        recentcord = [2,8]
        run(2)
    boat392.bind('<Button>', gogrt392)
    def gogrt3102(event):
        print(event)
        global recentcord
        recentcord = [2,9]
        run(2)
    boat3102.bind('<Button>', gogrt3102)
    def gogrt412(event):
        print(event)
        global recentcord
        recentcord = [3,0]
        run(2)
    boat412.bind('<Button>', gogrt412)
    def gogrt422(event):
        print(event)
        global recentcord
        recentcord = [3,1]
        run(2)
    boat422.bind('<Button>', gogrt422)
    def gogrt432(event):
        print(event)
        global recentcord
        recentcord = [3,2]
        run(2)
    boat432.bind('<Button>', gogrt432)
    def gogrt442(event):
        print(event)
        global recentcord
        recentcord = [3,3]
        run(2)
    boat442.bind('<Button>', gogrt442)
    def gogrt452(event):
        print(event)
        global recentcord
        recentcord = [3,4]
        run(2)
    boat452.bind('<Button>', gogrt452)
    def gogrt462(event):
        print(event)
        global recentcord
        recentcord = [3,5]
        run(2)
    boat462.bind('<Button>', gogrt462)
    def gogrt472(event):
        print(event)
        global recentcord
        recentcord = [3,6]
        run(2)
    boat472.bind('<Button>', gogrt472)
    def gogrt482(event):
        print(event)
        global recentcord
        recentcord = [3,7]
        run(2)
    boat482.bind('<Button>', gogrt482)
    def gogrt492(event):
        print(event)
        global recentcord
        recentcord = [3,8]
        run(2)
    boat492.bind('<Button>', gogrt492)
    def gogrt4102(event):
        print(event)
        global recentcord
        recentcord = [3,9]
        run(2)
    boat4102.bind('<Button>', gogrt4102)
    def gogrt512(event):
        print(event)
        global recentcord
        recentcord = [4,0]
        run(2)
    boat512.bind('<Button>', gogrt512)
    def gogrt522(event):
        print(event)
        global recentcord
        recentcord = [4,1]
        run(2)
    boat522.bind('<Button>', gogrt522)
    def gogrt532(event):
        print(event)
        global recentcord
        recentcord = [4,2]
        run(2)
    boat532.bind('<Button>', gogrt532)
    def gogrt542(event):
        print(event)
        global recentcord
        recentcord = [4,3]
        run(2)
    boat542.bind('<Button>', gogrt542)
    def gogrt552(event):
        print(event)
        global recentcord
        recentcord = [4,4]
        run(2)
    boat552.bind('<Button>', gogrt552)
    def gogrt562(event):
        print(event)
        global recentcord
        recentcord = [4,5]
        run(2)
    boat562.bind('<Button>', gogrt562)
    def gogrt572(event):
        print(event)
        global recentcord
        recentcord = [4,6]
        run(2)
    boat572.bind('<Button>', gogrt572)
    def gogrt582(event):
        print(event)
        global recentcord
        recentcord = [4,7]
        run(2)
    boat582.bind('<Button>', gogrt582)
    def gogrt592(event):
        print(event)
        global recentcord
        recentcord = [4,8]
        run(2)
    boat592.bind('<Button>', gogrt592)
    def gogrt5102(event):
        print(event)
        global recentcord
        recentcord = [4,9]
        run(2)
    boat5102.bind('<Button>', gogrt5102)
    def gogrt612(event):
        print(event)
        global recentcord
        recentcord = [5,0]
        run(2)
    boat612.bind('<Button>', gogrt612)
    def gogrt622(event):
        print(event)
        global recentcord
        recentcord = [5,1]
        run(2)
    boat622.bind('<Button>', gogrt622)
    def gogrt632(event):
        print(event)
        global recentcord
        recentcord = [5,2]
        run(2)
    boat632.bind('<Button>', gogrt632)
    def gogrt642(event):
        print(event)
        global recentcord
        recentcord = [5,3]
        run(2)
    boat642.bind('<Button>', gogrt642)
    def gogrt652(event):
        print(event)
        global recentcord
        recentcord = [5,4]
        run(2)
    boat652.bind('<Button>', gogrt652)
    def gogrt662(event):
        print(event)
        global recentcord
        recentcord = [5,5]
        run(2)
    boat662.bind('<Button>', gogrt662)
    def gogrt672(event):
        print(event)
        global recentcord
        recentcord = [5,6]
        run(2)
    boat672.bind('<Button>', gogrt672)
    def gogrt682(event):
        print(event)
        global recentcord
        recentcord = [5,7]
        run(2)
    boat682.bind('<Button>', gogrt682)
    def gogrt692(event):
        print(event)
        global recentcord
        recentcord = [5,8]
        run(2)
    boat692.bind('<Button>', gogrt692)
    def gogrt6102(event):
        print(event)
        global recentcord
        recentcord = [5,9]
        run(2)
    boat6102.bind('<Button>', gogrt6102)
    def gogrt712(event):
        print(event)
        global recentcord
        recentcord = [6,0]
        run(2)
    boat712.bind('<Button>', gogrt712)
    def gogrt722(event):
        print(event)
        global recentcord
        recentcord = [6,1]
        run(2)
    boat722.bind('<Button>', gogrt722)
    def gogrt732(event):
        print(event)
        global recentcord
        recentcord = [6,2]
        run(2)
    boat732.bind('<Button>', gogrt732)
    def gogrt742(event):
        print(event)
        global recentcord
        recentcord = [6,3]
        run(2)
    boat742.bind('<Button>', gogrt742)
    def gogrt752(event):
        print(event)
        global recentcord
        recentcord = [6,4]
        run(2)
    boat752.bind('<Button>', gogrt752)
    def gogrt762(event):
        print(event)
        global recentcord
        recentcord = [6,5]
        run(2)
    boat762.bind('<Button>', gogrt762)
    def gogrt772(event):
        print(event)
        global recentcord
        recentcord = [6,6]
        run(2)
    boat772.bind('<Button>', gogrt772)
    def gogrt782(event):
        print(event)
        global recentcord
        recentcord = [6,7]
        run(2)
    boat782.bind('<Button>', gogrt782)
    def gogrt792(event):
        print(event)
        global recentcord
        recentcord = [6,8]
        run(2)
    boat792.bind('<Button>', gogrt792)
    def gogrt7102(event):
        print(event)
        global recentcord
        recentcord = [6,9]
        run(2)
    boat7102.bind('<Button>', gogrt7102)
    def gogrt812(event):
        print(event)
        global recentcord
        recentcord = [7,0]
        run(2)
    boat812.bind('<Button>', gogrt812)
    def gogrt822(event):
        print(event)
        global recentcord
        recentcord = [7,1]
        run(2)
    boat822.bind('<Button>', gogrt822)
    def gogrt832(event):
        print(event)
        global recentcord
        recentcord = [7,2]
        run(2)
    boat832.bind('<Button>', gogrt832)
    def gogrt842(event):
        print(event)
        global recentcord
        recentcord = [7,3]
        run(2)
    boat842.bind('<Button>', gogrt842)
    def gogrt852(event):
        print(event)
        global recentcord
        recentcord = [7,4]
        run(2)
    boat852.bind('<Button>', gogrt852)
    def gogrt862(event):
        print(event)
        global recentcord
        recentcord = [7,5]
        run(2)
    boat862.bind('<Button>', gogrt862)
    def gogrt872(event):
        print(event)
        global recentcord
        recentcord = [7,6]
        run(2)
    boat872.bind('<Button>', gogrt872)
    def gogrt882(event):
        print(event)
        global recentcord
        recentcord = [7,7]
        run(2)
    boat882.bind('<Button>', gogrt882)
    def gogrt892(event):
        print(event)
        global recentcord
        recentcord = [7,8]
        run(2)
    boat892.bind('<Button>', gogrt892)
    def gogrt8102(event):
        print(event)
        global recentcord
        recentcord = [7,9]
        run(2)
    boat8102.bind('<Button>', gogrt8102)
    def gogrt912(event):
        print(event)
        global recentcord
        recentcord = [8,0]
        run(2)
    boat912.bind('<Button>', gogrt912)
    def gogrt922(event):
        print(event)
        global recentcord
        recentcord = [8,1]
        run(2)
    boat922.bind('<Button>', gogrt922)
    def gogrt932(event):
        print(event)
        global recentcord
        recentcord = [8,2]
        run(2)
    boat932.bind('<Button>', gogrt932)
    def gogrt942(event):
        print(event)
        global recentcord
        recentcord = [8,3]
        run(2)
    boat942.bind('<Button>', gogrt942)
    def gogrt952(event):
        print(event)
        global recentcord
        recentcord = [8,4]
        run(2)
    boat952.bind('<Button>', gogrt952)
    def gogrt962(event):
        print(event)
        global recentcord
        recentcord = [8,5]
        run(2)
    boat962.bind('<Button>', gogrt962)
    def gogrt972(event):
        print(event)
        global recentcord
        recentcord = [8,6]
        run(2)
    boat972.bind('<Button>', gogrt972)
    def gogrt982(event):
        print(event)
        global recentcord
        recentcord = [8,7]
        run(2)
    boat982.bind('<Button>', gogrt982)
    def gogrt992(event):
        print(event)
        global recentcord
        recentcord = [8,8]
        run(2)
    boat992.bind('<Button>', gogrt992)
    def gogrt9102(event):
        print(event)
        global recentcord
        recentcord = [8,9]
        run(2)
    boat9102.bind('<Button>', gogrt9102)
    def gogrt1012(event):
        print(event)
        global recentcord
        recentcord = [9,0]
        run(2)
    boat1012.bind('<Button>', gogrt1012)
    def gogrt1022(event):
        print(event)
        global recentcord
        recentcord = [9,1]
        run(2)
    boat1022.bind('<Button>', gogrt1022)
    def gogrt1032(event):
        print(event)
        global recentcord
        recentcord = [9,2]
        run(2)
    boat1032.bind('<Button>', gogrt1032)
    def gogrt1042(event):
        print(event)
        global recentcord
        recentcord = [9,3]
        run(2)
    boat1042.bind('<Button>', gogrt1042)
    def gogrt1052(event):
        print(event)
        global recentcord
        recentcord = [9,4]
        run(2)
    boat1052.bind('<Button>', gogrt1052)
    def gogrt1062(event):
        print(event)
        global recentcord
        recentcord = [9,5]
        run(2)
    boat1062.bind('<Button>', gogrt1062)
    def gogrt1072(event):
        print(event)
        global recentcord
        recentcord = [9,6]
        run(2)
    boat1072.bind('<Button>', gogrt1072)
    def gogrt1082(event):
        print(event)
        global recentcord
        recentcord = [9,7]
        run(2)
    boat1082.bind('<Button>', gogrt1082)
    def gogrt1092(event):
        print(event)
        global recentcord
        recentcord = [9,8]
        run(2)
    boat1092.bind('<Button>', gogrt1092)
    def gogrt10102(event):
        print(event)
        global recentcord
        recentcord = [9,9]
        run(2)
    boat10102.bind('<Button>', gogrt10102)

    def updateBoard():
        for i in boatB1:
            for I in i:
                if I == [0,0]:
                    boatshow11.set('B ')
                if I == [0,1]:
                    boatshow12.set('B ')
                if I == [0,2]:
                    boatshow13.set('B ')
                if I == [0,3]:
                    boatshow14.set('B ')
                if I == [0,4]:
                    boatshow15.set('B ')
                if I == [0,5]:
                    boatshow16.set('B ')
                if I == [0,6]:
                    boatshow17.set('B ')
                if I == [0,7]:
                    boatshow18.set('B ')
                if I == [0,8]:
                    boatshow19.set('B ')
                if I == [0,9]:
                    boatshow110.set('B ')
                if I == [1,0]:
                    boatshow21.set('B ')
                if I == [1,1]:
                    boatshow22.set('B ')
                if I == [1,2]:
                    boatshow23.set('B ')
                if I == [1,3]:
                    boatshow24.set('B ')
                if I == [1,4]:
                    boatshow25.set('B ')
                if I == [1,5]:
                    boatshow26.set('B ')
                if I == [1,6]:
                    boatshow27.set('B ')
                if I == [1,7]:
                    boatshow28.set('B ')
                if I == [1,8]:
                    boatshow29.set('B ')
                if I == [1,9]:
                    boatshow210.set('B ')
                if I == [2,0]:
                    boatshow31.set('B ')
                if I == [2,1]:
                    boatshow32.set('B ')
                if I == [2,2]:
                    boatshow33.set('B ')
                if I == [2,3]:
                    boatshow34.set('B ')
                if I == [2,4]:
                    boatshow35.set('B ')
                if I == [2,5]:
                    boatshow36.set('B ')
                if I == [2,6]:
                    boatshow37.set('B ')
                if I == [2,7]:
                    boatshow38.set('B ')
                if I == [2,8]:
                    boatshow39.set('B ')
                if I == [2,9]:
                    boatshow310.set('B ')
                if I == [3,0]:
                    boatshow41.set('B ')
                if I == [3,1]:
                    boatshow42.set('B ')
                if I == [3,2]:
                    boatshow43.set('B ')
                if I == [3,3]:
                    boatshow44.set('B ')
                if I == [3,4]:
                    boatshow45.set('B ')
                if I == [3,5]:
                    boatshow46.set('B ')
                if I == [3,6]:
                    boatshow47.set('B ')
                if I == [3,7]:
                    boatshow48.set('B ')
                if I == [3,8]:
                    boatshow49.set('B ')
                if I == [3,9]:
                    boatshow410.set('B ')
                if I == [4,0]:
                    boatshow51.set('B ')
                if I == [4,1]:
                    boatshow52.set('B ')
                if I == [4,2]:
                    boatshow53.set('B ')
                if I == [4,3]:
                    boatshow54.set('B ')
                if I == [4,4]:
                    boatshow55.set('B ')
                if I == [4,5]:
                    boatshow56.set('B ')
                if I == [4,6]:
                    boatshow57.set('B ')
                if I == [4,7]:
                    boatshow58.set('B ')
                if I == [4,8]:
                    boatshow59.set('B ')
                if I == [4,9]:
                    boatshow510.set('B ')
                if I == [5,0]:
                    boatshow61.set('B ')
                if I == [5,1]:
                    boatshow62.set('B ')
                if I == [5,2]:
                    boatshow63.set('B ')
                if I == [5,3]:
                    boatshow64.set('B ')
                if I == [5,4]:
                    boatshow65.set('B ')
                if I == [5,5]:
                    boatshow66.set('B ')
                if I == [5,6]:
                    boatshow67.set('B ')
                if I == [5,7]:
                    boatshow68.set('B ')
                if I == [5,8]:
                    boatshow69.set('B ')
                if I == [5,9]:
                    boatshow610.set('B ')
                if I == [6,0]:
                    boatshow71.set('B ')
                if I == [6,1]:
                    boatshow72.set('B ')
                if I == [6,2]:
                    boatshow73.set('B ')
                if I == [6,3]:
                    boatshow74.set('B ')
                if I == [6,4]:
                    boatshow75.set('B ')
                if I == [6,5]:
                    boatshow76.set('B ')
                if I == [6,6]:
                    boatshow77.set('B ')
                if I == [6,7]:
                    boatshow78.set('B ')
                if I == [6,8]:
                    boatshow79.set('B ')
                if I == [6,9]:
                    boatshow710.set('B ')
                if I == [7,0]:
                    boatshow81.set('B ')
                if I == [7,1]:
                    boatshow82.set('B ')
                if I == [7,2]:
                    boatshow83.set('B ')
                if I == [7,3]:
                    boatshow84.set('B ')
                if I == [7,4]:
                    boatshow85.set('B ')
                if I == [7,5]:
                    boatshow86.set('B ')
                if I == [7,6]:
                    boatshow87.set('B ')
                if I == [7,7]:
                    boatshow88.set('B ')
                if I == [7,8]:
                    boatshow89.set('B ')
                if I == [7,9]:
                    boatshow810.set('B ')
                if I == [8,0]:
                    boatshow91.set('B ')
                if I == [8,1]:
                    boatshow92.set('B ')
                if I == [8,2]:
                    boatshow93.set('B ')
                if I == [8,3]:
                    boatshow94.set('B ')
                if I == [8,4]:
                    boatshow95.set('B ')
                if I == [8,5]:
                    boatshow96.set('B ')
                if I == [8,6]:
                    boatshow97.set('B ')
                if I == [8,7]:
                    boatshow98.set('B ')
                if I == [8,8]:
                    boatshow99.set('B ')
                if I == [8,9]:
                    boatshow910.set('B ')
                if I == [9,0]:
                    boatshow101.set('B ')
                if I == [9,1]:
                    boatshow102.set('B ')
                if I == [9,2]:
                    boatshow103.set('B ')
                if I == [9,3]:
                    boatshow104.set('B ')
                if I == [9,4]:
                    boatshow105.set('B ')
                if I == [9,5]:
                    boatshow106.set('B ')
                if I == [9,6]:
                    boatshow107.set('B ')
                if I == [9,7]:
                    boatshow108.set('B ')
                if I == [9,8]:
                    boatshow109.set('B ')
                if I == [9,9]:
                    boatshow1010.set('B ')
        for I in hitB2:
            if I == [0,0]:
                boatshow112.set('H')
            if I == [0,1]:
                boatshow122.set('H')
            if I == [0,2]:
                boatshow132.set('H')
            if I == [0,3]:
                boatshow142.set('H')
            if I == [0,4]:
                boatshow152.set('H')
            if I == [0,5]:
                boatshow162.set('H')
            if I == [0,6]:
                boatshow172.set('H')
            if I == [0,7]:
                boatshow182.set('H')
            if I == [0,8]:
                boatshow192.set('H')
            if I == [0,9]:
                boatshow1102.set('H')
            if I == [1,0]:
                boatshow212.set('H')
            if I == [1,1]:
                boatshow222.set('H')
            if I == [1,2]:
                boatshow232.set('H')
            if I == [1,3]:
                boatshow242.set('H')
            if I == [1,4]:
                boatshow252.set('H')
            if I == [1,5]:
                boatshow262.set('H')
            if I == [1,6]:
                boatshow272.set('H')
            if I == [1,7]:
                boatshow282.set('H')
            if I == [1,8]:
                boatshow292.set('H')
            if I == [1,9]:
                boatshow2102.set('H')
            if I == [2,0]:
                boatshow312.set('H')
            if I == [2,1]:
                boatshow322.set('H')
            if I == [2,2]:
                boatshow332.set('H')
            if I == [2,3]:
                boatshow342.set('H')
            if I == [2,4]:
                boatshow352.set('H')
            if I == [2,5]:
                boatshow362.set('H')
            if I == [2,6]:
                boatshow372.set('H')
            if I == [2,7]:
                boatshow382.set('H')
            if I == [2,8]:
                boatshow392.set('H')
            if I == [2,9]:
                boatshow3102.set('H')
            if I == [3,0]:
                boatshow412.set('H')
            if I == [3,1]:
                boatshow422.set('H')
            if I == [3,2]:
                boatshow432.set('H')
            if I == [3,3]:
                boatshow442.set('H')
            if I == [3,4]:
                boatshow452.set('H')
            if I == [3,5]:
                boatshow462.set('H')
            if I == [3,6]:
                boatshow472.set('H')
            if I == [3,7]:
                boatshow482.set('H')
            if I == [3,8]:
                boatshow492.set('H')
            if I == [3,9]:
                boatshow4102.set('H')
            if I == [4,0]:
                boatshow512.set('H')
            if I == [4,1]:
                boatshow522.set('H')
            if I == [4,2]:
                boatshow532.set('H')
            if I == [4,3]:
                boatshow542.set('H')
            if I == [4,4]:
                boatshow552.set('H')
            if I == [4,5]:
                boatshow562.set('H')
            if I == [4,6]:
                boatshow572.set('H')
            if I == [4,7]:
                boatshow582.set('H')
            if I == [4,8]:
                boatshow592.set('H')
            if I == [4,9]:
                boatshow5102.set('H')
            if I == [5,0]:
                boatshow612.set('H')
            if I == [5,1]:
                boatshow622.set('H')
            if I == [5,2]:
                boatshow632.set('H')
            if I == [5,3]:
                boatshow642.set('H')
            if I == [5,4]:
                boatshow652.set('H')
            if I == [5,5]:
                boatshow662.set('H')
            if I == [5,6]:
                boatshow672.set('H')
            if I == [5,7]:
                boatshow682.set('H')
            if I == [5,8]:
                boatshow692.set('H')
            if I == [5,9]:
                boatshow6102.set('H')
            if I == [6,0]:
                boatshow712.set('H')
            if I == [6,1]:
                boatshow722.set('H')
            if I == [6,2]:
                boatshow732.set('H')
            if I == [6,3]:
                boatshow742.set('H')
            if I == [6,4]:
                boatshow752.set('H')
            if I == [6,5]:
                boatshow762.set('H')
            if I == [6,6]:
                boatshow772.set('H')
            if I == [6,7]:
                boatshow782.set('H')
            if I == [6,8]:
                boatshow792.set('H')
            if I == [6,9]:
                boatshow7102.set('H')
            if I == [7,0]:
                boatshow812.set('H')
            if I == [7,1]:
                boatshow822.set('H')
            if I == [7,2]:
                boatshow832.set('H')
            if I == [7,3]:
                boatshow842.set('H')
            if I == [7,4]:
                boatshow852.set('H')
            if I == [7,5]:
                boatshow862.set('H')
            if I == [7,6]:
                boatshow872.set('H')
            if I == [7,7]:
                boatshow882.set('H')
            if I == [7,8]:
                boatshow892.set('H')
            if I == [7,9]:
                boatshow8102.set('H')
            if I == [8,0]:
                boatshow912.set('H')
            if I == [8,1]:
                boatshow922.set('H')
            if I == [8,2]:
                boatshow932.set('H')
            if I == [8,3]:
                boatshow942.set('H')
            if I == [8,4]:
                boatshow952.set('H')
            if I == [8,5]:
                boatshow962.set('H')
            if I == [8,6]:
                boatshow972.set('H')
            if I == [8,7]:
                boatshow982.set('H')
            if I == [8,8]:
                boatshow992.set('H')
            if I == [8,9]:
                boatshow9102.set('H')
            if I == [9,0]:
                boatshow1012.set('H')
            if I == [9,1]:
                boatshow1022.set('H')
            if I == [9,2]:
                boatshow1032.set('H')
            if I == [9,3]:
                boatshow1042.set('H')
            if I == [9,4]:
                boatshow1052.set('H')
            if I == [9,5]:
                boatshow1062.set('H')
            if I == [9,6]:
                boatshow1072.set('H')
            if I == [9,7]:
                boatshow1082.set('H')
            if I == [9,8]:
                boatshow1092.set('H')
            if I == [9,9]:
                boatshow10102.set('H')
        for I in missB2:
            if I == [0,0]:
                boatshow112.set('M')
            if I == [0,1]:
                boatshow122.set('M')
            if I == [0,2]:
                boatshow132.set('M')
            if I == [0,3]:
                boatshow142.set('M')
            if I == [0,4]:
                boatshow152.set('M')
            if I == [0,5]:
                boatshow162.set('M')
            if I == [0,6]:
                boatshow172.set('M')
            if I == [0,7]:
                boatshow182.set('M')
            if I == [0,8]:
                boatshow192.set('M')
            if I == [0,9]:
                boatshow1102.set('M')
            if I == [1,0]:
                boatshow212.set('M')
            if I == [1,1]:
                boatshow222.set('M')
            if I == [1,2]:
                boatshow232.set('M')
            if I == [1,3]:
                boatshow242.set('M')
            if I == [1,4]:
                boatshow252.set('M')
            if I == [1,5]:
                boatshow262.set('M')
            if I == [1,6]:
                boatshow272.set('M')
            if I == [1,7]:
                boatshow282.set('M')
            if I == [1,8]:
                boatshow292.set('M')
            if I == [1,9]:
                boatshow2102.set('M')
            if I == [2,0]:
                boatshow312.set('M')
            if I == [2,1]:
                boatshow322.set('M')
            if I == [2,2]:
                boatshow332.set('M')
            if I == [2,3]:
                boatshow342.set('M')
            if I == [2,4]:
                boatshow352.set('M')
            if I == [2,5]:
                boatshow362.set('M')
            if I == [2,6]:
                boatshow372.set('M')
            if I == [2,7]:
                boatshow382.set('M')
            if I == [2,8]:
                boatshow392.set('M')
            if I == [2,9]:
                boatshow3102.set('M')
            if I == [3,0]:
                boatshow412.set('M')
            if I == [3,1]:
                boatshow422.set('M')
            if I == [3,2]:
                boatshow432.set('M')
            if I == [3,3]:
                boatshow442.set('M')
            if I == [3,4]:
                boatshow452.set('M')
            if I == [3,5]:
                boatshow462.set('M')
            if I == [3,6]:
                boatshow472.set('M')
            if I == [3,7]:
                boatshow482.set('M')
            if I == [3,8]:
                boatshow492.set('M')
            if I == [3,9]:
                boatshow4102.set('M')
            if I == [4,0]:
                boatshow512.set('M')
            if I == [4,1]:
                boatshow522.set('M')
            if I == [4,2]:
                boatshow532.set('M')
            if I == [4,3]:
                boatshow542.set('M')
            if I == [4,4]:
                boatshow552.set('M')
            if I == [4,5]:
                boatshow562.set('M')
            if I == [4,6]:
                boatshow572.set('M')
            if I == [4,7]:
                boatshow582.set('M')
            if I == [4,8]:
                boatshow592.set('M')
            if I == [4,9]:
                boatshow5102.set('M')
            if I == [5,0]:
                boatshow612.set('M')
            if I == [5,1]:
                boatshow622.set('M')
            if I == [5,2]:
                boatshow632.set('M')
            if I == [5,3]:
                boatshow642.set('M')
            if I == [5,4]:
                boatshow652.set('M')
            if I == [5,5]:
                boatshow662.set('M')
            if I == [5,6]:
                boatshow672.set('M')
            if I == [5,7]:
                boatshow682.set('M')
            if I == [5,8]:
                boatshow692.set('M')
            if I == [5,9]:
                boatshow6102.set('M')
            if I == [6,0]:
                boatshow712.set('M')
            if I == [6,1]:
                boatshow722.set('M')
            if I == [6,2]:
                boatshow732.set('M')
            if I == [6,3]:
                boatshow742.set('M')
            if I == [6,4]:
                boatshow752.set('M')
            if I == [6,5]:
                boatshow762.set('M')
            if I == [6,6]:
                boatshow772.set('M')
            if I == [6,7]:
                boatshow782.set('M')
            if I == [6,8]:
                boatshow792.set('M')
            if I == [6,9]:
                boatshow7102.set('M')
            if I == [7,0]:
                boatshow812.set('M')
            if I == [7,1]:
                boatshow822.set('M')
            if I == [7,2]:
                boatshow832.set('M')
            if I == [7,3]:
                boatshow842.set('M')
            if I == [7,4]:
                boatshow852.set('M')
            if I == [7,5]:
                boatshow862.set('M')
            if I == [7,6]:
                boatshow872.set('M')
            if I == [7,7]:
                boatshow882.set('M')
            if I == [7,8]:
                boatshow892.set('M')
            if I == [7,9]:
                boatshow8102.set('M')
            if I == [8,0]:
                boatshow912.set('M')
            if I == [8,1]:
                boatshow922.set('M')
            if I == [8,2]:
                boatshow932.set('M')
            if I == [8,3]:
                boatshow942.set('M')
            if I == [8,4]:
                boatshow952.set('M')
            if I == [8,5]:
                boatshow962.set('M')
            if I == [8,6]:
                boatshow972.set('M')
            if I == [8,7]:
                boatshow982.set('M')
            if I == [8,8]:
                boatshow992.set('M')
            if I == [8,9]:
                boatshow9102.set('M')
            if I == [9,0]:
                boatshow1012.set('M')
            if I == [9,1]:
                boatshow1022.set('M')
            if I == [9,2]:
                boatshow1032.set('M')
            if I == [9,3]:
                boatshow1042.set('M')
            if I == [9,4]:
                boatshow1052.set('M')
            if I == [9,5]:
                boatshow1062.set('M')
            if I == [9,6]:
                boatshow1072.set('M')
            if I == [9,7]:
                boatshow1082.set('M')
            if I == [9,8]:
                boatshow1092.set('M')
            if I == [9,9]:
                boatshow10102.set('M')
        for I in hitB1:
            if I == [0,0]:
                boatshow11.set('H')
            if I == [0,1]:
                boatshow12.set('H')
            if I == [0,2]:
                boatshow13.set('H')
            if I == [0,3]:
                boatshow14.set('H')
            if I == [0,4]:
                boatshow15.set('H')
            if I == [0,5]:
                boatshow16.set('H')
            if I == [0,6]:
                boatshow17.set('H')
            if I == [0,7]:
                boatshow18.set('H')
            if I == [0,8]:
                boatshow19.set('H')
            if I == [0,9]:
                boatshow110.set('H')
            if I == [1,0]:
                boatshow21.set('H')
            if I == [1,1]:
                boatshow22.set('H')
            if I == [1,2]:
                boatshow23.set('H')
            if I == [1,3]:
                boatshow24.set('H')
            if I == [1,4]:
                boatshow25.set('H')
            if I == [1,5]:
                boatshow26.set('H')
            if I == [1,6]:
                boatshow27.set('H')
            if I == [1,7]:
                boatshow28.set('H')
            if I == [1,8]:
                boatshow29.set('H')
            if I == [1,9]:
                boatshow210.set('H')
            if I == [2,0]:
                boatshow31.set('H')
            if I == [2,1]:
                boatshow32.set('H')
            if I == [2,2]:
                boatshow33.set('H')
            if I == [2,3]:
                boatshow34.set('H')
            if I == [2,4]:
                boatshow35.set('H')
            if I == [2,5]:
                boatshow36.set('H')
            if I == [2,6]:
                boatshow37.set('H')
            if I == [2,7]:
                boatshow38.set('H')
            if I == [2,8]:
                boatshow39.set('H')
            if I == [2,9]:
                boatshow310.set('H')
            if I == [3,0]:
                boatshow41.set('H')
            if I == [3,1]:
                boatshow42.set('H')
            if I == [3,2]:
                boatshow43.set('H')
            if I == [3,3]:
                boatshow44.set('H')
            if I == [3,4]:
                boatshow45.set('H')
            if I == [3,5]:
                boatshow46.set('H')
            if I == [3,6]:
                boatshow47.set('H')
            if I == [3,7]:
                boatshow48.set('H')
            if I == [3,8]:
                boatshow49.set('H')
            if I == [3,9]:
                boatshow410.set('H')
            if I == [4,0]:
                boatshow51.set('H')
            if I == [4,1]:
                boatshow52.set('H')
            if I == [4,2]:
                boatshow53.set('H')
            if I == [4,3]:
                boatshow54.set('H')
            if I == [4,4]:
                boatshow55.set('H')
            if I == [4,5]:
                boatshow56.set('H')
            if I == [4,6]:
                boatshow57.set('H')
            if I == [4,7]:
                boatshow58.set('H')
            if I == [4,8]:
                boatshow59.set('H')
            if I == [4,9]:
                boatshow510.set('H')
            if I == [5,0]:
                boatshow61.set('H')
            if I == [5,1]:
                boatshow62.set('H')
            if I == [5,2]:
                boatshow63.set('H')
            if I == [5,3]:
                boatshow64.set('H')
            if I == [5,4]:
                boatshow65.set('H')
            if I == [5,5]:
                boatshow66.set('H')
            if I == [5,6]:
                boatshow67.set('H')
            if I == [5,7]:
                boatshow68.set('H')
            if I == [5,8]:
                boatshow69.set('H')
            if I == [5,9]:
                boatshow610.set('H')
            if I == [6,0]:
                boatshow71.set('H')
            if I == [6,1]:
                boatshow72.set('H')
            if I == [6,2]:
                boatshow73.set('H')
            if I == [6,3]:
                boatshow74.set('H')
            if I == [6,4]:
                boatshow75.set('H')
            if I == [6,5]:
                boatshow76.set('H')
            if I == [6,6]:
                boatshow77.set('H')
            if I == [6,7]:
                boatshow78.set('H')
            if I == [6,8]:
                boatshow79.set('H')
            if I == [6,9]:
                boatshow710.set('H')
            if I == [7,0]:
                boatshow81.set('H')
            if I == [7,1]:
                boatshow82.set('H')
            if I == [7,2]:
                boatshow83.set('H')
            if I == [7,3]:
                boatshow84.set('H')
            if I == [7,4]:
                boatshow85.set('H')
            if I == [7,5]:
                boatshow86.set('H')
            if I == [7,6]:
                boatshow87.set('H')
            if I == [7,7]:
                boatshow88.set('H')
            if I == [7,8]:
                boatshow89.set('H')
            if I == [7,9]:
                boatshow810.set('H')
            if I == [8,0]:
                boatshow91.set('H')
            if I == [8,1]:
                boatshow92.set('H')
            if I == [8,2]:
                boatshow93.set('H')
            if I == [8,3]:
                boatshow94.set('H')
            if I == [8,4]:
                boatshow95.set('H')
            if I == [8,5]:
                boatshow96.set('H')
            if I == [8,6]:
                boatshow97.set('H')
            if I == [8,7]:
                boatshow98.set('H')
            if I == [8,8]:
                boatshow99.set('H')
            if I == [8,9]:
                boatshow910.set('H')
            if I == [9,0]:
                boatshow101.set('H')
            if I == [9,1]:
                boatshow102.set('H')
            if I == [9,2]:
                boatshow103.set('H')
            if I == [9,3]:
                boatshow104.set('H')
            if I == [9,4]:
                boatshow105.set('H')
            if I == [9,5]:
                boatshow106.set('H')
            if I == [9,6]:
                boatshow107.set('H')
            if I == [9,7]:
                boatshow108.set('H')
            if I == [9,8]:
                boatshow109.set('H')
            if I == [9,9]:
                boatshow1010.set('H')
        for I in missB1:
            if I == [0,0]:
                boatshow11.set('M')
            if I == [0,1]:
                boatshow12.set('M')
            if I == [0,2]:
                boatshow13.set('M')
            if I == [0,3]:
                boatshow14.set('M')
            if I == [0,4]:
                boatshow15.set('M')
            if I == [0,5]:
                boatshow16.set('M')
            if I == [0,6]:
                boatshow17.set('M')
            if I == [0,7]:
                boatshow18.set('M')
            if I == [0,8]:
                boatshow19.set('M')
            if I == [0,9]:
                boatshow110.set('M')
            if I == [1,0]:
                boatshow21.set('M')
            if I == [1,1]:
                boatshow22.set('M')
            if I == [1,2]:
                boatshow23.set('M')
            if I == [1,3]:
                boatshow24.set('M')
            if I == [1,4]:
                boatshow25.set('M')
            if I == [1,5]:
                boatshow26.set('M')
            if I == [1,6]:
                boatshow27.set('M')
            if I == [1,7]:
                boatshow28.set('M')
            if I == [1,8]:
                boatshow29.set('M')
            if I == [1,9]:
                boatshow210.set('M')
            if I == [2,0]:
                boatshow31.set('M')
            if I == [2,1]:
                boatshow32.set('M')
            if I == [2,2]:
                boatshow33.set('M')
            if I == [2,3]:
                boatshow34.set('M')
            if I == [2,4]:
                boatshow35.set('M')
            if I == [2,5]:
                boatshow36.set('M')
            if I == [2,6]:
                boatshow37.set('M')
            if I == [2,7]:
                boatshow38.set('M')
            if I == [2,8]:
                boatshow39.set('M')
            if I == [2,9]:
                boatshow310.set('M')
            if I == [3,0]:
                boatshow41.set('M')
            if I == [3,1]:
                boatshow42.set('M')
            if I == [3,2]:
                boatshow43.set('M')
            if I == [3,3]:
                boatshow44.set('M')
            if I == [3,4]:
                boatshow45.set('M')
            if I == [3,5]:
                boatshow46.set('M')
            if I == [3,6]:
                boatshow47.set('M')
            if I == [3,7]:
                boatshow48.set('M')
            if I == [3,8]:
                boatshow49.set('M')
            if I == [3,9]:
                boatshow410.set('M')
            if I == [4,0]:
                boatshow51.set('M')
            if I == [4,1]:
                boatshow52.set('M')
            if I == [4,2]:
                boatshow53.set('M')
            if I == [4,3]:
                boatshow54.set('M')
            if I == [4,4]:
                boatshow55.set('M')
            if I == [4,5]:
                boatshow56.set('M')
            if I == [4,6]:
                boatshow57.set('M')
            if I == [4,7]:
                boatshow58.set('M')
            if I == [4,8]:
                boatshow59.set('M')
            if I == [4,9]:
                boatshow510.set('M')
            if I == [5,0]:
                boatshow61.set('M')
            if I == [5,1]:
                boatshow62.set('M')
            if I == [5,2]:
                boatshow63.set('M')
            if I == [5,3]:
                boatshow64.set('M')
            if I == [5,4]:
                boatshow65.set('M')
            if I == [5,5]:
                boatshow66.set('M')
            if I == [5,6]:
                boatshow67.set('M')
            if I == [5,7]:
                boatshow68.set('M')
            if I == [5,8]:
                boatshow69.set('M')
            if I == [5,9]:
                boatshow610.set('M')
            if I == [6,0]:
                boatshow71.set('M')
            if I == [6,1]:
                boatshow72.set('M')
            if I == [6,2]:
                boatshow73.set('M')
            if I == [6,3]:
                boatshow74.set('M')
            if I == [6,4]:
                boatshow75.set('M')
            if I == [6,5]:
                boatshow76.set('M')
            if I == [6,6]:
                boatshow77.set('M')
            if I == [6,7]:
                boatshow78.set('M')
            if I == [6,8]:
                boatshow79.set('M')
            if I == [6,9]:
                boatshow710.set('M')
            if I == [7,0]:
                boatshow81.set('M')
            if I == [7,1]:
                boatshow82.set('M')
            if I == [7,2]:
                boatshow83.set('M')
            if I == [7,3]:
                boatshow84.set('M')
            if I == [7,4]:
                boatshow85.set('M')
            if I == [7,5]:
                boatshow86.set('M')
            if I == [7,6]:
                boatshow87.set('M')
            if I == [7,7]:
                boatshow88.set('M')
            if I == [7,8]:
                boatshow89.set('M')
            if I == [7,9]:
                boatshow810.set('M')
            if I == [8,0]:
                boatshow91.set('M')
            if I == [8,1]:
                boatshow92.set('M')
            if I == [8,2]:
                boatshow93.set('M')
            if I == [8,3]:
                boatshow94.set('M')
            if I == [8,4]:
                boatshow95.set('M')
            if I == [8,5]:
                boatshow96.set('M')
            if I == [8,6]:
                boatshow97.set('M')
            if I == [8,7]:
                boatshow98.set('M')
            if I == [8,8]:
                boatshow99.set('M')
            if I == [8,9]:
                boatshow910.set('M')
            if I == [9,0]:
                boatshow101.set('M')
            if I == [9,1]:
                boatshow102.set('M')
            if I == [9,2]:
                boatshow103.set('M')
            if I == [9,3]:
                boatshow104.set('M')
            if I == [9,4]:
                boatshow105.set('M')
            if I == [9,5]:
                boatshow106.set('M')
            if I == [9,6]:
                boatshow107.set('M')
            if I == [9,7]:
                boatshow108.set('M')
            if I == [9,8]:
                boatshow109.set('M')
            if I == [9,9]:
                boatshow1010.set('M')

    def boatHere(cheek):
        for i in cheek:
            if i == [0,0]:
                if boatshow11.get() == 'B ':
                    return False
            if i == [0,1]:
                if boatshow12.get() == 'B ':
                    return False
            if i == [0,2]:
                if boatshow13.get() == 'B ':
                    return False
            if i == [0,3]:
                if boatshow14.get() == 'B ':
                    return False
            if i == [0,4]:
                if boatshow15.get() == 'B ':
                    return False
            if i == [0,5]:
                if boatshow16.get() == 'B ':
                    return False
            if i == [0,6]:
                if boatshow17.get() == 'B ':
                    return False
            if i == [0,7]:
                if boatshow18.get() == 'B ':
                    return False
            if i == [0,8]:
                if boatshow19.get() == 'B ':
                    return False
            if i == [0,9]:
                if boatshow110.get() == 'B ':
                    return False
            if i == [1,0]:
                if boatshow21.get() == 'B ':
                    return False
            if i == [1,1]:
                if boatshow22.get() == 'B ':
                    return False
            if i == [1,2]:
                if boatshow23.get() == 'B ':
                    return False
            if i == [1,3]:
                if boatshow24.get() == 'B ':
                    return False
            if i == [1,4]:
                if boatshow25.get() == 'B ':
                    return False
            if i == [1,5]:
                if boatshow26.get() == 'B ':
                    return False
            if i == [1,6]:
                if boatshow27.get() == 'B ':
                    return False
            if i == [1,7]:
                if boatshow28.get() == 'B ':
                    return False
            if i == [1,8]:
                if boatshow29.get() == 'B ':
                    return False
            if i == [1,9]:
                if boatshow210.get() == 'B ':
                    return False
            if i == [2,0]:
                if boatshow31.get() == 'B ':
                    return False
            if i == [2,1]:
                if boatshow32.get() == 'B ':
                    return False
            if i == [2,2]:
                if boatshow33.get() == 'B ':
                    return False
            if i == [2,3]:
                if boatshow34.get() == 'B ':
                    return False
            if i == [2,4]:
                if boatshow35.get() == 'B ':
                    return False
            if i == [2,5]:
                if boatshow36.get() == 'B ':
                    return False
            if i == [2,6]:
                if boatshow37.get() == 'B ':
                    return False
            if i == [2,7]:
                if boatshow38.get() == 'B ':
                    return False
            if i == [2,8]:
                if boatshow39.get() == 'B ':
                    return False
            if i == [2,9]:
                if boatshow310.get() == 'B ':
                    return False
            if i == [3,0]:
                if boatshow41.get() == 'B ':
                    return False
            if i == [3,1]:
                if boatshow42.get() == 'B ':
                    return False
            if i == [3,2]:
                if boatshow43.get() == 'B ':
                    return False
            if i == [3,3]:
                if boatshow44.get() == 'B ':
                    return False
            if i == [3,4]:
                if boatshow45.get() == 'B ':
                    return False
            if i == [3,5]:
                if boatshow46.get() == 'B ':
                    return False
            if i == [3,6]:
                if boatshow47.get() == 'B ':
                    return False
            if i == [3,7]:
                if boatshow48.get() == 'B ':
                    return False
            if i == [3,8]:
                if boatshow49.get() == 'B ':
                    return False
            if i == [3,9]:
                if boatshow410.get() == 'B ':
                    return False
            if i == [4,0]:
                if boatshow51.get() == 'B ':
                    return False
            if i == [4,1]:
                if boatshow52.get() == 'B ':
                    return False
            if i == [4,2]:
                if boatshow53.get() == 'B ':
                    return False
            if i == [4,3]:
                if boatshow54.get() == 'B ':
                    return False
            if i == [4,4]:
                if boatshow55.get() == 'B ':
                    return False
            if i == [4,5]:
                if boatshow56.get() == 'B ':
                    return False
            if i == [4,6]:
                if boatshow57.get() == 'B ':
                    return False
            if i == [4,7]:
                if boatshow58.get() == 'B ':
                    return False
            if i == [4,8]:
                if boatshow59.get() == 'B ':
                    return False
            if i == [4,9]:
                if boatshow510.get() == 'B ':
                    return False
            if i == [5,0]:
                if boatshow61.get() == 'B ':
                    return False
            if i == [5,1]:
                if boatshow62.get() == 'B ':
                    return False
            if i == [5,2]:
                if boatshow63.get() == 'B ':
                    return False
            if i == [5,3]:
                if boatshow64.get() == 'B ':
                    return False
            if i == [5,4]:
                if boatshow65.get() == 'B ':
                    return False
            if i == [5,5]:
                if boatshow66.get() == 'B ':
                    return False
            if i == [5,6]:
                if boatshow67.get() == 'B ':
                    return False
            if i == [5,7]:
                if boatshow68.get() == 'B ':
                    return False
            if i == [5,8]:
                if boatshow69.get() == 'B ':
                    return False
            if i == [5,9]:
                if boatshow610.get() == 'B ':
                    return False
            if i == [6,0]:
                if boatshow71.get() == 'B ':
                    return False
            if i == [6,1]:
                if boatshow72.get() == 'B ':
                    return False
            if i == [6,2]:
                if boatshow73.get() == 'B ':
                    return False
            if i == [6,3]:
                if boatshow74.get() == 'B ':
                    return False
            if i == [6,4]:
                if boatshow75.get() == 'B ':
                    return False
            if i == [6,5]:
                if boatshow76.get() == 'B ':
                    return False
            if i == [6,6]:
                if boatshow77.get() == 'B ':
                    return False
            if i == [6,7]:
                if boatshow78.get() == 'B ':
                    return False
            if i == [6,8]:
                if boatshow79.get() == 'B ':
                    return False
            if i == [6,9]:
                if boatshow710.get() == 'B ':
                    return False
            if i == [7,0]:
                if boatshow81.get() == 'B ':
                    return False
            if i == [7,1]:
                if boatshow82.get() == 'B ':
                    return False
            if i == [7,2]:
                if boatshow83.get() == 'B ':
                    return False
            if i == [7,3]:
                if boatshow84.get() == 'B ':
                    return False
            if i == [7,4]:
                if boatshow85.get() == 'B ':
                    return False
            if i == [7,5]:
                if boatshow86.get() == 'B ':
                    return False
            if i == [7,6]:
                if boatshow87.get() == 'B ':
                    return False
            if i == [7,7]:
                if boatshow88.get() == 'B ':
                    return False
            if i == [7,8]:
                if boatshow89.get() == 'B ':
                    return False
            if i == [7,9]:
                if boatshow810.get() == 'B ':
                    return False
            if i == [8,0]:
                if boatshow91.get() == 'B ':
                    return False
            if i == [8,1]:
                if boatshow92.get() == 'B ':
                    return False
            if i == [8,2]:
                if boatshow93.get() == 'B ':
                    return False
            if i == [8,3]:
                if boatshow94.get() == 'B ':
                    return False
            if i == [8,4]:
                if boatshow95.get() == 'B ':
                    return False
            if i == [8,5]:
                if boatshow96.get() == 'B ':
                    return False
            if i == [8,6]:
                if boatshow97.get() == 'B ':
                    return False
            if i == [8,7]:
                if boatshow98.get() == 'B ':
                    return False
            if i == [8,8]:
                if boatshow99.get() == 'B ':
                    return False
            if i == [8,9]:
                if boatshow910.get() == 'B ':
                    return False
            if i == [9,0]:
                if boatshow101.get() == 'B ':
                    return False
            if i == [9,1]:
                if boatshow102.get() == 'B ':
                    return False
            if i == [9,2]:
                if boatshow103.get() == 'B ':
                    return False
            if i == [9,3]:
                if boatshow104.get() == 'B ':
                    return False
            if i == [9,4]:
                if boatshow105.get() == 'B ':
                    return False
            if i == [9,5]:
                if boatshow106.get() == 'B ':
                    return False
            if i == [9,6]:
                if boatshow107.get() == 'B ':
                    return False
            if i == [9,7]:
                if boatshow108.get() == 'B ':
                    return False
            if i == [9,8]:
                if boatshow109.get() == 'B ':
                    return False
            if i == [9,9]:
                if boatshow1010.get() == 'B ':
                    return False
        else:
            return True

    window.mainloop()

if __name__ == "__main__":
    g()
#!python3

import x01_map, x02_convert, x03_create, x04_checkConflicts, time

boatB1 = []
hitB1 = []
missB1 = []
boatB2 = []
hitB2 = []
missB2 = []
letters = ('a','A','b','B','c','C','d','D','e','E','f','F','g','G','h','H','i','I','j','J')
numbers = ('1','2','3','4','5','6','7','8','9','10')

def setup():
    for i in range(5):
        newboat = x03_create.create(i)
        boatB1.append(x04_checkConflicts.fullList(newboat,boatB1))
    for i in range(5):
        newboat = x03_create.create(i,False)
        boatB2.append(x04_checkConflicts.fullList(newboat,boatB2,False))
    x01_map.show2Boards(boatB1, [])

def test():
    for i in range(5):
        newboat = x03_create.create(i,False)
        boatB1.append(x04_checkConflicts.fullList(newboat,boatB1,False))
    for i in range(5):
        newboat = x03_create.create(i,False)
        boatB2.append(x04_checkConflicts.fullList(newboat,boatB2,False))
    x01_map.show2Boards(boatB1, [])

def fire(player,notai=True):
    if notai:
        while True:
                loc = input(f"Enter cauordenets: ")
                try:
                    cord = x02_convert.convert(loc)
                    if (cord not in boatB1) and (cord not in hitB1):
                        break
                except:
                    print("Invalade cords")
                    x01_map.show2Boards(boatB1, [], hitB1, missB1, hitB2, missB2)
        if player == 1:
            for i in boatB2:
                if cord in i:
                    hitB2.append(cord)
                    i.remove(cord)
                    return 'Hit'
            else:
                missB2.append(cord)
                return 'Miss'
        elif player == 2:
            while True:
                loc = input(f"Enter cauordenets: ")
                try:
                    cord = x02_convert.convert(loc)
                    if (cord not in boatB1) and (cord not in hitB1):
                        break
                except:
                    print("Invalade cords")
                    x01_map.show2Boards(boatB1, [], hitB1, missB1, hitB2, missB2)
            for i in boatB1:
                if cord in i:
                    hitB1.append(cord)
                    i.remove(cord)
                    return 'Hit'
            else:
                missB1.append(cord)
                return 'Miss'
    else:
        if player == 1:
            while True:
                cord = x02_convert.aicord(notai)
                if cord not in hitB2 and cord not in missB2:
                    break
            for i in boatB2:
                if cord in i:
                    hitB2.append(cord)
                    i.remove(cord)
                    return f'Hit! {x02_convert.convert(cord)}'
            else:
                missB2.append(cord)
                return f'Miss! {x02_convert.convert(cord)}'
        elif player == 2:
            while True:
                cord = x02_convert.aicord(notai)
                if cord not in hitB1 and cord not in missB1:
                    break
            for i in boatB1:
                if cord in i:
                    hitB1.append(cord)
                    i.remove(cord)
                    return f'Hit! {x02_convert.convert(cord)}'
            else:
                missB1.append(cord)
                return f'Miss! {x02_convert.convert(cord)}'

def Cleanup():
    for i in boatB1:
        if i == []:
            boatB1.remove(i)
    for i in boatB2:
        if i == []:
            boatB2.remove(i)
    if boatB1 == []:
        return 'Player 1'
    elif boatB2 == []:
        return 'Player 2'
    else:
        return None

def gameLoop():
    while True:
        hit = fire(1)
        x01_map.showBoard(hit = hitB2, miss = missB2)
        print(hit,end='')
        time.sleep(1)
        hit = fire(2,False)
        x01_map.showBoard(boatB1,hitB1,missB1)
        print(hit,end='')
        time.sleep(1)
        x01_map.show2Boards(boatB1, [], hitB1, missB1, hitB2, missB2)
        if Cleanup() != None:
            break
    print(f"\n{Cleanup()} is the Winner!")

if __name__ == "__main__":
    setup()
    #test()
    gameLoop()
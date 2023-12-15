#!python3

import x01_map, x02_convert, x03_create, x04_checkConflicts, time

boatB1 = [['','']]
hitB1 = [['','']]
missB1 = [['','']]
boatB2 = [['','']]
hitB2 = [['','']]
missB2 = [['','']]

def setup():
    for i in range(5):
        x01_map.showBoard(boatB1)
        newboat = x03_create.create(i,boatB1)
        boatB1.append(x04_checkConflicts.fullList(newboat,boatB1))
    for i in range(5):
        newboat = x03_create.create(i,[],False)
        boatB2.append(x04_checkConflicts.fullList(newboat,boatB2,False))

def test():
    for i in range(5):
        newboat = x03_create.create(i,[],False)
        boatB1.append(x04_checkConflicts.fullList(newboat,boatB1,False))
    for i in range(5):
        newboat = x03_create.create(i,[],False)
        boatB2.append(x04_checkConflicts.fullList(newboat,boatB2,False))

def fire(player,notai=True):
    if notai:
        if player == 1:
            while True:
                loc = input(f"Enter cauordenets: ")
                try:
                    cord = x02_convert.convert(loc)
                    if (cord not in missB2) and (cord not in hitB2):
                        break
                except:
                    x01_map.show2Boards([], boatB1, hitB2, missB2, hitB1, missB1)
                    print("Invalade cords")
                else:
                    x01_map.show2Boards([], boatB1, hitB2, missB2, hitB1, missB1)
                    print("Invalade cords")
            for i in boatB2:
                if cord in i:
                    hitB2.append(cord)
                    i.remove(cord)
                    return f'Hit {x02_convert.convert(cord)}'
            else:
                missB2.append(cord)
                return f'Miss {x02_convert.convert(cord)}'
        elif player == 2:
            while True:
                loc = input(f"Enter cauordenets: ")
                try:
                    cord = x02_convert.convert(loc)
                    if (cord not in missB1) and (cord not in hitB1):
                        break
                except:
                    x01_map.show2Boards([], boatB1, hitB2, missB2, hitB1, missB1)
                    print("Invalade cords")
                else:
                    x01_map.show2Boards([], boatB1, hitB2, missB2, hitB1, missB1)
                    print("Invalade cords")
            for i in boatB1:
                if cord in i:
                    hitB1.append(cord)
                    i.remove(cord)
                    return f'Hit {x02_convert.convert(cord)}'
            else:
                missB1.append(cord)
                return f'Miss {x02_convert.convert(cord)}'
    else:
        if player == 1:
            while True:
                cord = x02_convert.aicord(notai,hitB2,missB2)
                if cord not in hitB2:
                    break
            for i in boatB2:
                if cord in i:
                    hitB2.append(cord)
                    i.remove(cord)
                    return f'Hit {x02_convert.convert(cord)}'
            else:
                missB2.append(cord)
                return f'Miss {x02_convert.convert(cord)}'
        elif player == 2:
            while True:
                cord = x02_convert.aicord(notai,hitB1,missB1)
                if cord not in hitB1:
                    break
            for i in boatB1:
                if cord in i:
                    hitB1.append(cord)
                    i.remove(cord)
                    return f'Hit {x02_convert.convert(cord)}'
            else:
                missB1.append(cord)
                return f'Miss {x02_convert.convert(cord)}'

def Cleanup():
    for i in boatB1:
        if i == []:
            boatB1.remove(i)
    for i in boatB2:
        if i == []:
            boatB2.remove(i)
    if boatB2 == [['','']]:
        return 'Player 1'
    elif boatB1 == [['','']]:
        return 'Player 2'
    else:
        return None

def gameLoop():
    re = 0
    while True:
        x01_map.show2Boards([], boatB1, hitB2, missB2, hitB1, missB1)
        hit = fire(1,False)
        x01_map.showBoard(hit = hitB2, miss = missB2)
        #x01_map.showBoard(boatB2,hitB2,missB2)
        print(hit)
        time.sleep(1)
        if Cleanup() != None:
            break
        hit = fire(2,False)
        x01_map.showBoard(boatB1,hitB1,missB1)
        print(hit)
        time.sleep(1)
        if Cleanup() != None:
            break
        re = re + 1
    print(f"\n{Cleanup()} is the Winner!", re)

if __name__ == "__main__":
    #test()
    setup()
    gameLoop()
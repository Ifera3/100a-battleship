#!python3

import x01_map, x02_convert, x03_create, x04_checkConflicts

ocupiedB1 = []
ocupiedB2 = []

def setup():
    for i in range(5):
        newboat = x03_create.aiCreate(i)
        ocupiedB2.append(x04_checkConflicts.fullList(newboat,ocupiedB1,False))
    for i in range(5):
        newboat = x03_create.create(i)
        ocupiedB1.append(x04_checkConflicts.fullList(newboat,ocupiedB1))
    x01_map.showBoard(ocupiedB2)
    x01_map.showBoard(ocupiedB1)

def test():
    for i in range(5):
        newboat = x03_create.aiCreate(i)
        ocupiedB2.append(x04_checkConflicts.fullList(newboat,ocupiedB1,False))
    for i in range(5):
        newboat = x03_create.aiCreate(i)
        ocupiedB1.append(x04_checkConflicts.fullList(newboat,ocupiedB1,False))
    x01_map.show2Boards(ocupiedB1, ocupiedB2)


if __name__ == "__main__":
    test()
#! python3

"""
* Take a list of coordinates and draw a map showing occupied squares
* The map is a 10x10 grid
* (0,0) is the coordinate in the bottom left (like a regular (x,y) grid system)

Sample Data1:
[[1, 1], [2, 1], [4, 0], [5, 0], [6, 0], [0, 1], [0, 2], [0, 3], [1, 8], [2, 8], [3, 8], [4, 8], [4, 3], [4, 4], [4, 5], [4, 6], [4, 7]]

Suggested Output:
..........
.xxxx.....
....x.....
....x.....
....x.....
....x.....
x...x.....
x.........
xxx.......
....xxx...

Sample Data2:
[[0, 0], [1, 0], [8, 6], [8, 7], [8, 8], [7, 5], [7, 6], [7, 7], [1, 1], [1, 2], [1, 3], [1, 4], [0, 6], [1, 6], [2, 6], [3, 6], [4, 6]]

..........
........x.
.......xx.
xxxxx..xx.
.......x..
.x........
.x........
.x........
.x........
xx........
"""

def showBoard(occupied=[],hit=[],miss=[]):
    cawordents = []
    board = []
    for I in range(10):
        for i in range(10):
            cawordents.append([i,I])
            board.append('.  ')
    for i in cawordents:
        for I in occupied:
            if i in I:
                board[cawordents.index(i)] = '[] '
        if i in hit:
                board[cawordents.index(i)] = 'X  '
        if i in miss:
                board[cawordents.index(i)] = 'O  '
    num = "10 | "
    p = "\n    _______________________________\n"
    for I in range(10):
        p = p + num
        for i in range(10):
            square = ((9 - I)*10) + i
            p = p + board[square]
        num = f"0{9 - I} | "
        p = p + f"|\n"
    p = p + "   |_______________________________|\n     "
    for i in range(10):
        letter = ('A  ','B  ','C  ','D  ','E  ','F  ','G  ','H  ','I  ','J  ')
        p = p + letter[i]
    print(p)

def show2Boards(occupied1,occupied2,hit1=[],miss1=[],hit2=[],miss2=[]):
    cawordents = []
    board1 = []
    board2 = []
    for I in range(10):
        for i in range(10):
            cawordents.append([i,I])
            board1.append('.  ')
            board2.append('.  ')
    for i in cawordents:
        for I in occupied1:
            if i in I:
                board1[cawordents.index(i)] = '[] '
        if i in hit1:
                board1[cawordents.index(i)] = 'X  '
        if i in miss1:
                board1[cawordents.index(i)] = 'O  '
        for I in occupied2:
            if i in I:
                board2[cawordents.index(i)] = '[] '
        if i in hit2:
                board2[cawordents.index(i)] = 'X  '
        if i in miss2:
                board2[cawordents.index(i)] = 'O  '
    num = "10 | "
    p = "\n    _______________________________           _______________________________\n"
    for I in range(10):
        p = p + num
        for i in range(10):
            square = ((9 - I)*10) + i
            p = p + board1[square]
        p = p + f"|      {num}"
        for i in range(10):
            square = ((9 - I)*10) + i
            p = p + board2[square]
        num = f"0{9 - I} | "
        p = p + '|\n'
    p = p + "   |_______________________________|         |_______________________________|\n     "
    for i in range(10):
        letter = ('A  ','B  ','C  ','D  ','E  ','F  ','G  ','H  ','I  ','J  ')
        p = p + letter[i]
    p = p + f"            "
    for i in range(10):
        letter = ('A  ','B  ','C  ','D  ','E  ','F  ','G  ','H  ','I  ','J  ')
        p = p + letter[i]
    print(p)

if __name__ == "__main__":
    occupied = [[[1, 1], [2, 1]], [[4, 0], [5, 0], [6, 0]], [[0, 1], [0, 2], [0, 3]], [[1, 8], [2, 8], [3, 8], [4, 8]], [[4, 3], [4, 4], [4, 5], [4, 6], [4, 7]]]
    showBoard(occupied)
    show2Boards(occupied, occupied)
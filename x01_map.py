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


def showBoard(occupied):
    cawordents = []
    board = []
    for I in range(10):
        for i in range(10):
            cawordents.append([i,I])
    print(cawordents)
    for i in cawordents:
        if i in occupied:
            board.append('X ')
        else:
            board.append('. ')
    print(board)
    p = ""
    for I in range(10):
        p = p + "\n"
        for i in range(10):
            square = ((9 - I)*10) + i
            p = p + board[square]
    print(p)

if __name__ == "__main__":
    occupied = [[1, 1], [2, 1], [4, 0], [5, 0], [6, 0], [0, 1], [0, 2], [0, 3], [1, 8], [2, 8], [3, 8], [4, 8], [4, 3], [4, 4], [4, 5], [4, 6], [4, 7]]
    showBoard(occupied)
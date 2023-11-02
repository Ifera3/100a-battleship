#!python3
'''
There are 5 boats in battleship. They must occupy coordinates that are horizontal or vertical only (no diagonals). 
The size of the boats are 2, 3, 3, 4 and 5. Create a function that generates a list of the data for your boats.
'''
import random, x02_convert

boatDatat = (('tugboat',2),('sumbarine',3),('destroyer',3),('battelship',4),('carrier',5))

def create(boat):
  yes = 0
  letters = ('a','A','b','B','c','C','d','D','e','E','f','F','g','G','h','H','i','I','j','J')
  numbers = ('1','2','3','4','5','6','7','8','9','10')
  directions = ('up','down','left','right')
  while yes == 0:
    loc = input(f"enter boat cauordenetsfor {boatDatat[boat][0]}(eg: A1(min),g6,J 10(max)): ")
    for i in letters:
      for I in numbers:
        if f"{i}{I}" == loc:
          yes = 1
        elif f"{i} {I}" == loc:
          yes = 1
  while yes == 1:
    direc = input(f"enter direction of the {boatDatat[boat][0]}(eg: up, down, left, right): ")
    for i in directions:
      if direc == i:
        yes = 2
  xy = x02_convert.convert(loc)
  boatCords = [xy,direc,boat]
  print(boatCords)
  return boatCords  
  
def aiCreate(boat):
  letters = ('a','A','b','B','c','C','d','D','e','E','f','F','g','G','h','H','i','I','j','J')
  numbers = ('1','2','3','4','5','6','7','8','9','10')
  directions = ('up','down','left','right')
  loc = f"{letters[random.randrange(len(letters))]}{numbers[random.randrange(len(numbers))]}"
  print(loc)
  direc = directions[random.randrange(len(directions))]
  xy = x02_convert.convert(loc)
  boatCords = [xy,direc,boat]
  print(boatCords)
  return boatCords

if __name__ == "__main__":
  x = create(0)
  print(x)
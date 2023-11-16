#!python3
'''
There are 5 boats in battleship. They must occupy coordinates that are horizontal or vertical only (no diagonals). 
The size of the boats are 2, 3, 3, 4 and 5. Create a function that generates a list of the data for your boats.
'''
import random, x02_convert

boatDatat = (('tugboat',2),('sumbarine',3),('destroyer',3),('battelship',4),('carrier',5))

def create(boat,notai=True):
  directions = ('up','down','left','right')
  if notai:
    while True:
      loc = input(f"enter boat cauordenetsfor {boatDatat[boat][0]}(eg: A1(min),g6,J 10(max)): ")
      try:
        xy = x02_convert.convert(loc)
        break
      except:
        print("invalade cawordenets")
    while True:
      direc = input(f"enter direction of the {boatDatat[boat][0]}(eg: up, down, left, right): ")
      if direc in directions:
        break
    boatCords = [xy,direc,boat]
    #print(boatCords)
    return boatCords  
  else:
    xy = x02_convert.aicord(notai)
    direc = directions[random.randrange(len(directions))]
    boatCords = [xy,direc,boat]
    return boatCords

if __name__ == "__main__":
  x = create(0)
  print(x)
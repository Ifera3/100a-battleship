#!python3
'''
There are 5 boats in battleship. They must occupy coordinates that are horizontal or vertical only (no diagonals). 
The size of the boats are 2, 3, 3, 4 and 5. Create a function that generates a list of the data for your boats.
'''
import random, x02_convert, x01_map, math

boatDatat = (('tugboat',2),('sumbarine',3),('destroyer',3),('battelship',4),('carrier',5))

def create(boat,bord,notai=True):
  directions = ('up','Up','u','U','north','North','n','N','down','Down','d','D','south','South','s','S','left','Left','l','L','west','West','w','W','right','Right','r','R','east','East','e','E')
  if notai:
    while True:
      loc = input(f"Enter boat cauordenets for the {boatDatat[boat][0]}: ")
      try:
        xy = x02_convert.convert(loc)
        break
      except:
        print("Invalade cwordenets")
    bord.append([xy])
    while True:
      x01_map.showBoard(bord)
      direc = input(f"Enter direction of the {boatDatat[boat][0]}: ")
      if direc in directions:
        direc = (directions.index(direc)+1)/8
        break
    bord.remove([xy])
    boatCords = [xy,direc,boat]
    #print(boatCords)
    return boatCords  
  else:
    xy = x02_convert.aicord(notai,[],[])
    direc = random.randrange(5)
    boatCords = [xy,direc,boat]
    return boatCords

if __name__ == "__main__":
  x = create(0)
  print(x)
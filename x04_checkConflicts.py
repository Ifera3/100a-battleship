#!python3

'''
##### 4. Check for conflicts
It is not possible for a boat to occupy the same space as another boat.  
We would need to add a tool to check to see if a boat that we are trying 
to place is overlapping with another boat, so that if it is, we can re-create it.

One strategy:
Create a function that converts all existing boats to a list of coordinates and add them to
a list of "occupied" squares
Check each of your new ship squares to see if there is a conflict
The two functions that have been created here might be helpful
'''
import x03_create, x02_convert

boatDatat = x03_create.boatDatat

def fullList(ships,ocupied,notai = True):
  '''
  inputs:
  ships: list of all current/valid ship data
  
  return:
  list of occupied coordinates
  (example: [ [0,2] , [0,3] , [1,4] , [2,4] , [3,4] ])
  '''
  boat = ships[2]
  boatsquare = [ships[0]]
  print(ships[1])
  if ships[1] <= 1:
    for i in range(boatDatat[boat][1] - 1):
      c = [boatsquare[-1][0],boatsquare[-1][1] + 1]
      boatsquare.append(c)
  elif ships[1] <= 2:
    for i in range(boatDatat[boat][1] - 1):
      c = [boatsquare[-1][0],boatsquare[-1][1] - 1]
      boatsquare.append(c)
  elif ships[1] <= 3:
    for i in range(boatDatat[boat][1] - 1):
      c = [boatsquare[-1][0] - 1,boatsquare[-1][1]]
      boatsquare.append(c)
  elif ships[1] <= 4:
    for i in range(boatDatat[boat][1] - 1):
      c = [boatsquare[-1][0] + 1,boatsquare[-1][1]]
      boatsquare.append(c)
  else:
    ships = x03_create.create(boat,ocupied,notai)
    boatsquare = fullList(ships,ocupied,notai)
  if isConflict(boatsquare,ocupied,notai):
    ships = x03_create.create(boat,ocupied,notai)
    boatsquare = fullList(ships,ocupied,notai)
  return boatsquare

def isConflict(shipSquares,ocupied,notai):
  '''
  inputs:
  occupied: list of all occupied squares
  boat: dictionary with information about your boat you are checking
  
  return: 
  True if the new boat conflicts with existing data
  False if the new boat does not conflict
  '''
  ValueAccept = [0,1,2,3,4,5,6,7,8,9]
  for i in shipSquares:
    if i[0] not in ValueAccept:
      if notai:
        print("Cawordenets out of rane")
      return True
    elif i[1] not in ValueAccept:
      if notai:
        print("Cawordenets out of rane")
      return True
    for O in ocupied:
      if i in O:
        if notai:
          print(f"boat already at {x02_convert.convert(i)}")
        return True
  else:
    return False

'''if __name__ == "__main__":
  ocupied = [[[0, 0], [0, 1]], [[9, 9], [8, 9], [7, 9]], [[2, 9], [3, 9], [4, 9]], [[0, 9], [0, 8], [0, 7], [0, 6]]]
  newBoat = [[9, 0], 'left', 4] #x03_create.create()
  ocupied.append(fullList(newBoat))
  x01_map.showBoard(ocupied)'''
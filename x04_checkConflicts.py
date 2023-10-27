#!python3

import x03_create
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

def fullList(ships):
  '''
  inputs:
  ships: list of all current/valid ship data
  
  return:
  list of occupied coordinates
  (example: [ [0,2] , [0,3] , [1,4] , [2,4] , [3,4] ])
  '''
  return None

  
def isConflict(occupied):
  '''
  inputs:
  occupied: list of all occupied squares
  boat: dictionary with information about your boat you are checking
  
  return: 
  True if the new boat conflicts with existing data
  False if the new boat does not conflict
  '''
  
  return None
  
if __name__ == "__main__":
  boatDatat = x03_create.boats
  boats = x03_create.create()
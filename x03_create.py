#!python3
'''
There are 5 boats in battleship. They must occupy coordinates that are horizontal or vertical only (no diagonals). 
The size of the boats are 2, 3, 3, 4 and 5. Create a function that generates a list of the data for your boats.
'''
import x01_map, x02_convert

def create():
  '''
  You will need to specify what information you need as inputs, but the output should be a list
  Add whatever code you need for each of your different ships to specify what coordinates it
  occupies and/or whether it is vertical/horizontal
  output = [
    { "name" : "Tugboat", "size" : 2 },
    { "name" : "Sumbarine", "size" : 3 },
    { "name" : "Destroyer", "size" : 3 },
    { "name" : "Battelship", "size" : 4 }
    { "name" : "Carrier", "size" : 5 },
    ]
  return output
  '''
  boatCords = []
  for i in range(5):
    loc = input(f"enter boat cauordenets for {boats[i][0]}(eg: A1(min),g6,J 10(max)): ")
    direc = input(f"enter direction of the {boats[i][0]}(eg: up, down, left, right): ")
    xy = x02_convert.convert(loc)
    boatCords.append([xy,direc])
  return boatCords

  

if __name__ == "__main__":
  boats = (('tugboat',2),('sumbarine',3),('destroyer',3),('battelship',4),('carrier',5))
  x = create()
  print(x)
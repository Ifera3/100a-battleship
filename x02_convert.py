#!python3
"""
Given a string literal convert it to a list that contains the coordinate. Your string literal should be able to remove whitespace and work with both lower and upper case values. "B3", "b3" , "B 3" and "b 3" should all correspond to the list item [1,2]
"""
import math, random

letters = ('a','A','b','B','c','C','d','D','e','E','f','F','g','G','h','H','i','I','j','J')
numbers = ('01','02','03','04','05','06','07','08','09','10')

def convert(coordinate):
  """
  input: coordinate is a string literal 
    examples: "B 3" "B3" "b3"
  return value: list containing 2 integers
  """
  #print(coordinate)
  if type(coordinate) == str:
    for i in letters:
      if i in coordinate:
        try:
          x = math.floor(letters.index(i) / 2)
          coordinate = coordinate.replace(i,'')
          y = int(coordinate) - 1
          return [x,y]
        except:
          raise NameError("Invaled input")
    raise NameError("Invaled input")
  elif type(coordinate) == list or type(coordinate) == tuple:
    try:
      print(coordinate)
      s = f"{letters[((coordinate[0] + 1) * 2) - 1]} {numbers[coordinate[1]]}"
      return s
    except:
      #print(coordinate)
      raise NameError("Invaled input")
  else:
      raise NameError("Invaled input")

def aicord(notai,hit, miss):
  #print('\n\n', hit, miss)
  if not notai:
    while True:
      if hit[-1] not in miss:
        xy = [hit[-1][0]+1,hit[-1][1]]
        if xy not in miss and xy not in hit and -1 < xy[0] < 10 and -1 < xy[1] < 10:
          break
        else:
          xy = [hit[-1][0]-1,hit[-1][1]]
          if xy not in miss and xy not in hit and -1 < xy[0] < 10 and -1 < xy[1] < 10:
            break
          else:
            if hit[-1] not in miss:
              xy = [hit[-1][0],hit[-1][1]+1]
              if xy not in miss and xy not in hit and -1 < xy[0] < 10 and -1 < xy[1] < 10:
                break
              else:
                xy = [hit[-1][0],hit[-1][1]-1]
                if xy not in miss and xy not in hit and -1 < xy[0] < 10 and -1 < xy[1] < 10:
                  break
                else:
                  x = random.randrange(10)
                  y = random.randrange(10)
                  xy = [x,y]
                  if xy not in miss and xy not in hit and -1 < xy[0] < 10 and -1 < xy[1] < 10:
                    break
      else:
        x = random.randrange(10)
        y = random.randrange(10)
        xy = [x,y]
        if xy not in miss:
          break
    #print(xy)
    return xy

if __name__ == "__main__":
  assert convert("B3") == [1,2]
  assert convert([0,9]) == "A 10"
  assert convert("d 4") == [3,3]
  print(convert([0,0]))
  

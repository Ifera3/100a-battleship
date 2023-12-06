#!python3
"""
Given a string literal convert it to a list that contains the coordinate. Your string literal should be able to remove whitespace and work with both lower and upper case values. "B3", "b3" , "B 3" and "b 3" should all correspond to the list item [1,2]
"""
import math, random

letters = ('a','A','b','B','c','C','d','D','e','E','f','F','g','G','h','H','i','I','j','J')
numbers = ('1','2','3','4','5','6','7','8','9','10')

def convert(coordinate):
  """
  input: coordinate is a string literal 
    examples: "B 3" "B3" "b3"
  return value: list containing 2 integers
  """
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
      s = f"{letters[((coordinate[0] + 1) * 2) - 1]}{numbers[coordinate[1]]}"
      return s
    except:
      raise NameError("Invaled input")
  else:
      raise NameError("Invaled input")

def aicord(notai):
  if not notai:
    x = random.randrange(10)
    y = random.randrange(10)
    return [x,y]

if __name__ == "__main__":
  assert convert("B3") == [1,2]
  assert convert([0,9]) == "A10"
  assert convert("d 4") == [3,3]
  print(convert([0,0]))
  

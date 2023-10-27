#!python3
"""
Given a string literal convert it to a list that contains the coordinate. Your string literal should be able to remove whitespace and work with both lower and upper case values. "B3", "b3" , "B 3" and "b 3" should all correspond to the list item [1,2]

"""
import math

def convert(coordinate):
  """
  input: coordinate is a string literal 
    examples: "B 3" "B3" "b3"
  return value: list containing 2 integers
  """
  letters = ('a','A','b','B','c','C','d','D','e','E','f','F','g','G','h','H','i','I','j','J')
  numbers = ('1','2','3','4','5','6','7','8','9','10')
  coordinate = str(coordinate)
  for i in letters:
    if i in coordinate:
      x = math.floor(letters.index(i) / 2)
      coordinate = coordinate.replace(i,'')
      coordinate = coordinate.strip()
      y = numbers.index(coordinate)
  return [x,y]


if __name__ == "__main__":
  assert convert("B3") == [1,2]
  assert convert("A10") == [0,9]
  assert convert("d 4") == [3,3]
  

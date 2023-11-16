
letters = ('a','A','b','B','c','C','d','D','e','E','f','F','g','G','h','H','i','I','j','J')
numbers = ('1','2','3','4','5','6','7','8','9','10')
combinations = []

for i in letters:
    for I in numbers:
        combinations.append(f'{i}{I}')
        combinations.append(f'{i} {I}')

print(combinations)
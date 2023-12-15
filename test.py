
letters = ('a','A','b','B','c','C','d','D','e','E','f','F','g','G','h','H','i','I','j','J')
numbers = ('01','1','02','2','03','3','04','4','05','5','06','6','07','7','08','8','09','9','10')
combinations = []

for i in letters:
    for I in numbers:
        combinations.append(f'{i}{I}')

print(combinations, len(combinations))
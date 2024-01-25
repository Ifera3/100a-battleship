myList = [3,4,5,1,3,6,2]
myDictionary ={
    'a1': [10,20],
    'a2': [10,33],
    'a3': [10,46]
}

coords = {}
rows = [1,2,3,4,5,6,7,8,9,10]
cols = ['a','b','c','d','e','f','g','h','i','j']
colNums = {'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8,'i':9,'j':10}
for i in cols:
    for j in rows:
        print(i+str(j))
        print(colNums[i],j)
        coords[i+str(j)] = ( colNums[i],j)
print(coords)
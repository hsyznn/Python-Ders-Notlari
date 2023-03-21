"""
list = [1,2,3,4,5]
list1 = [i for i in list]
print(list1)
"""
"""
list = [1,2,3,4,5]
list1 = [i * 2 for i in list]
print(list1)
"""
"""
list = [(1,2),(3,4),(5,6),(7,8)]
list1 = [a*b for a,b in list]
print(list1)
"""
"""
a = "Hüseyin"
b = [i * 3 for i in a]
print (b)
"""
"""
list = [[1,2],[3,4],[5,6],[7,8],[9,10],[11,12]]
list1 = []
for i in list:
    for x in i:
        list1.append(x)
print(list1)
"""
"""
list = [[1,2],[3,4],[5,6],[7,8],[9,10],[11,12]]
list1 = [x for i in list for x in i]
print(list1)
"""

array = [ 1, 9, 22 ]
g = (x for x in array if array.count(x) > 0)
array = [ 2, 5, 22 ]

print(list(g))


print(array.count(92))
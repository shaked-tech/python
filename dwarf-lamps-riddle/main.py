
lamps = [
    False, False, False, False, False, False, False, False, False, False,
    False, False, False, False, False, False, False, False, False, False,
    False, False, False, False, False, False, False, False, False, False,
    False, False, False, False, False, False, False, False, False, False,
    False, False, False, False, False, False, False, False, False, False,
    False, False, False, False, False, False, False, False, False, False,
    False, False, False, False, False, False, False, False, False, False,
    False, False, False, False, False, False, False, False, False, False,
    False, False, False, False, False, False, False, False, False, False,
    False, False, False, False, False, False, False, False, False, False
]

for i in range(1, 101):
    for j in range(i, 101, i):
        print(j)
        lamps[j-1] = not lamps[j-1]


count = 0 
for i in range(100):
    if lamps[i]:
        count += 1

print(f"{count} lamps are lit!")
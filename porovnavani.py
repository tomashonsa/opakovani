import random
p1 = []
d1 = random.randint(0,5)
for x in range(d1):
    p1.append(random.randint(0,10))

p2 = []
d2 = random.randint(0,5)
for x in range(d2):
    p2.append(random.randint(0,10))

print(p1)
print(p2)
p1.sort()
p2.sort()
p1.append(p2)

print(p1)

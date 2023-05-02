x = []
y = []
for z in range(1, 10000, 6):
    x.append(z)
while x:
    h = x.pop()
    y.append(h)
y.reverse()
print(y)
    
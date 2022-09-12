y=0
for x in range(1,6):
    a = int(input())
    if (a % 2) == 0:
        y += 1

print("{} valores pares".format(y))
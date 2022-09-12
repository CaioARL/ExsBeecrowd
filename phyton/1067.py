x = int(input())

while x <1 or x > 1000:
    x = int(input())

for i in range(1,x+1):
    if (i % 2) != 0:
        print(i)
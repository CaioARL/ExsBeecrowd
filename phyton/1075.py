n = int(input())

while n>10000:
    n = int(input())

a=0
for x in range(1,10001):
    a +=1
    if (a%n) == 2:
        print(a)
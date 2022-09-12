n = int(input())

while n >10000:
    n = int(input())

for x in range(1,n+1):
    a = int(input())
    if (a%2==0) and (a>0):
        print("EVEN POSITIVE")

    if (a%2==0) and (a<0):
        print("EVEN NEGATIVE")

    if (a%2!=0) and (a>0):
        print("ODD POSITIVE")

    if (a%2!=0) and (a<0):
        print("ODD NEGATIVE")

    if a==0:
        print("NULL")
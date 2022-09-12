a = int(input())

if a % 2 == 0:
    a +=1

print(a)
for x in range(1,12):
    a+=1
    if (a % 2) !=0:
        print(a)
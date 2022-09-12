x = int(input())
y = int(input())

if x > y:
    a=x
    b=y

if y > x:
    a=y
    b=x

c=0
for i in range(b, a+1):
    if (i%13) !=0:
        c +=i

print(c)
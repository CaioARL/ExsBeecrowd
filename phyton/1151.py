n = int(input())
fib=[0,1]
while(n>=46 or n<0):
    n = int(input())

while len(fib)<n:
    fib.append(fib[-1]+fib[-2])
    
for i in range(n):
    if i == n-1:
        print(fib[i], end="\n")
    else:
        print(fib[i] , end=" ")
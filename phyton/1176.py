repete = int(input())
fib=[0,1]

for x in range(2,61):
    fib.append(fib[x-1]+fib[x-2])
    
for i in range(repete):
    num = int(input())
    res = fib[num]
    print(f'Fib({num}) = {res}')
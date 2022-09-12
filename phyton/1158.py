n = int(input())
for j in range(n):
    x, y = list(map(int, input().split(" ")))
    soma = 0
    r = 1
    rep = 0
    while r == 1:
        if x % 2 != 0:
            soma += x
            rep += 1
            x += 1
        else:
            x += 1

        if rep == y:
            r = 0
    print(soma)

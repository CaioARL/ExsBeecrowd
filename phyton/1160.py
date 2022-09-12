T = int(input())
for x in range(T):
    cont = 0
    PA,PB,G1,G2 = input().split(" ")
    PA = int(PA)
    PB = int(PB)
    G1 = float(G1)
    G2 = float(G2)
    while PA <= PB:
        PA += int((G1 * PA) / 100)
        PB += int((G2 * PB) / 100)
        cont +=1
        if cont > 100:
            break
    if cont>100:
        print('Mais de 1 seculo.')
    else:
        print(f'{cont} anos.')
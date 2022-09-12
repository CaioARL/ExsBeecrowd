##
#
##
test = 0
while(test == 0):
    valor_1, valor_2 = list(map(int, input().split(" ")))
    if (valor_1 > 1) and (valor_1 < 20) and (valor_1 < valor_2) and (valor_2 < 100000):
        test = 1

valorImprimir = 1
for total in range(int((valor_2-valor_1)/valor_1)+1):
    CountValoresLinha = 1
    while (CountValoresLinha <= valor_1):
        if (CountValoresLinha < valor_1):
            print(valorImprimir, end=" ")
        else:
            print(valorImprimir)
        CountValoresLinha = CountValoresLinha + 1
        valorImprimir = valorImprimir + 1

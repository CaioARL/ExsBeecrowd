a = int(input("Informe um valor inteiro para A:"))
b = int(input("Informe um valor inteiro para B:"))
c = int(input("Informe um valor inteiro para C:"))

maiorAB=((a+b+abs(a-b))/2)
maiorABC=int((maiorAB+c+abs(maiorAB-c))/2)

print(f"{maiorABC} é o maior")
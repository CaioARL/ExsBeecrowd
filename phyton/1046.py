x,y = input().split()
x = int(x)
y = int(y)

while x > 24 or y > 24:
    x,y = input().split()   #ou break

while x < 1 or y < 1:
    x,y = input().split()   #ou break

if x == (y-1):
    print("O JOGO DUROU 1 HORA(S)")
    
if x == y:
    print("O JOGO DUROU 24 HORA(S)")

if x > y:
    h1 = (24 - x) + y
    print(f"O JOGO DUROU {h1} HORA(S)")

if x < y:
    h2 = y - x
    print(f"O JOGO DUROU {h2} HORA(S)")
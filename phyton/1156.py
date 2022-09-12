S=0
y=1
for x in range(1,40,2):
    S+= x / y
    y*=2
print(f'{S:.2f}')
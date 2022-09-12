t = int(input())
vetor=[]
x = []
num = 0

while t>50 or t<2:
    t = int(input())
    
while len(x) <= 1000:
    x.append(num)
    if num == (t-1):
        num = 0
    else:
        num+=1
   
for i in range(1000):
    print("N[{}] = {}".format(i,x[i]))
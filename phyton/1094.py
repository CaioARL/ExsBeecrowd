n = int(input())

while n<1 and n >15:
    n = int(input())
    
tot=0
totC=0
totR=0
totS=0

for x in range(1,n+1):
    q,t = input().split(" ")
    q = int(q)
    t = str(t)
    tot += q
    if(t == "C"):
        totC+= q
    if(t == "R"):
        totR+=q
    if(t == "S"):
        totS+=q
        
pC = (totC / tot)*100
pR = (totR / tot)*100
pS = (totS / tot)*100

print("Total: {} cobaias".format(tot))
print("Total de coelhos: {}".format(totC))
print("Total de ratos: {}".format(totR))
print("Total de sapos: {}".format(totS))
print("Percentual de coelhos: {:.2f} %".format(pC))
print("Percentual de ratos: {:.2f} %".format(pR))
print("Percentual de sapos: {:.2f} %".format(pS))               
i=0
media = 0
while i<2:
    a=float(input())
    i+=1
    while (a>10) or (a<0):
        print("nota invalida")
        a = float(input())
    if (a>0) or (a<=10):
        media+=a
print("media = {:.2f}".format(media/2))
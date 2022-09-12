n = int(input())

for x in range(1,n+1):
    a,b,c=list(map(float,input().split(" ")))
    m = ((a*2) + (b*3) + (c*5)) /10
    print("{:.1f}".format(m))
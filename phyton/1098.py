i=0
j=1
acres = 0.2

while i<=2:
    for x in range(0,3):

        if i == 1.0 or i==0.0 or i>1.8:
            print("I={:.0f} J={:.0f}".format(i,j))
                
        elif i<2:
            print("I={:.1f} J={:.1f}".format(i,j))
        j=j+1
    i+=acres
    j=1+i
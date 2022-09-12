entrada = int(input())
string = ''
for x in range(1,entrada+1):
    if x < entrada:
        string+='Ho '
    else:
        string+='Ho!'
print(string)
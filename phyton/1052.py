a = int(input())
mes = ["January","February","March","April","May",
"June","July","August","September","October","November","December",]

while a < 1 or a > 12:
    a = int(input())

a += -1
print(mes[a])
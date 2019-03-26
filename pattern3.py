#WhatsApp Image 2019-03-19 at 1.33.43 PM.jpeg
x=5
j=0
for i in range(1,8):
    for l in range(i+x):
        print(" ",end=" ")
    x=x-2
    for k in range(i+j) :
        print("*",end=" ")
    print(" ")
    j=j+1

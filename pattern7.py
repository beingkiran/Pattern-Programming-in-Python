#WhatsApp Image 2019-03-19 at 1.33.47 PM.jpeg
x=6
y=8
g=-1
f=7
b=6
s=1
for i in range(1,9):
    for j in range(i):
        print("*",end=" ")
    for k in range(i+x):
        print(" ",end=" ")
    for m in range(i+y) :
        print("*",end=" ")
    for k in range(i+g):
        print(" ",end=" ")
    for c in range(i-1):
        print(" ",end=" ")
    for h in range(i+f)  :
        print("*",end=" ")
    for m in range(i+b) :
        print(" ",end=" ")
    for v in range(i):
        print("*",end=" ")


    print(" ")
    x=x-2
    y=y-2
    f=f-2
    b=b-2





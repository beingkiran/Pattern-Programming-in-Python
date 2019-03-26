#WhatsApp Image 2019-03-21 at 3.59.18 PM.jpeg
r=4
for i in range(1,7):
    for j in range(1,i):
        print("*",end=" ")
    for k in range(i+r):
        print("#",end=" ")
    print(" ")
    r=r-2

r=4
for i in range(1,7):
    for j in range(1,i):
        print("#",end=" ")
    for k in range(i+r):
        print("*",end=" ")
    print(" ")
    r=r-2
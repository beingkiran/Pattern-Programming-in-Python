#WhatsApp Image 2019-03-21 at 3.46.10 PM.jpeg
h=3
for i in range(1,5):
    for j in range(i+h):
        print("*",end=" ")
    for k in range(i-1):
        print("@",end=" ")
    print(" ")
    h=h-2
h=4

for i in range(1,6):
    if i%2==1:
        sym1='#'
        sym2="@"
    else:
        sym1="@"
        sym2="#"
    for j in range(i+h):
        if j%2==1:
            print(sym1,end=" ")
        else:
            print(sym2,end=" ")

    print("")
    h=h-2
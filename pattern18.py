'''
#####
 ####
  ###
   ##
    #
*****
#
##
###
#####
######
'''

h=4
for i in range(1,6):
    for j in range(1,i):
        print(" ",end=" ")

    for k in range(i+h):
        print("#",end=" ")
    print(" ")
    h=h-2

for i in range(5):
    print("*",end=" ")

for i in range(1,7):
    for j in range(1,i):
        print("#",end=" ")
    print(" ")
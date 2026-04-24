#   *
#  **
# ***
n=3
for i in range(1,n+1):
    for j in range(0,n-i) :
        print(" ", end="")
    for k in range(i):
        print("*",end="")
    print()

#   *
#  ***
# *****
for i in range(1, n+1):
    for j in range(0,n-i):
        print(" ",end="")

    for k in range(2*i-1):
        print("*",end="")
    print()

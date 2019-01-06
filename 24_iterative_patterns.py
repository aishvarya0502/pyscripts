n = int(input("Enter a number of rows"))
for i in range(1,n+1):
    for j in range(1,i+1):  #print("*"*i)
        print("*",end=" ")
    print()

r = int(input("Enter a number of rows"))
for i in range(1,r+1):
    print(" *"*r)
    r -= 1

p = int(input("Enter number of rows"))
for i in range(1,p+1):
    for j in range(1,p+1):
        print("*",end=" ")
    print()

q = int(input("Enter number of rows"))
for i in range(q):
    for j in range(q):
        print(" * ",end='')
    print()

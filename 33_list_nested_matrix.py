list = [[10,20,30],[40,50,60],[70,80,90]]

print(list)
print("Elements Row wise : ")
for i in list:
    print(i)

print("Element in Matrix style : ")

for i in range(len(list)):
    for j in range(len(list[i])):
        print(list[i][j],end=" ")
    print()

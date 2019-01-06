str = input("Enter a String")

list  = str.split()
list =  list[::-1]
print(" ".join(list))

li  = str.split()
rev = []
for i in li:
    rev.append(i[::-1])
print(" ".join(rev))


print(str[::2])
print(str[1::2])

i = 0
while i<len(str):
    print(str[i],end=" ")
    i += 2
print()
i = 1
while i<len(str):
    print(str[i],end=" ")
    i += 2

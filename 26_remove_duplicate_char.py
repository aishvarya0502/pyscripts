str = input("Enter a String")
l = []
for i in str:
    if (i not in l):
        #l.append(i)
        l += [i]
    else:
        pass
print(l)

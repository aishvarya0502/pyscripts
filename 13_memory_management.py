l = [1,2,3]
d = [1,2,3]

print(id(l)) #0000
print(id(d)) #0008
if(l is d):
    print(True)
else:
    print(False) #output as each time we create a variable that refers to an object it creates a new object
    #Each time we create a variable(list,tuple,set) that refers to an object, a new object is created.

a = [4,5,6]
b = a #now b refers to the same objct as that of a
print(id(a))
print(id(b))
if a is b:
    print(True)
else:
    print(False)

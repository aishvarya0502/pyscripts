a=int(input("Enter First number:")) #input to a by default is string only.
b=int(input("Enter Second number:"))
x = a if (a<b) else b
print("Mininmum value:",x)

#Ternary nesting
z = 10 if (20<30) else 40 if (50<60) else 70
print(z)#Ans 10
y = 10 if (20>30) else 40 if (50>60) else 70
print(y)#Ans 70

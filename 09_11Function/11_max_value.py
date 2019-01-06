
x = int(input("Enter First Value"))  #30
y = int(input("Enter Second Value")) #20
z = int(input("Enter Third Value"))  #25

result = x if (x>y and x>z) else y if y>z else z
print("The Maxium value is :",result)

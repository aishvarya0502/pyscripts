int = eval(input("Enter number of students : "))
rec = {}
i = 1
while i<=int:
    name = input("Enter stundent Name : ")
    marks = input("Enter student % : ")
    rec[name] = marks
    i += 1

for x in rec:
    print( x ,":", rec[x])

str = input("Enter alphanumeric String")

output = ""#[]
alpha = num = ""#[] being list it was performing wierd
#error the type of object i took above vastly matters because operation changes wiht different object type
for i in str:
    if i.isalpha():#'a'<=i<='z' or 'A'<=i<='Z':
        alpha = alpha + i
    else:#'0'<=i<='9':
        num = num + i

print(alpha)
print(num)
#print(alpha + num)

for x in sorted(alpha):
    output += x

for x in sorted(num):
    output += x

print(output)

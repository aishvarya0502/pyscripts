#input a4k3b2
#output aeknbd

str = input("Enter the required input in format charintcharint : ")
output = ""
for i in str:
    if(i.isalpha()):
        output = output + i #if we remove this then we get a way to decrypt an encrypted alphanumeraic string
        prv = i
    else:
        output = output + chr(ord(prv) + int(i))
print(output)

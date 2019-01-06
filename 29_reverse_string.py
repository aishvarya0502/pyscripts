s = input("Enter a string to get reverse : ")
####################################
rev = []
l = len(s) - 1  #len = len(s) here now len is an integer and shadows the in-built function.
for i in range(len(s)):
        rev.append(s[l - i])

print("".join(rev))
####################################
j = s[::-1]
print(j)
####################################
def reverse(s):
  str = ""
  for i in s:
    print(i)
    str =  i + str
  return str
result = reverse(s)
print (result)
####################################
def reversebyrecur(s):
    if len(s) == 0:
        return s
    else:
        print("cha : ",s)
        return (reverse(s[1:]) + s[0])
        
str = "python"
print(reversebyrecur(str))

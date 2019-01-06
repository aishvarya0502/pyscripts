x = input("Enter a String")
num = {}#declared a dictionary, this is not a set
for i in x :
    num[i] = x.count(i) #storing values in key : pair
    #here note the last occuring char which is repeated in String set the value for key
    #as same key value gets overwritten
    #for input like aaaaaaaaaaaaaaaaaaaaaa the last occurennce of 'a' set the value
print(num) #pritn dictionary
for k in num:
    print( k,':' ,(num[k]))

y = input("Enter a String")
num = {}#declared a dictionary, this is not a set
for i in y :
    num[i] = y.get(i,0) + 1 #storing values in key : pair
print(num) #pritn dictionary
for k in num:
    print( k,':' ,(num[k]))

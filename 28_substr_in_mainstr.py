mainstr = input("Enter the main string : ")
substr = input("Enter sub-string : ")

if substr  in mainstr:
    print(substr, 'is present in ', mainstr)
else:
    print(substr," is not present", mainstr)

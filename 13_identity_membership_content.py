a = 10
b = 10
c = -10

#identity is and is not used to know when two objects are pointing to the same obeject
print(a is b)#True
print(a is c)#False
print(a is not c)#True

list1 = [10,20,30]
list2 = [10,20,30]
print(id(list1))
print(id(list2))
print(list1 is list2)

#content comparison by == operator
print('when compared by == ',list1,list2,list1 == list2)

#difference b/w is and ==
    # is is ment for Address comparison
    # == is ment for content comparison

#membership operator
list = [10,20,30]
print(10 in list)
print(60 in list)
print(60 not in list)


s = "Hello SAI"
print(s)
print( "lo" in s)
print(" " in s)

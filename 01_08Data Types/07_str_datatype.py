z = 'Sai ram'
print(z)
print(type(z))

x = '''SAI
    RAM'''
print(x)

str = """Durga Sir "Python" classes are very helpfull"""
print(str)
#multi line

#index of string
    #right to left => + index s='durga' => 0,1,2,3,4
    #left to right => - index s='durga' => -5,-4,-3,-2,-1
a = 'DurgaSoft'
print(a[0])
print(a[2])
print(a[-1])
print(a[-2])
#print(a[-10]) #index out of range


#slice operator
#s[begin:end] => return a substring from begin index to end-1 index
#d u r g a s o f t
#0 1 2 3 4 5 6 7 8
#9 8 7 6 5 4 3 2 1
print(a[0:4])   #Durg
print(a[1:4])    #urg
print(a[2:2])    #no output
print(a[2:-1])   #rgaSof (begin to end -1 => 2 to -2)
print(a[-1:3])   # -1 to 2 // no output as -1 is last index thus it does not print there  after**** moving in +ive direction
print(a[-1:-3])  #no ouptut , begin value should be lower and end be higher -1 to -4**************
print(a[-4:-1])  #sof
print(a[-1:])     # t
print(a[1:])      #urfgSoft , here end is  optional
print(a[:2])      #Du , here start is  optional
print(a[2:3])   #r

print(a[::])        #DurgaSoft
print(a[::-1])  # here move form begin to end+1 in backward direction possible because 0 to 8+1 = 9
print(a[2:7:-1]) #no output as for -ive step we move backward direction from begin to end+1 but 2 will never get 9 in backward direction

#s[begin:end:step] to make jump

#repetition operator
a *= 2
print(a*2)
print(len(a))


b = input("Enter a string")
i = 0
for x in b:
    print('The character at +ive index {} and at -ive index {} is {}'.format(i,i-len(b),x))
    i += 1


c = input("Enter a string : ")
d = {} #empty dict
e = {} #empty dict
for i in range(len(c)):
    d[i] = c[i]
    e[i-len(c)] = c[i]

print()
print(d)
print()
print(e)
print()

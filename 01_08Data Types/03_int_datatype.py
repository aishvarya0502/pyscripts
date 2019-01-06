a = 10    # this is decimal representation
A = -10   # this is decimal representation
b = 0b1111  # this is binary representation
B = -0B1111 # this is binary representation
c = 0o777   # this is octal representation
C = -0O777  # this is octal representation
d = 0xFaCe  # this is Hexa representation
D = -0XfAcE # this is Hexa representation
print(a,A,b,B,c,C,d,D) #output 10 -10 15 -15 511 -511 64206 -64206

#conversion function
print(bin(a))
print(oct(a))
print(hex(a))
#and if we want to get decimal from some other representation than it done internally
z = 0xf
print(z)
#output is 15

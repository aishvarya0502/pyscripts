#format z = a + bj
#a is real and can be int(all 4 rep) or float
#b is iamginary and can be obly int(decimal) or float
#j is underoot of -1
z = 10 + 13j
print(z)
print(type(z))
z = 0xf + 15.6j
print(z)
a = 0.9 + 1j
print(a)
# output (10+13j) <class 'complex'> (15+15.6j) (0.9+1j)

result = a + z
print(result.real)
result = a - z
print(result.imag)
result = a*z
print(result)
result = a/z
print(result)
# output
#(15.9)
#(14.6)
#(-2.0999999999999996+29.04j)
#(0.062131693569049455+0.00204970535485524j)

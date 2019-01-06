list = []
for x in range(1,11): list.append(x*x)
print(list)

l = [x*x for x in range(1,11)]
l1 = [ x for x in l if x%2==0]
print(l)
print(l1)

words = "the quick brown fox jumps over the lazy dog"
l2 = [[w.capitalize(),len(w)] for w in words.split()]
print(l2)
print()

word = "the quick brown fox jumps over the lazy dog"
l3 = []
for w in word:
      l3.append(w)
      print(w,end=" ")
print()
print(l3)
print()

l4 = sorted(word.split())
print("l4 : ",l4)
print()


l6 = sorted(word)
print("l6 : ",l6)
print()

l5 = [w for w in word.split()]
print("".join(l5))
l7 = "".join(sorted("".join(l5)))
print(l7, type(l7))

l8 = ""
for i in "".join(sorted("".join(l5))):
    if i not in l8:
        l8 += i
    else:
        pass
print(l8)

print("".join(word))

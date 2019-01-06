def read(input):
    if input == 1:
        print("one")
    elif input == 2:
        print("two")
    elif input == 3:
        print("three")
    elif input == 4:
        print("four")
    elif input == 5:
        print("five")
    elif input == 6:
        print("six")
    elif input == 7:
        print("seven")
    elif input == 8:
        print("eight")
    elif input == 9:
        print("nine")
    elif input == 0:
        print("zero")


def evaluate(input,times):
    if times == 1:
        #print("Zero place value : ",input)
        read(input)
    elif times == 2:
        #print("Once place value : ",input)
        read(input)
    elif times == 3:
        #print("Tens place value : ",input)
        read(input)

x = eval(input("Enter a number 3 DIGIT NUMBER : "))
y = 0
print(type(x))
if type(x)!= type(y):
    print("Invalid Number")
else:
    count = 0
    while x != 0:
        digit = x%10
        x  = int(x/10)
        #print(digit)
        count += 1
        evaluate(digit,count)

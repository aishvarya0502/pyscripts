def get_bool(promt):
        try:
            return {"true":True,"false":False}[input(promt).lower()]
        except ValueError:
            print : "error"

eno = int(input("Enter Employee Number : "))
ename = input("Enter Employee Name : ")
esal = float((input("Enter Employee Salary : ")))
enaddress = input("Enter Employee Address : ")
estatus =bool(input("Enter Employee marriage status:"))
#get_bool("Enter Employee marriage status:")
print("Confirm Information")
print("ENO : ",eno)
print("ENAME : ",ename)
print("ESAL : ",esal)
print("enaddress : ",enaddress)
print("marriage : ",estatus)

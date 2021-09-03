ValidOperations = ("x","-","+","/")

Num1 = float(input("choose a number: "))
while not isinstance(Num1,float):
    
    try:
        num1 = float(input("enter a number"))
    except ValueError:
        print("Invalid Input")
    
Operation = input("choose an operation: ")
while Operation not in ValidOperations:
    print("Invalid Operation")
    Operation = input("Choose an operation: ")

Num2 = float(input("choose another number: "))
while not isinstance(Num2,float):
    
    try:
        num2 = float(input("enter another number"))
    except ValueError:
        print("Invalid Input")


if Operation == "+":
    print (f'{"{0:,.2f}".format(Num1)} + {"{0:,.2f}".format(Num2)} = {"{0:,.2f}".format(Num1 + Num2)}')

if Operation == "-":
    print (f'{"{0:,.2f}".format(Num1)} - {"{0:,.2f}".format(Num2)} = {"{0:,.2f}".format(Num1 - Num2)}')


if Operation == "/":
    print (f'{"{0:,.2f}".format(Num1)} / {"{0:,.2f}".format(Num2)} = {"{0:,.2f}".format(Num1 / Num2)}')

    
if Operation.lower() == "x":
    print (f'{"{0:,.2f}".format(Num1)} x {"{0:,.2f}".format(Num2)} = {"{0:,.2f}".format(Num1 * Num2)}')

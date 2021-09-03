GoodInputHit = False
Valid_operations = ["x","+","/","-"]
while(GoodInputHit == False):
    
    Num1 = (input("enter a number: "))
    if not Num1.isdigit():
        print("Invalid Input")
        Num1 = (input("enter a number: "))
    
    Operation = input("enter an operation: ")
    if Operation not in Valid_operations:
        print("Invalid Operation")
        input("enter an operation: ")
    Num2 = (input("enter another number: "))
    if not Num2.isdigit():
        print("Invalid Input")
        Num2 = (input("enter another number: "))

    Num1 = int(Num1)
    Num2 = int(Num2)

    if Operation.lower() == "x":
        print(Num1*Num2)
        GoodInputHit = True
    elif Operation == "+":
        print((Num1+Num2))
        GoodInputHit = True
    elif Operation == "-":
        print(Num1-Num2)
        GoodInputHit = True
    elif Operation == "/":
        print(Num1/Num2)
        GoodInputHit = True
    else:
        print("Invalid Input")
    
def create_phone_number(n):
    phoneNumber = ("")
    output = ("")
    for i in n:
        phoneNumber += str(i)
    output = "(" + phoneNumber[0:3] + ")" + " " + phoneNumber[3:6] + "-" + phoneNumber[6:11]
    print(str(output))
    return str(output)
create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])
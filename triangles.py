def is_triangle(a, b, c):
    pizza = [a,b,c]
    pizza.sort()
    print(pizza)
    print (int(pizza[0])**2,int(pizza[1])**2,int(pizza[2])**2)

    if int(pizza[0])**2 + int(pizza[1])**2 == int(pizza[2])**2:
        print("good boy")
        return True
    else:
        print("bad boy")
        return False
is_triangle(3,3,3)
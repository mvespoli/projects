def persistence(n):
    num = str(n)    
    product = 1
    gonext = False
    Tally = 1
    if len(str(num)) == 1:
        Tally = 0
    while gonext == False:
        for i in num:
            print("i: " + i)
            product = product * int(i)
            print(product)
        num = str(product)
        product = 1
        
        print(num)
        print(Tally)
        if len(str(num))!= 1:
            Tally += 1
            gonext = False
        else:
            gonext = True
        print(num)
        print(Tally)
    return(Tally)
    
    
    
persistence(375)
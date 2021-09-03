def persistence(n):
    num = str(n)    
    product = 1
    goagain = False
    tally = ""
    while goagain == False:
        for i in num:
            print("i: " + i)
            product *= int(i)
            print("Product: " + str(product))
        if len(str(num)) != 1:
            goagain = False
            
        else:
            goagain = True

        tally += str(product)
    print("Length of Tally: " + str(len(tally)))
    
persistence(39)
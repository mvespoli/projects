def digital_root(n):
    num = str(n)
    add = 0
    runAgain = True 
    if len(num) == 1: 
        runAgain = False 
    while runAgain == True:
        add = 0
        for i in num:
            add += int(i)
        num = str(add)    
        if len(str(num)) == 1:
            runAgain = False
    print(num)
    return(int(num))
digital_root(12345)
def make_readable(seconds):
    import math
    second = "0"
    minute= "0"
    hour = "0"
    hour = int((seconds/60**2))
    minute = int(((seconds/60**2) - math.floor((seconds/60**2)))*60)
    second = round((((seconds/60) - math.floor((seconds/60)))*60))

    x = [str(hour), str(minute), str(second)]
    y = []
    z = ()
    for each in x:
        if len(str(each)) <= 1:
            each = str("0" + str(each))
        y.append(each)
    print(y[0])
    print(y[1])
    print(y[2])
    z = y[0] +":"+y[1]+":"+y[2]  
    print (z) 
    return z 

make_readable(235200)

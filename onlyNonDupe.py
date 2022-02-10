def nondupe(input):
    uniqueArray = []
    for i in input:
        if str(i) in uniqueArray:
            continue
        else:
            uniqueArray += str(i)
        for j in uniqueArray:
            if str(i) in uniqueArray:
                continue
            else:
                uniqueArray += str(i)
            
    print(uniqueArray)
nondupe([1,2,1,2,1,3,2,1,2,6])
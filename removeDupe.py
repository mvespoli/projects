def findUnique(input):
    uniqueArray = []
    dupe = False
    remove = False
    position = -1
    for i in input:
        for j in uniqueArray:
            print(j)
            if str(j) == str(i):
                print("first instance")
                remove = True
                position = j
                break 
        
        if remove == True:
            uniqueArray.remove(position)
            remove = False
        else:
            uniqueArray += str(i)
    print(uniqueArray)


findUnique([2,1,1,2,4])
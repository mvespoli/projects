def permutations(string):


    List = [] 
    List2 = []   
    Final = []
    if len(string) <= 1:
        return [string]
    for i in range(len(string)):
        m = string[i]
        listRem = string[:i] + string[i+1:]
        print('listRem = ' + listRem)

        for j in range(len(listRem)+1):
            List.append(listRem[:j] + m + listRem[j:])
            List2.append(listRem[j::-1] + m + listRem[:j:-1])
            
    
    print(List2)
    Final = (List + List2) 
    Final = list(dict.fromkeys(Final))
    print(Final)
    return Final
    

            
            



            

permutations('1234')
def permutations(string):
    List = []
    ListF =[]
    ListR = []
    
    

    if len(string) <= 1:
        return [string]

    for i in range(len(string)):
        m = string[i]
        
        rList = string[:i] + string[i+1:]
        for j in range(len(rList)):
            rListF = rList[j] + rList[:j] + rList[j+1:]
            rListR = rList[j] + rList[:j:-1] + rList[j::-1]
            ListF.append(str(m) + str(rListF))
            ListR.append(str(m) + str(rListR))
            print(rList[j])
            print('break 1')
            print(rList[:j:-1])
            print('break 2')
            print(rList[j-1::-1])
            print('break 3')
            print(rListR)
        List.append(str(m) + str(rList))
        # for j in rList:
            
              
        print(List)
        print(ListF)
        print(ListR)
        
            
        



    #     for j in range(len(rList)):
    #         rList2 = rList[:j] + rList[j+1:] + rList[j]
    #         print(rList2)
    #         List2.append(str(m) + str(rList2))
    #         print(List2)
    #         print("---")
    #         print(List)
            
    #     print(next)
    #     List.append(str(m) + str(rList))
        
        
    # print(List)
    # print(list(dict.fromkeys(List2)))
    # return list(dict.fromkeys(List2))      

permutations('1234')
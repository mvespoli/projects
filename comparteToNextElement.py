def compare(pizza):
    for i in pizza[0:-1]:    
        print(i)
        if pizza[pizza.index(i)+1] > i:
            print(str(pizza[pizza.index(i)+1]) + " is greater than " + str(i))
        elif pizza[pizza.index(i)+1] < i:
            print(str(pizza[pizza.index(i)+1]) + " is less than " + str(i))
        elif pizza[pizza.index(i)+1] == i:
            print(str(pizza[pizza.index(i)+1]) + " is equal to " + str(i))
        
    
compare([10,20,14,14,3,-10,4])
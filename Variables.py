character_name = input("Enter your name: ")
character_age = input("Enter your age: ")
hitGoodInput = False
#Zack True True
while(hitGoodInput == False):
    print(character_name)
    print(character_age)
    if character_name == 'Zack' and character_age == '25':
        print("Hey, my name is " + character_name + ".")
        print("I enjoy anime and love being known as the nicest person.")
        print("Additionally, I am " + character_age + ", and if you add 44 to that number, it becomes 69. Ha!") 
        hitGoodInput = True
       
#Zack True False
    elif character_name == 'Zack' and character_age != '25':
        print("Hey cringe nerd! You're not " + character_age + ". Do you think this is a game?")
        character_age = input("Enter your age: ")
        hitGoodInput = False
        
#Brandon True True
    elif character_name == 'Brandon' and character_age == '25':
        print("Hola! Qué tal!")
        print("My name is Brandon and I necesito mas agua")
        print("I am the breaker of doors and the lover of couches")
        hitGoodInput = True
        
#Brandon True False
    elif character_name == 'Brandon' and character_age != '25':
        print("Hey cringe nerd! You're not " + character_age + ". Do you think this is a game?")
        print("Do they count different in Mexico?")
        character_age = input("Enter your age: ")
        hitGoodInput = False
       
#McChills 
    elif character_name =='Mike' and character_age == '24':
        print("Naw bro try inputting your name as McChills")
        character_name = input("Enter your name: ") 
        hitGoodInput = False
    elif (character_name =='Michael' and character_age == '24'):
        print("Naw bro try inputting your name as McChills")
        character_name = input("Enter your name: ") 
        hitGoodInput = False
    elif character_name =='Mechilly' and character_age == '24':  
        print("Naw bro try inputting your name as McChills") 
        hitGoodInput = False
        character_name = input("Enter your name: ")    
    elif character_name =='McChills' and character_age != '24':
        print("Naw you're not" + character_age + "yet homie.")
        character_age = input("Enter your age: ")
        hitGoodInput = False
    elif character_name =='McChills' and character_age == '24':
        print("Ayyyy my dads a Narc! But watta you gunna do about it")
        hitGoodInput = True
        
    else:
        print("You would break my code eh?")
        hitGoodInput = False
        character_name = input("Enter your name: ")
        character_age = input("Enter your age: ")

def myFunction():
    valid_names = ['Zack', 'Brandon', 'Mike', 'Michael', 'Mechilly', 'McChills']
    invalid_mcchills = ['Mike', 'Michael', 'Mechilly']
    character_name = input("Enter your name: ")
    if character_name == "exit":
        return character_name
    elif character_name not in valid_names:
        print("Hey I don't know you!")
        return None
    character_age = input("Enter your age: ")
#Zack True
    if character_name == 'Zack' and character_age == '25':
        print("Hey, my name is " + character_name + ".")
        print("I enjoy anime and love being known as the nicest person.")
        print("Additionally, I am " + character_age + ", and if you add 44 to that number, it becomes 69. Ha!")
    elif character_name == 'Zack' and character_age != '25':
        print("Hey cringe nerd! You're not " + character_age + ". Do you think this is a game?")
        
#Brandon True True
    elif character_name == 'Brandon' and character_age == '25':
        print("Hola! QuÃ© tal!")
        print("My name is Brandon and I necesito mas agua")
        print("I am the breaker of doors and the lover of couches")
#Brandon True False
    elif character_name == 'Brandon' and character_age != '25':
        print("Hey cringe nerd! You're not " + character_age + ". Do you think this is a game?")
        print("Do they count different in Mexico?")
       
#McChills 
    elif character_name in invalid_mcchills:
        print("Naw bro try inputting your name as McChills")
    elif character_name =='McChills' and character_age != '24':
        print("Naw you're not " + character_age + " yet homie.")
    elif character_name =='McChills' and character_age == '24':
        print("Ayyyy my dads a Narc! But watta you gunna do about it")
    else:
        print("You would break my code eh?")

character_name = ""
while character_name != "exit":
    character_name = myFunction()
quit()
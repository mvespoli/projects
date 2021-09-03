def alphabet_position(text):
    alphabet_number = {'a':'1','b':'2','c':'3','d':'4','e':'5','f':'6','g':'7','h':'8','i':'9','j':'10','k':'11','l':'12','m':'13','n':'14','o':'15','p':'16','q':'17','r':'18','s':'19','t':'20','u':'21','v':'22','w':'23','x':'24','y':'25','z':'26'
        }
    alphabet = text.replace(" ","")
    print(alphabet)
    numbers = ""
    alphabet2 = alphabet.lower()
    
    print(alphabet2)
    
    for pizza in alphabet2:
        print(pizza)
        if pizza in alphabet_number:
            numbers = numbers + alphabet_number.get(str(pizza)) + " "
        else:
            continue
            print("")
    
    print(numbers[:-1])
    numbers = numbers[:-1]
    return numbers
alphabet_position("'o clockc")       

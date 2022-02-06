def disemvowel(string_):

    vowelList = ["a","e","i","o","u"]
    newString = (string_)
    for i in string_:
        if i.lower() in vowelList:
            newString = newString.replace(i,"")
            

    print(newString)

    return newString

disemvowel("This website is for losers LOL!")
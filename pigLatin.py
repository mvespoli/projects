def pig_it(text):
    wordsArray = text.split(' ')
    newArray = ""
    print (wordsArray)
    punctuationMap= ['.', ",", '!', ';', ':', "'", '[', ']', '(', ')', '-', '?']
    for word in wordsArray:
        if any(x in punctuationMap for x in word) and len(word) >1:
            for i in punctuationMap:
                if i in word:
                    word = word[1: word.index(i)] + word[0:1] + 'ay' +  word[word.index(i):] + " "
                    newArray += word
        elif any(x in punctuationMap for x in word) and len(word) ==1:
            newArray += word
            
        else:
            word = word[1:] + word[0:1] + 'ay' + " " 
            newArray += word
    newArray.strip()
    print(newArray)
    return newArray.strip()
    
    
pig_it('sample text here')
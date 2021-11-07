def valid_parentheses(string):
    counter = 0
    for i in string:
        print(i)
        if i == '(':
            counter += 1
        elif i == ')':
            counter -= 1
        if counter < 0:
            break
    print(counter)
    if counter != 0:
        print(False)
        return(False)
        
    print(True)
    return(True)

valid_parentheses("khwiwqwjwjf((ch(j)zoekredt)sic")
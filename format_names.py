def namelist(names):
    output = ""
    counter = 0
        
    for person in names:
        for key, value in person.items():
        
            if len(names) == 1:
                output = (value)
                return(output)
            elif counter == len(names) -1:
                output += ("& " + value)
            elif counter == len(names) -2:
                output += (value + " ")
            else:
                output += (value + ", ")
        counter += 1
    print(output)
    return output
namelist([ {'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'} ])
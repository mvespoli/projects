def solution(string,markers):
    string = string.split("\n")
    print(string)
    print(markers)
    pizza = ""
    for i in string:            
        for j in i:
            if j in markers:
                break
            else:
                pizza += j
        if i != string[-1]:
            pizza += "\n"

    stripPizza = pizza.split("\n")
    output = ""
    for i in stripPizza:
        if i == stripPizza[-1]:
            output += i.strip()
        else:
            output += i.strip() + "\n"
    print(output)
    return output



 if output == "\n":
        output = ""
    # Gstring = ""
    # for i in markers:
    #     if Gstring == '':
    #         Gstring = i
    #     else:
    #         Gstring = Gstring + " | " + i
    # print(Gstring)
    # ans = ""
    
    
    # for i in markers:
    #     string = (re.sub(i,"",string))
    # print(string)
   
    
    # ans = re.split(Gstring,string)
    # ans2 = ""
    # for i in ans:
    #     ans2 += i
    # print(ans2)
    # return ans2
    
    
   
#     for index, value in enumerate(markers):
#         print(index)
#         print(value)
#         string.split(value)
#     print(string)

# text = "apples pears # and bananas grapes bananas !apples"
# pizza = ['#', '!']
solution("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"])
a1 = ["live", "arp", "strong"] 
a2 = ["lively", "alive", "harp", "sharp", "armstrong"]
def in_array(array1, array2):
    pizza = []
    r = []
    for i in array1:
        for j in array2:
            if i in j:
                print(i)
                pizza.append(i)
    r = list(dict.fromkeys(pizza))
    r.sort()
    print(r)
    return [r]
in_array(a1,a2)  
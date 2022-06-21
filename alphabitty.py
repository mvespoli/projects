def alphabet_list(letter):
    x=letter
    print(x)
    while x != 'M':
        x = chr(ord(x)+1)
        print(x)
    return x
                

print(alphabet_list('A'))
class RomanNumerals:
    romanNumbersDictionary = {'I': 1, 'II': 2, 'III': 3, 'IV': 4, 'V': 5, 'VI': 6, 'VII': 7, 'VIII': 8, 'IX': 9, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000 }
    romanToNumbers = []
    def to_roman(val):
        newVal = str(val)
        for i in str(val):
            if len(newVal) == 4:
             
                newVal = newVal[1:]
                print(newVal)
            if len(newVal) == 3:
                print('C')
                newVal = newVal[1:]
                print(newVal)
            if len(newVal) == 2:
                print('X')
                newVal = newVal[1:]
                print(newVal)
            if len(newVal) == 1:
                print('I')
                newVal = newVal[1:]
                print(newVal)

        return ''

    def from_roman(roman_num):
        return 0

    to_roman(2003)
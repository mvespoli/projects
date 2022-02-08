def palindrome(word):

    for i in word[::-1]:
        word += i
    print(word)

palindrome("pizza")
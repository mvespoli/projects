# def tribonacci(signature, n):
#     mylist = signature
#     add = 0
#     print(signature[-3:])
#     for i in range(n):
#         add = sum(signature[-3:])
#         mylist.append(str(signature) + str(add))
#         print(mylist)
#         print (add)
        
#     print(mylist)


# tribonacci([2, 1, 1, 1], 10)


# 1 1 1
# 1 1 1 3
# 1 1 1 3 5
# 1 1 1 3 5 9
# 1 1 1 3 5 9 17

def tribonacci(signature, n):
    print(signature[-3:])
    if n == 0:
        return []
    if n < 3:
        return signature[:n]
    for i in range(3,n):
        signature.append(sum(signature[-3:]))
    return signature
print(tribonacci([1, 1, 1], 10))
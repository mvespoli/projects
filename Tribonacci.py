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
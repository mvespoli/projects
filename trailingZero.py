def zeros(n):
    f = 5
    count = 0
    while n >= f:
        count += n//f
        f *= 5
    return(count)
 
zeros(12)

 
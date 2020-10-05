def power(x,n):
    if n == 0:
        return 1
    else:
        part = power(x,n//2)
        result = part*part
        if n%2 == 1:
            result *= x
        return result   
    

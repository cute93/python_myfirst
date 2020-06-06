def isosu(n):
    if n<2:
        return False
    if not n%2:
        return False
    for i in range(3, n//2+1):
        if not n%i:
            return False
    return True
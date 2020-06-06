def issosu(n):
    if n<2:
        return False
    if not n%2:
        return False
    for i in range(3, n//2+1):
        if not n%i:
            return False
    return True
def sosulist(n):
    return [a for a in range(2, n+1) if issosu(a)]
def divisor(n):
    rtn = []
    for a in range(1, n//2+1):
        if not n%a:
            rtn.append(a)
    rtn.append(n)
    return rtn

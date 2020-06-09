def divisor(n):
    return [a for a in range(1,n+1) if not n%a]

def sosulist(n):
    return [a for a in range(1,n+1) if len(divisor(a))==2]

def dividePrime(n):
    li = sosulist(n)
    rtn = []
    i = 0
    while n>1:
        if not n%li[i]:
            rtn.append(li[i])
            n //= li[i]
            continue
        i+=1
    return rtn

def mul(li):
    rtn = 1
    for i in li:
        rtn *= i
    return rtn


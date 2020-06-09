import random

def randlist(n=10, leng=100):
    r = [a for a in range(1,leng+1)]
    return random.sample(r, n)

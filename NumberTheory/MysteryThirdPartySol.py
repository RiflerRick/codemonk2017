from math import sqrt
from functools import lru_cache

@lru_cache(maxsize=None)
def getvalue(v):
    t = int(sqrt(v))
    print('t now: '+str(t))
    c = 2
    for i in range(2, t + 1):
        print("i: {} and c: {} ".format(i, c))
        if not v % i:
            c += 2
    print('c now: {}'.format(c))
    return c - 1 if t * t == v else c
def parse():
    for _ in range(int(input())):
        s = input()
        if " " in s:
            for v in map(int, s.split()):
                yield getvalue(v)
            break
        yield getvalue(int(s))
print(*parse(), sep="\n")
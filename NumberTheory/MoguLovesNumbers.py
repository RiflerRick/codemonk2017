def isprime(n):
    if n==1:
        return False
    """Returns True if n is prime."""
    if n == 2:
        return True
    if n == 3:
        return True
    if n % 2 == 0:
        return False
    if n % 3 == 0:
        return False

    i = 5
    w = 2

    while i * i <= n:
        # print('i*i at the beginning: '+str(i*i))
        if n % i == 0:
            return False

        i += w
        w = 6 - w
        # print('i and w at the end: '+str(i)+', '+str(w))
    return True

def sieve(n):
    visited=[]
    c=1
    for i in range(2, n+1):
        if i not in visited:
            j=i
            while j<n+1:
                if j not in visited:
                    visited.append(j)
                j+=2

def answer(l, r):
    c=0
    if l>r:
        for i in range(r, l+1):
            if isprime(i):
                c+=1
        print(c)
    else:
        for i in range(l,r+1):
            if isprime(i):
                c+=1 
        print(c)
# print(isprime(1))
q=int(input())
for i in range(q):
    l, r=input().split()
    answer(int(l),int(r))
"""
Test program to find all permutations of a number, Clearly for very large numbers this is not going to work because it is soon going to exceed the recursion depth.
"""
x=[]
def permute(a, l, r):
    if l==r:
        # yield a
        b=a[:]
        x.append(b)
    else:
        for i in range(l, r+1):
            a[l], a[i] = a[i], a[l]
            permute(a, l+1, r)
            a[l], a[i] = a[i], a[l] # this is essentially to back track, this is because you would need to revert the changes made in this function call in the stack to move up to the previous function call

t=int(input())
while t>0:
    n=int(input())
    if n==1:
        print(1)
        t-=1
        continue
    a=[]
    s=0
    maxS=0
    for i in range(1, n+1):
        a.append((i))
    
    permute(list(a), 0, n-1)
    for i in x:
        # print('wow')
        s=0
        for j in range(n-1):
            s+= abs(int(i[j])-int(i[j+1]))
            if s>maxS:
                maxS=s
                # combination=i
    del x[:]
    print(maxS)
    t-=1

# print('sum: {}'.format(maxS))
# print("combination: {}".format(combination))
    




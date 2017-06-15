"""
This solution of the problem will use the eratosthenes algorithm to generate prime numbers till r.
"""
# def answer1(l, r):
#     found=[]
#     count=0
#     for i in range(2, r+1):
#         if i not in found:
#             # print('prime found: '+str(i))
#             if i>=l:
#                 count+=1     
#             # it means clearly i is a prime number.
#             j=i*i
#             while j<=r:
                
#                 j+=i
#                 if j not in found:
#                     found.append(j)

#     del found
#     return count
a=[True]*int(1000000+1)
a[0]=a[1]=False

def answer(r=1000001):
    for i in range(r):
        # print ('i: {} and isprime: {}'.format(i, isprime))
        if a[i]:
            for n in range(i*i, r, i):     # Mark factors non-prime, remember that we are simply marking factors from i*i, not from i itself. This is important.
                a[n] = False

answer()
t=int(input())
count=0
while t>0:
    l, r=input().split()
    l=int(l)
    r=int(r)
    if l>r:
        temp=l
        l=r
        r=temp
    count=0
    for i in range(l, r+1):
        if a[i]:
            count+=1
    print(count)
    t-=1


            

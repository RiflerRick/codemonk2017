"""
Given an integer N. Find out the PermutationSum where PermutationSum for integer N is defined as the maximum sum of difference of adjacent elements in all arrangement of numbers from 1 to N.

NOTE: Difference between two elements A and B will be considered as abs(A-B) or |A-B| which always be a positive number.

Input:
First line of input contains number of test case T. Each test case contains a single integer N.

Output:
For each test case print the maximum value of PermutationSum.

Constraints:
1<=T<=10000
1<=N<=105
"""
def answer(n):
    s=0
    i=1
    j=2
    leftTerm=1
    rightTerm=n
    c=1
    while c<=n-1:
        if c%2!=0:
            # print('{}-{}, c now: {}'.format(leftTerm, rightTerm, c))
            s+=abs(leftTerm-rightTerm)
            i+=1
            leftTerm=rightTerm
            rightTerm=i

        else:
            # print('{}-{}, c now: {}'.format(leftTerm, rightTerm, c))
            s+=abs(leftTerm-rightTerm)
            leftTerm=rightTerm
            rightTerm=n-i+1
        c+=1
        
    return s

# print('answer: {}'.format(answer(4)))
t=int(input())
while t>0:
    n=int(input())
    if n==1:
        print(1)
    else:
        print(answer(n))
    t-=1
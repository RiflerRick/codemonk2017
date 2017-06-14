"""
The Monk wants to teach all its disciples a lesson about patience, since they are always in a hurry to do something crazy. To teach them this, he gives them a list of N numbers, which may or may not be distinct. The students are supposed to solve a simple Mathematical equation based on the array of these N numbers.

g(x) - GCD (a[ 0 ], a[ 1 ], a[ 2 ]... a[n-1] )
f(x) - (a[ 0 ] * a[ 1 ] * a[ 2 ]... * a[n-1] )
The value of the MonkQuotient is: 109 + 7.

The equation to be solved is: ( f(x)g(x) ) modulo MonkQuotient

Input constraints:
The first line of input will contain an integer — N. The next line will contain N integers denoting the elements of the list.

Output constraints:
Print the required answer of the equation.

Constraints:
1 ≤ N ≤ 50 
1 ≤ Ai ≤ 103
"""

def gcd(a, b):
    if b==0:
        return a
    else:
        return gcd(b, a%b)

def multiply(l):
    ans=1
    for i in range(len(l)):
        ans*=int(l[i])

    return ans

def answer(f, g, M):
    if g==0:
        return 1
    if g%2==0:
        # g is even
        return answer((f*f)%M , g/2, M)
    else:
        return (f* answer((f*f)%M, (g-1)/2, M)%M)

def main():
    n=int(input())
    l=input().strip().split()
    a=int(l[0])
    for i in range(1,n):
        a=gcd(a, int(l[i]))
    
    f=multiply(l)
    g=a
    print(answer(f,g, 10**9 + 7))



if __name__=="__main__":
    main()

    
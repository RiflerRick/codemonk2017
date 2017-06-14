"""
This solution uses a very efficient method of finding out whether a number is prime or not.
This algorithm is really fast for finding if a number is prime or not.
The loop part is executed for numbers greater then 25. We start from 5 and alternately add 2 and 4 at each step. Remember that primes are always in the form 6k+1 or 6k-1. For this one if we start from 5, this would be 5 , (5+2), (5+2+4), (5+2+4+2) and so on. 

One primality test is that for checking whether a number p is prime or not. First find the smallest value of n such that n*n<=p. Now check if p is divisible by any number less than n. If so then p is prime or not. 
"""

def isprime(n):
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
        print('i*i at the beginning: '+str(i*i))
        if n % i == 0:
            return False

        i += w
        w = 6 - w
        print('i and w at the end: '+str(i)+', '+str(w))
    return True

def answer(n):
    if n==0:
        return 2
    elif n==1:
        return 1
    if isprime(n):
        return 0
    num=n-1
    while True:
        # finding the previous prime number
        if isprime(num):
            prevPrime=num
            break
        num-=1

    num=n+1
    while True:
    
        if isprime(num):
            nextPrime=num
            break
        num+=1

    dif1=abs(prevPrime-n)
    dif2=abs(nextPrime-n)
    if dif1<dif2:
        return dif1
    else:
        return dif2

def main():
    # a=int(input())
    # print(answer(a))
    print(isprime(103))
    

if __name__=="__main__":
    main()

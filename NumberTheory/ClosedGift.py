"""
You are on your way to find the gifts. All the gifts lie in your path in a straight line at prime numbers and your house is at 0.Given your current position find the closest gift to your position, and calculate the distance between your current position and gift and tell the distance.
"""

"""
Problem solved using sieve of eratosthenes, however this is inefficient when it comes to using very large numbers.
"""
def answer(n):
    if n==0:
        return 2
    elif n==1:
        return 1
    elif n==2:
        return 0
    else:
        visited=[]
        prime=[]
        num=2
        flag=0
        flag2=0
        val=n
        while True:
            n=n*2
            while num<=n:
                # print('prime now: '+str(prime))
                # print('visited now: ' +str(visited))
                if num not in visited:
                    if flag==1:
                        nextPrime=num
                        flag2=1
                        break
                    i=num
                    while i<=n:
                        if i not in visited: # i may already be in visited because i may have been entered as multiples of another number. For example 6 is multiple of 2 and 3
                            visited.append(i)
                        i=i+num
                    prime.append(num)

                
                if num==val:
                    prevPrime=prime.pop() # the last number that went in
                    if prevPrime==val:
                        return 0
                    flag=1
                num+=1

            if flag2==1:
                break
        
        # print('prevPrime: '+str(prevPrime)+ ' , nextPrime: '+str(nextPrime))

        dif1=abs(nextPrime-val)
        dif2=abs(prevPrime-val)
        if dif1>dif2:
            return dif2
        else:
            return dif1
        # print (prevPrime)
        # return prevPrime

def main():
    a=int(input())
    print(answer(a))

if __name__=="__main__":
    main()

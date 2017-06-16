"""
James has decided to take a break from his work. He makes a plan to visit India for a few days with his family. He knows a lot about India, and also about the various cities he could visit. He decides to write down all the cities on a paper. Let the number of cities be n. Now, he shows the list to his wife and asks her, the city/cities she wants to visit. He tells her that she can select any city/cities and any number of cities. The wife says, she needs a day to decide.

After this, James calls his son and tells him all about the trip, and the list of cities. He gives him a task and asks him, the number of ways the city/cities can be chosen from the list, if the total number of cities written on the list is n. The cities are numbered from 1 to n. At least 1 city has to be selected.

He now asks your help to find the answer for the question that was asked to him. 
The problem consists of a number of test cases.

Solution: Clearly this is a combination problem.
The solution would be: nC1 + nC2 + nC3 + ... + nCn = 2**n -1. This is a mathematical result.

Since the result can be very big, if we try a traditional solution using math.pow(), it wont work and we would get overflow errors.
So the solution is using the basic idea that a**b= (a*b/2)**2
"""
import math
moduloVal=10**9+7

def answer(ans, n):
    if n==0:
        return 1
    if n%2==0: # n is even
        return answer((ans*ans) % moduloVal, n/2)
    else:# n-1 is even 
        return (ans * answer((ans*ans)%moduloVal, (n-1)/2))% moduloVal

t=int(input())
while t>0:
    n=int(input())
    a=answer(2, n)-1
    print (a)
    t-=1


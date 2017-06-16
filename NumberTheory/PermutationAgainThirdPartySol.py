"""
This is undoubtedly the best solution for this problem, it again uses proper math to solve the problem. It is observation actually. For instance consider the number 5, how do we get the answer for the number 5.

Our original solution was actually pretty close to the real solution. Only thing that was remaining was the math behind it.
For instance, lets consider the number 5 and try and find the highest sum for differences of all possible permutations of consecutive numbers. So first we take the least number on our disposal: 1. With 1 the number that can give the highest difference is the highest number 5. So the sequence goes 1,5. The next number that can give the highest difference with 5 is 2, so 1, 5, 2. the next number that can give highest difference with 2 is 4 and then 3, so we get 1, 5, 2, 4, 3: This gives us the answer as 10. However the real answer is 11 that is obtained by shifting the 3 from the last position to the first position. So we get 3, 1, 5, 4, 2. This gives answer 11. 

Here the observation part comes in:
|1-5|: 4, |5-2|: 3, |2-4|: 2, |4-3|: 1; so we are essentially doing 1+2+3+4 or for any value n, we are doing 1+2+3+4+...+n-1 = n*(n-2)/2. This is the first observation. 
However this solution ain't correct just yet.
remember we bring the last 3 to the front. This means we are addding the last number found in each case to the front of the list. Thus an extra |3-5| and removing that 1 from the end. In this case the net result is an extra 1. This is the crux of the problem right here. Hence we get, the number to be added in the front will be int(n/2). Calculating we get the formula as n*n/2 -1.

Its an excellent observation
"""
t=int(input())
while t>0:
    n=int(input())
    if n==1:
        print(1)
        t-=1
        continue
    val=int(n*n/2)-1
    print(val)
    t-=1
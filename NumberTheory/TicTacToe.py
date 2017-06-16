"""
King Tle4Ever of Time Limit Exceeded is really fascinated about Tic Tac Toe. He organizes a national level contest for Tic Tac Toe every year in Time Limit Exceeded. (Though I agree you need to be really stupid to loose a game of Tic Tac Toe but for the sake of question assume playing Tic Tac Toe for them is same as playing Chess for us :P ). 

Every year the contest has lots of participants. This year there are n participants from all over the country. Seeing this huge participation he asks Moron a simple question.

Suppose participant pi wins wi matches. The king wants to know the sum of wi2 from 1 to n. Now as you already 
know Moron is not good with maths, he asks you to help him.

Given the value of n find the minimum and maximum value of sum of wi2 from 1 to n. As values can be too large output the values mod 10**9+7.

From the question unfortunately it is not very clear what is to be done. The following tells what is to be done.
Brilliant Question ! 
Good practice for modulo under divide condition 
Question Explanation : 
for n=3
There are 3 participants : A B C , They compete against each other , A-B , A-C , B-C , ( 3c2 combinations )
wi be the number of matches won by ith player , here : w1 means number of matches won by A
now : (Sigma) wi^2 will be maximum if the results of the matches are such that :
A-B : A wins
A-C : A wins
B-C : B wins
here : w1=2 , w2=1 , w3=0
(Sigma) wi^2 = 1^2+2^2 = 5
now : (Sigma) wi^2 will be minimum if : 
A-B : A wins
B-C : B wins
A-C : C wins
wi=1 for all i=1,2,3
(Sigma) wi^2 = 3
"""

"""
Probable solution:
Clearly one thing we can say that the number of games to be played are nC2. 
One probable max is the following: If there are n players then the idea is that every player will play with every other player in the competition. Now lets assume that the first player wins against every other player. This means he will win a total of (n-1) matches as he will play those many matches. Now the second player mind you also plays (n-1) matches(i.e against every other player). However the first player has beaten him. So he will win against the rest (n-2) players. Like wise we wil get the sequence: (n-1)**2 + (n-2)**2 + (n-3)**2 + ...+ 1**2. That is the sum of squares of all numbers till n-1.

Recall that the sum of squares of all numbers upto n is = (n)(n+1)(2n+1)/6. So for the first n-1 numbers = 
(n-1)(n)(2(n-1)+1)/6 = (n-1)(n)(2n-1)/6

Now for the minimum part:
One probable solution could be to use n*((n-1)/2)**2. Assuming that each player actually wins half the games that he plays.

"""
modVal=10**9+7
def answer(n):
    # term=int(n*(n-1)*(2*n-1)) 
    # maxNum=int((term)/6) % modVal # one interesting idea is that n*(n+1)*(2n+1) is always divisible by
    maxNum=getMaxVal(n)
    minNum=(n*(int((n-1)/2)**2))%modVal
    return minNum, maxNum

def getMaxVal(n):
    val=0
    # for i in range(1, n):
    #     val=(val+((n-i)*(n-i))%modVal)%modVal

    val=int((n*(n+1)*(2*n+1))/6) % modVal
    # print(val)
    # val%=modVal
    # print('after modVal: {}'.format(val))
    val-=((n*n))%modVal
    # print('val after negating n**2: {}'.format(val))
    val%=modVal
    # print('after modVal again: {}'.format(val))
    return val

t=int(input())
while t>0:
    n=int(input())
    ans=answer(n)
    print('{} {}'.format(int(ans[0]), int(ans[1])))
    t-=1
# ----#3918----
def isPrime(x:int):
    if x in [2,3,5,7]:
        return True
    if x==1 or 0 in [x%2,x%3,x%5]: 
        return False
    y=6
    while y*y<=x:
        if not x%(y+1):
            return False
        elif not x%(y+5):
            return False
        y+=6
    return True
# ----#3918----
cache=[0]*1001
for x in range(1,1001):
    if isPrime(x): 
        cache[x]=x
    cache[x]+=cache[x-1]

class Solution:
    '''
    3918. Sum of Primes Between Number and Its Reverse

    You are given an integer n.
    Let r be the integer formed by reversing the digits of n.
    Return the sum of all prime numbers between min(n, r) and max(n, r), inclusive.
    
    Example 1:
    Input: n = 13
    Output: 132
    Explanation:
    The reverse of 13 is 31. Thus, the range is [13, 31].
    The prime numbers in this range are 13, 17, 19, 23, 29, and 31.
    The sum of these prime numbers is 13 + 17 + 19 + 23 + 29 + 31 = 132.

    Constraints:
    1 <= n <= 1000
    '''
    def sumOfPrimesInRange(self, n: int) -> int:
        r=int(''.join([*str(n)][::-1]))
        return cache[max(n,r)]-cache[min(n,r)-1]

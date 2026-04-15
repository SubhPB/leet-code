class Solution:
    '''
    3881. Direction Assignments with Exactly K Visible People
    You are given three integers n, pos, and k.
    There are n people standing in a line indexed from 0 to n - 1. Each person independently chooses a direction:
    'L': visible only to people on their right
    'R': visible only to people on their left
    A person at index pos sees others as follows:
    A person i < pos is visible if and only if they choose 'L'.
    A person i > pos is visible if and only if they choose 'R'.
    Return the number of possible direction assignments such that the person at index pos sees exactly k people.

    Since the answer may be large, return it modulo 109 + 7.
    
    Example 1:
    Input: n = 3, pos = 1, k = 0
    Output: 2
    Explanation:​​​​​​​
    Index 0 is to the left of pos = 1, and index 2 is to the right of pos = 1.
    To see k = 0 people, index 0 must choose 'R' and index 2 must choose 'L', keeping both invisible.
    The person at index 1 can choose 'L' or 'R' since it does not affect the count. Thus, the answer is 2.

    Constraints:
    1 <= n <= 10^5
    0 <= pos, k <= n - 1
    '''
    def exp(self, i:int,mod:int):
        r=1; b=i; p=mod-2
        while p>0:
            if p%2: r=(r*b)%mod
            b=(b*b)%mod
            p>>=1
        return r
    def countVisiblePeople(self, n: int, pos: int, k: int) -> int:
        mod=10**9+7; u=1; b=1; k=min(k,n-1-k)
        for i in range(1,1+k):
            u=(u*(n-i))%mod
            b=(b*i)%mod
        return (2*(self.exp(b,mod)*u)%mod)%mod
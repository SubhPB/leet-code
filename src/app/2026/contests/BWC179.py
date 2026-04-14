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
    def __init__(self):
        self.perm=[1]*(10**5+1)
        self.mod=10**9+7
        for i in range(2,10**5+1):
            self.perm[i]=(i%self.mod * self.perm[i-1]%self.mod)%self.mod
    def exp(self,b:int,p:int): # log(n)
        r=1
        while p>0:
            if p%2: r=self.mul(r,b)
            b=self.mul(b,b)
            p>>=1
        return r
    def add(self,a:int,b:int):
        return (a%self.mod + b%self.mod)%self.mod
    def mul(self,a:int,b:int):
        return (a%self.mod * b%self.mod)%self.mod
    def C(self,n,r):
        if n<=r: return 0
        return self.mul(
                self.mul(
                    self.perm[n],
                    self.exp(self.perm[n-r], self.mod-2)
                    ),
                self.exp(self.perm[r],self.mod-2)
            )
    def countVisiblePeople(self, n: int, pos: int, k: int) -> int:
        res=0
        if pos not in [0,n-1]:
            for i in range(min(pos,k)):
                res=self.add(
                    res,
                    self.mul(
                        self.C(pos,i), self.C(n-pos-1,k-i)
                    )
                )
        return self.mul(2,res)
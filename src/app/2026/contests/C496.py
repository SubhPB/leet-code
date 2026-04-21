
'''#3890:cache'''
N=10**9; x=0; k=0
pows=[]; frq={}

while k+1<=N:
    pows.append(k)
    x+=1; k=x**3

ans=[]; m=len(pows)
for i in range(m):
    for j in range(i+1):
        k=pows[i]+pows[j]
        frq[k]=1+frq.get(k,0)
        if frq[k]==2: 
            ans.append(pows[i]+pows[j])
z=len(ans); ans.sort()
'''#3890'''

class Solution:
    '''
    3890. Integers With Multiple Sum of Two Cubes

    You are given an integer n.
    An integer x is considered good if there exist at least two distinct pairs (a, b) such that:
    a and b are positive integers.
    a <= b
    x = a3 + b3
    Return an array containing all good integers less than or equal to n, sorted in ascending order.
    Example 1:
    Input: n = 4104
    Output: [1729,4104]
    Explanation:
    Among integers less than or equal to 4104, the good integers are:
    1729: 13 + 123 = 1729 and 93 + 103 = 1729.
    4104: 23 + 163 = 4104 and 93 + 153 = 4104.
    Thus, the answer is [1729, 4104].

    
    Constraints:
    1 <= n <= 10**9
    '''
    def findGoodIntegers(self, n: int) -> list[int]:
        l=-1;r=z
        while l<r:
            m=(l+r+1)//2
            if ans[m]<=n: l=m
            else: r=m-1
        return ans[:l+1]
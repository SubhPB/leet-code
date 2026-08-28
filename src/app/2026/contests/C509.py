
class Solution:
    '''
    3983. Subsequence After One Replacement
    You are given two strings s and t consisting of lowercase English letters.
    You may choose at most one index in s and replace the character at that index with any lowercase English letter.
    Return true if it is possible to make s a subsequence of t; otherwise, return false.

    Example 1:
    Input: s = "cat", t = "chat"
    Output: true
    Explanation:
    Replace s[1] from 'a' to 'h'. The resulting string is "cht".
    "cht" is a subsequence of "chat" because we can match 'c', 'h', and 't' in order.

    Constraints:
    1 <= s.length, t.length <= 10**5
    s and t consist only of lowercase English letters.
    '''
    def canMakeSubsequence(self, s: str, t: str) -> bool:
        n=len(s)
        m=len(t)

        if n>m: return False
        elif not n-1: return True

        left=[-1]*n
        at=0

        for i,c in enumerate(t):      
            if c==s[at]: 
                left[at]=i
                at+=1
            if at==n: return True

        right=[-1]*n; at=n-1
        for i in range(m-1,-1,-1):
            if s[at]==t[i]:
                right[at]=i
                at-=1
            # note at==0 is not possible bcz left[n-1]=-1
        
        for i in range(n):
            # replacing ith idx
            if i==0:
                r=right[i+1]
                if r>0: return True
            elif i==n-1:
                l=left[i-1]
                if -1<l<m-1: return True
            else:
                l=left[i-1]; r=right[i+1]
                if -1<l<r-1:
                    return True

        return False
    '''
    3984. Divisible Game

    You are given an integer array nums of length n.
    Alice and Bob are playing a game. Alice chooses:
    An integer k such that k > 1.
    Two integers l and r such that 0 <= l <= r < n.
    Initially, both Alice's and Bob's scores are 0.
    For each index i in the range [l, r] (inclusive):
    If nums[i] is divisible by k, Alice's score increases by nums[i].
    Otherwise, Bob's score increases by nums[i].
    The score difference is Alice's score minus Bob's score.
    Alice wants to maximize the score difference. If there are multiple values of k that achieve the maximum score difference, she chooses the smallest such k.
    Return the product of the maximum score difference and the chosen value of k. Since the result can be large, return it modulo 1e9 + 7.

    Example 1:
    Input: nums = [1,4,6,8]
    Output: 36
    Explanation:

    Alice can choose k = 2, l = 1, and r = 3.
    All values in nums[1..3] are divisible by 2, so Alice's score is 4 + 6 + 8 = 18, while Bob's score is 0.
    The score difference is 18, which is the maximum possible. Among all values of k that achieve this score difference, the smallest is 2.
    Therefore, the answer is 18 * 2 = 36.

    Constraints:
    1 <= nums.length <= 1000
    1 <= nums[i] <= 10**6
    '''
    def divisibleGame(self, nums: list[int]) -> int:
        st=set(); st.add(2)
        for num in nums:
            k=1
            while k*k<=num:
                if not num%k: 
                    if k>1: st.add(k)
                    if num//k>1: st.add(num//k)
                k+=1

        mod=10**9+7
        add=lambda a,b: (a%mod + b%mod)%mod
        mul=lambda a,b: (a%mod * b%mod)%mod

        mxscore=None; kcurr=2
        for k in st:
            score=None
            total=0
            mn=0
            for num in nums:
                if num%k:
                    total-=num
                else: 
                    total+=num

                if score is None: score=total
                score=max(score,total-mn)
                mn=min(mn,total)
            if mxscore is None or score>mxscore:
                mxscore=score
                kcurr=k
            elif score==mxscore:
                kcurr=min(kcurr,k)
            
        return mul(kcurr,mxscore)
    '''
    3985. Palindromic Subarray Sum

    You are given an integer array nums.
    Return the maximum possible sum of a subarray of nums that is a palindrome.

    Example 1:
    Input: nums = [10,10]
    Output: 20
    Explanation:
    The whole array [10,10] is a palindrome. Therefore, the maximum sum is 10 + 10 = 20.

    Constraints:
    1 <= nums.length <= 10**5
    1 <= nums[i] <= 10**​​​​​​​9
    '''
    def getSum(self, nums: list[int]) -> int:
        pass
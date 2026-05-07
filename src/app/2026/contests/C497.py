class Solution:
    '''
    3900. Longest Balanced Substring After One Swap

    You are given a binary string s consisting only of characters '0' and '1'.
    A string is balanced if it contains an equal number of '0's and '1's.
    You can perform at most one swap between any two characters in s. Then, you select a balanced substring from s.
    Return an integer representing the maximum length of the balanced substring you can select.

    Example 1:
    Input: s = "100001"
    Output: 4
    Explanation:
    Swap "100001". The string becomes "101000".
    Select the substring "101000", which is balanced because it has two '0's and two '1's.

    Constraints:
    1 <= s.length <= 10**5
    s consists only of the characters '0' and '1'.
    '''
    def longestBalanced(self, s: str) -> int:

        n=len(s); res=0
        u0=n; u1=-1
        v0=n; v1=-1
        for i,b in enumerate(s):
            if int(b):
                u0=min(u0,i); u1=max(u1,i)
            else:
                v0=min(v0,i); v1=max(v1,i)
        
        df={}; Δc=0 # Δc=Δp+Δt
        #df[Δp]: segment [initial occrance, contains '0', contains '1']
        df[Δc]=[-1,n,n] 

        for i,b in enumerate(s):
            if int(b): Δc+=1
            else: Δc-=1

            # Δt:0 -> Δp:Δc
            res=max(res, i-df.get(Δc,[i])[0])
            # Δt:-2 {u<v} -> Δc:Δp-2
            [j,v,u]=df.get(Δc+2,[i,n,n])
            if i<u1: res=max(res,i-j)
            res=max(res,i-u)
            # Δt:2 {u>v} -> Δc:Δp+2
            [j,v,u]=df.get(Δc-2,[i,n,n])
            if i<v1: res=max(res,i-j)
            res=max(res,i-v)
            
            if Δc not in df: df[Δc]=[i,n,n]
            if i>=v0: df[Δc][1]=min(df[Δc][1],i)
            if i>=u0: df[Δc][2]=min(df[Δc][2],i)
        return res
    '''
    3901. Good Subsequence Queries

    You are given an integer array nums of length n and an integer p.
    A non-empty subsequence of nums is called good if:
    Its length is strictly less than n.
    The greatest common divisor (GCD) of its elements is exactly p.
    You are also given a 2D integer array queries of length q, where each queries[i] = [indi, vali] indicates that you should update nums[indi] to vali.
    After each query, determine whether there exists any good subsequence in the current array.
    Return the number of queries for which a good subsequence exists.
    The term gcd(a, b) denotes the greatest common divisor of a and b.
    
    Example 1:
    Input: nums = [4,8,12,16], p = 2, queries = [[0,3],[2,6]]
    Output: 1
    Explanation:
    i	[indi, vali]	Operation	Updated nums	Any good Subsequence
    0	[0, 3]	Update nums[0] to 3	[3, 8, 12, 16]	No, as no subsequence has GCD exactly p = 2
    1	[2, 6]	Update nums[2] to 6	[3, 8, 6, 16]	Yes, subsequence [8, 6] has GCD exactly p = 2
    Thus, the answer is 1.

    Constraints:
    2 <= n == nums.length <= 5 * 10^4
    1 <= nums[i] <= 5 * 104
    1 <= queries.length <= 5 * 10^4
    queries[i] = [indi, vali]
    1 <= vali, p <= 5 * 10^4
    0 <= indi <= n - 1
    '''
    def countGoodSubseq(self, nums: list[int], p: int, queries: list[list[int]]) -> int:
        pass
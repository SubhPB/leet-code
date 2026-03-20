class Solution:
    '''
    3862. Find the Smallest Balanced Index
    You are given an integer array nums.
    An index i is balanced if the sum of elements strictly to the left of i equals the product of elements strictly to the right of i.
    If there are no elements to the left, the sum is considered as 0. Similarly, if there are no elements to the right, the product is considered as 1.
    Return an integer denoting the smallest balanced index. If no balanced index exists, return -1.

    Example 1:
    Input: nums = [2,1,2]
    Output: 1

    Constraints:
    1 <= nums.length <= 10^5
    1 <= nums[i] <= 10^9
    '''
    def smallestBalancedIndex(self, nums: list[int]) -> int:
        γ=-1;Σ=sum(nums);Π=1;x=10**18;n=len(nums)
        for i in range(n-1,-1,-1):
            Σ-=nums[i]
            if Σ==Π:γ=i
            Π*=nums[i]
            if Π>x: break
        return γ
    '''
    3863. Minimum Operations to Sort a String
    You are given a string s consisting of lowercase English letters.
    In one operation, you can select any substring of s that is not the entire string and sort it in non-descending alphabetical order.
    Return the minimum number of operations required to make s sorted in non-descending order. If it is not possible, return -1.

    Example 1:
    Input: s = "dog"
    Output: 1

    1 <= s.length <= 10^5
    s consists of only lowercase English letters.
    '''
    def minOperations(self, s: str) -> int:
        n=len(s);sm='z';lg='a'
        res=3;b=True

        if n<=2: return -1 if s[0]>s[-1] else 0
        for i in range(1,n-1):
            b&=(s[i-1]<=s[i]<=s[i+1])
            if sm>s[i]:sm=s[i]
            if lg<s[i]:lg=s[i]

        if b: return 0
        elif s[i]<=sm and s[i]<=s[-1]: return 1
        elif s[-1]>=lg and s[-1]>=s[0]: return 1

        def fn(x,y,z):
            ops=0;v=list((x,y,z))
            for i in [1,2,1]:
                if v[i]<v[i-1]:
                    v[i],v[i-1]=v[i-1],v[i]
                    ops+=1
            return ops
        
        if s[i]>sm:
            res=min(res,1+fn(sm,lg if lg>s[i] else s[i],s[-1]))
        if lg>s[-1]:
            res=min(res,1+fn(s[0],sm if sm<s[-1] else s[-1],lg))

        return res
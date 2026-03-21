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
        n=len(s);b=1
        if n<=2:
            return -1 if s[0]>s[-1] else 0
        sm=ord('z');lg=ord('a')
        for i in range(1,n-1):
            b&=int(s[i]>=s[max(1,i-1)])
            sm=min(sm,ord(s[i]))
            lg=max(lg,ord(s[i]))
        x=ord(s[0]);z=ord(s[-1])
        def calc(x:int,y:int,z:int):
            nums=list((x,y,z));ops=0
            for i in [1,2,1]:
                if nums[i]<nums[i-1]:
                    nums[i],nums[i-1]=nums[i-1],nums[i]
                    ops+=1
            return ops
        if n==3: 
            return calc(x,sm,z)
        elif b:
            if x<=sm: return calc(x,lg,z)
            else: return calc(max(x,lg),sm,z)
        return 1+min(
            calc(min(x,sm),max(x,lg),z),
            calc(x,min(sm,z),max(lg,z))
        )
            

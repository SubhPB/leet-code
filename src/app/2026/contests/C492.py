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
        
    '''
    3864. Minimum Cost to Partition a Binary String

    You are given a binary string s and two integers encCost and flatCost.
    For each index i, s[i] = '1' indicates that the ith element is sensitive, and s[i] = '0' indicates that it is not.
    The string must be partitioned into segments. Initially, the entire string forms a single segment.
    For a segment of length L containing X sensitive elements:

    If X = 0, the cost is flatCost.
    If X > 0, the cost is L * X * encCost.
    If a segment has even length, you may split it into two contiguous segments of equal length and the cost of this split is the sum of costs of the resulting segments.
    Return an integer denoting the minimum possible total cost over all valid partitions.

    Example 1:
    Input: s = "1010", encCost = 2, flatCost = 1
    Output: 6
    Explanation:
    The entire string s = "1010" has length 4 and contains 2 sensitive elements, giving a cost of 4 * 2 * 2 = 16.
    Since the length is even, it can be split into "10" and "10". Each segment has length 2 and contains 1 sensitive element, so each costs 2 * 1 * 2 = 4, giving a total of 8.
    Splitting both segments into four single-character segments yields the segments "1", "0", "1", and "0". A segment containing "1" has length 1 and exactly one sensitive element, giving a cost of 1 * 1 * 2 = 2, while a segment containing "0" has no sensitive elements and therefore costs flatCost = 1.
    ​​​​​​​The total cost is thus 2 + 1 + 2 + 1 = 6, which is the minimum possible total cost.

    Constraints:
    1 <= s.length <= 10^5
    s consists only of '0' and '1'.
    1 <= encCost, flatCost <= 10^5
    '''
    def minCost(self, s: str, encCost: int, flatCost: int) -> int:
        n=len(s); pf=[0]*(n+1)
        for i in range(n): pf[i]+=pf[i-1]+int(s[i])
        def minfn(l:int,r:int):
            nonlocal pf,n,s,encCost,flatCost
            m=r-l+1; x=pf[r]-pf[l-1]
            if not x: return flatCost
            elif m%2: return m*x*encCost
            return min(
                m*x*encCost,
                minfn(l,(l+r)//2)
                + minfn(1+(l+r)//2, r)
            )
        return minfn(0,n-1)
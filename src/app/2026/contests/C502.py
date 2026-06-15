class Solution:
    '''
    3932. Count K-th Roots in a Range

    You are given three integers l, r, and k.
    An integer y is said to be a perfect kth power if there exists an integer x such that y = xk.
    Return the number of integers y in the range [l, r] (inclusive) that are perfect kth powers.

    Example 1:
    Input: l = 1, r = 9, k = 3
    Output: 2
    Explanation:
    The perfect cubes in the range [1, 9] are:
    1 = 13
    8 = 23
    Hence, the answer is 2.

    Constraints:
    0 <= l <= r <= 10**9
    1 <= k <= 30
    '''
    def countKthRoots(self, l: int, r: int, k: int) -> int:
        i=0;ls=[]
        while i**k <= r:
            ls.append(i)
            i+=1
        left=-1;right=len(ls)-1
        while left<right:
            m=(left+right+1)//2
            if ls[m]<l:
                left=m
            else:
                right=m-1
        res=right
        left=-1; right=len(ls)-1
        while left<right:
            m=(left+right+1)//2
            if ls[m]<=r:
                left=i
            else:
                right=i-1
        return left-res
import math
from collections import defaultdict

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
    def countKthRoots(self, l: int, r: int, k: int) -> int: # n+2O(log(n))
        if k==1: return r-l+1
        i=0;ls=[]
        while i**k<=r:
            ls.append(i**k)
            i+=1
        left=-1;right=len(ls)-1
        while left<right:
            m=(left+right+1)//2
            if ls[m]<l:
                left=m
            else:
                right=m-1
        res=left
        left=-1; right=len(ls)-1
        while left<right:
            m=(left+right+1)//2
            if ls[m]<=r:
                left=m
            else:
                right=m-1
        return left-res
    def countKthRootsII(self, l: int, r: int, k: int) -> int: # O(1)
        l=math.ceil(l**(1/k) - 1e-9); r=math.floor(r**(1/k) + 1e-9)
        return (r-l)+1

    '''
    3933. Largest Local Values in a Matrix II

    You are given an n x m integer matrix matrix containing non-negative integers.
    A non-zero cell (row, col) checks the cells near it as follows:
    Let x = matrix[row][col].
    Consider every cell within x rows and x columns of (row, col).
    Ignore cells that are outside the matrix.
    Ignore the cells where both the row distance and column distance are exactly x.
    The cell (row, col) is a local maximum if it is non-zero and no considered cell has a value greater than x.
    Return an integer denoting the number of local maximums in matrix.

    ​​​​​​​Example 1:
    Input: matrix = [[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,2,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0]]
    Output: 1

    ​​​​​​​​​​​​​​​​​​​
    Explanation:
    For the non-zero cell (3, 3), x = matrix[3][3] = 2.
    The highlighted cells are the considered cells within x rows and x columns of (3, 3).
    The four cells with both row and column distances equal to x = 2 are ignored.
    No considered cell has a value greater than 2, so (3, 3) is a local maximum.
    There are no other non-zero cells, so the answer is 1.

    Constraints:
    1 <= n == matrix.length <= 200
    1 <= m == matrix[i].length <= 200
    0 <= matrix[i][j] <= 200
    '''
    def countLocalMaximums(self, matrix: list[list[int]]) -> int:
        res=0;n=len(matrix);m=len(matrix[0])
        q=[[i,j] for j in range(m) for i in range(n)]
        q.sort(key=lambda x:-matrix[x[0]][x[1]])
        for [i,j] in q:
            val=(matrix[i][j])
            if val>0:
                mx=i;my=j
                for x in range(
                  max(0,i-val),min(n,i+val+1)   
                ):
                    for y in range(
                        max(0,j-val),min(m,j+val+1)
                    ):
                        if x in (i+val,i-val) and y in (j+val,j-val) and (x,y)==(i,j):
                            continue
                        if val<abs(matrix[x][y]):
                            mx=x;my=y
                        if val!=matrix[x][y]:
                            matrix[x][y]=min(
                                matrix[x][y],-matrix[x][y]
                            )
                if (i,j)==(mx,my): res+=1
        return res
    '''
    3934. Smallest Unique Subarray

    You are given an integer array nums.
    Find the minimum length of a subarray that is not identical to any other subarray in nums.
    Return an integer denoting the minimum possible length of such a subarray.
    Two subarrays are considered identical if they have the same length and the same elements in corresponding positions.

    Example 1:
    Input: nums = [3,3,3]
    Output: 3
    Explanation:
    Subarrays of length 1: [3] → appears 3 times
    Subarrays of length 2: [3, 3] → appears 2 times
    Subarrays of length 3: [3, 3, 3] → appears once
    The subarray [3, 3, 3] is unique, so the smallest unique subarray length is 3.

    Constraints:
    1 <= nums.length <= 10**5
    1 <= nums[i] <= 10**5
    '''
    def smallestUniqueSubarray(self, nums: list[int]) -> int:
        n=len(nums); bse1=10**9+7; bse2=bse1+2
        add = lambda x,y,mod: (x%mod + y%mod)%mod
        mul = lambda x,y,mod: (x%mod * y%mod)%mod

        def λ(l:int):
            hsh1=0;hsh2=0 
            pm1=37; pm2=39
            pw1=pm1; pw2=pm2
            # hash = E(1<=i<=l) e[i]*b[n-i]
            for i in range(l-2,-1,-1): #imp:note range
                hsh1=add(
                    hsh1,
                    mul(nums[i],pw1,bse1),
                    bse1
                )
                pw1=mul(pw1,pm1,bse1)

                hsh2=add(
                    hsh2,
                    mul(nums[i],pw2,bse2),
                    bse2
                )
                pw2=mul(pw2,pm2,bse2)
            
            fq=defaultdict()
            for i in range(l-1,n):
                hsh1=add(hsh1,nums[i],bse1)
                hsh2=add(hsh2,nums[i],bse2)

                enc=str(hsh1)+'.'+str(hsh2)
                fq[enc]=1+fq.get(enc,0)
                
                hsh1=mul(
                    hsh1-mul(nums[i-l+1],pw1,bse1),
                    pm1,
                    bse1
                )

                hsh2=mul(
                    hsh2-mul(nums[i-l+1],pw2,bse2),
                    pm2,
                    bse2
                )
            for ky in fq:
                if fq[ky]==1:
                    return True
            return False

        l=1;r=n
        while l<r:
            m=(l+r)//2
            if λ(m): r=m
            else: l=m+1
        return l
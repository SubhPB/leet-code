import math
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
        for i in range(n):
            for j in range(m):
                val=matrix[i][j]; bl=val==0
                for k in range(
                    max(0,i-val),min(n,i+val+1)
                ):
                    if bl: break
                    for l in range(
                        max(0,j-val),min(m,j+val+1)
                    ):
                        if k in (i+val,i-val) and l in (j+val,j-val):
                            continue
                        if matrix[k][l]>val:
                            bl=True
                            break
                if not bl:
                    res+=1
        return res




'''
3480. Maximize Subarrays After Removing One Conflicting Pair

    You are given an integer n which represents an array nums containing the numbers from 1 to n in order. Additionally, you are given a 2D array conflictingPairs, where conflictingPairs[i] = [a, b] indicates that a and b form a conflicting pair.

    Remove exactly one element from conflictingPairs. Afterward, count the number of non-empty subarrays of nums which do not contain both a and b for any remaining conflicting pair [a, b].

    Return the maximum number of subarrays possible after removing exactly one conflicting pair.
    Example 1:

    Input: n = 4, conflictingPairs = [[2,3],[1,4]]

    Output: 9

    Explanation:

    Remove [2, 3] from conflictingPairs. Now, conflictingPairs = [[1, 4]].
    There are 9 subarrays in nums where [1, 4] do not appear together. They are [1], [2], [3], [4], [1, 2], [2, 3], [3, 4], [1, 2, 3] and [2, 3, 4].
    The maximum number of subarrays we can achieve after removing one element from conflictingPairs is 9.
    Example 2:

    Input: n = 5, conflictingPairs = [[1,2],[2,5],[3,5]]

    Output: 12

    Explanation:

    Remove [1, 2] from conflictingPairs. Now, conflictingPairs = [[2, 5], [3, 5]].
    There are 12 subarrays in nums where [2, 5] and [3, 5] do not appear together.
    The maximum number of subarrays we can achieve after removing one element from conflictingPairs is 12.

    Constraints:

    2 <= n <= 10^5
    1 <= conflictingPairs.length <= 2 * n
    conflictingPairs[i].length == 2
    1 <= conflictingPairs[i][j] <= n
    conflictingPairs[i][0] != conflictingPairs[i][1]

    python ./src/app/2025/July/3480.py
'''
from typing import List
from collections import defaultdict
class Solution:
    def maxSubarrays(self, n: int, conflictingPairs: List[List[int]]) -> int:
        lp = lambda x: (x*(x+1))//2
        lpRange = lambda x,y: lp(y) - lp(max(x-1,0))
        visited = set(); res = 0; default = lp(n)
        for pair in conflictingPairs:
            [a,b] = sorted(pair)
            if (a,b) not in visited:
                diff = b-a; sizes = n-diff
                preViolation = b+1; postViolation = n-a+2

                default -= (
                    lpRange(diff+1, n) - diff*sizes - lp(n-preViolation+1) - lp(n-postViolation+1)
                )

        for pair in conflictingPairs: #If this pair delete means more subArrays
            [a,b] = sorted(pair); 
            diff = b-a; sizes = n-diff
            preViolation = b+1; postViolation = n-a+2
            res = max(
                res,
                default + (
                    lpRange(diff+1,n) - diff*sizes - lp(n-preViolation+1) - lp(n-postViolation+1)
                )
            )
            
        return res
  
    def fn(self, n: int, conflictingPairs: List[List[int]]) -> int:
        table : dict[int,List[int]] = {}
        for pair in conflictingPairs:
            [a,b] = sorted(pair)
            if b not in table: table[b] = [0,0]
            table[b][0] = max(table[b][0], a)
            table[b].sort()

        res = 0; default = 0; peakB = 0
        table[peakB] = [0,0]
        for num in range(1,n+1):
            b = max(
                table.get(num, [0,0])[1], 
                table[peakB][1]
            )
            default += num-b
            if num in table: peakB = num
        peakB = 0
        for num in range(1,n+1):
            if num in table:
                [a,b] = table.get(num)
                a = max(
                    a,
                    table.get(peakB)[1]
                )
                res = max(
                    res, 
                    default + b-a
                ) # currently there is no way to include subArrays from postElems
                peakB = num

        return res

if __name__ == '__main__':
    testcases = []
    add = lambda n,conflictingPairs: testcases.append([n,conflictingPairs])
    add(n = 4, conflictingPairs = [[2,3],[1,4]])
    add(n = 5, conflictingPairs = [[1,2],[2,5],[3,5]])
    add(n=5,conflictingPairs=[[1,4]])
    sol = Solution()
    for [n,pairs] in testcases:
        print(f'N={n} conflictingPairs={pairs} [1]:{sol.maxSubarrays(n,pairs)} [2]:{sol.fn(n,pairs)}')
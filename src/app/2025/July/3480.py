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
        count = 0; conflictingPoints = [[0,0] for _ in range(n+1)]
        for pair in conflictingPairs:
            [a,b] = sorted(pair)
            conflictingPoints[b].append(a)
            conflictingPoints[b] = sorted(conflictingPoints[b])[1:]
        mx1, mx2 = 0, 0
        xtra = [0]*(n+1); diff = 0
        for end in range(1,n+1):
            [a,b] = conflictingPoints[end]
            [mx2,mx1] = sorted([a,b,mx2,mx1])[2:]
            count += end-mx1
            xtra[mx1] += mx1-mx2
        for x in xtra: diff=max(diff,x)
        return count+diff
if __name__ == '__main__':
    testcases = []
    add = lambda n,conflictingPairs: testcases.append([n,conflictingPairs])
    add(n = 4, conflictingPairs = [[2,3],[1,4]])
    add(n = 5, conflictingPairs = [[1,2],[2,5],[3,5]])
    add(n=5,conflictingPairs=[[1,4]])
    sol = Solution()
    for [n,pairs] in testcases:
        print(f'N={n} conflictingPairs={pairs} result={sol.maxSubarrays(n,pairs)}')
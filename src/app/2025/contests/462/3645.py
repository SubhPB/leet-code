'''
    3645. Maximum Total from Optimal Activation Order

    You are given two integer arrays value and limit, both of length n.

    Initially, all elements are inactive. You may activate them in any order.

    To activate an inactive element at index i, the number of currently active elements must be strictly less than limit[i].
    When you activate the element at index i, it adds value[i] to the total activation value (i.e., the sum of value[i] for all elements that have undergone activation operations).
    After each activation, if the number of currently active elements becomes x, then all elements j with limit[j] <= x become permanently inactive, even if they are already active.
    Return the maximum total you can obtain by choosing the activation order optimally.

    Example 1:

    Input: value = [3,5,8], limit = [2,1,3]

    Output: 16

    Explanation:

    One optimal activation order is:

    Step	Activated i	value[i]	Active Before i	Active After i	Becomes Inactive j	Inactive Elements	Total
    1	1	5	0	1	j = 1 as limit[1] = 1	[1]	5
    2	0	3	0	1	-	[1]	8
    3	2	8	1	2	j = 0 as limit[0] = 2	[0, 1]	16
    Thus, the maximum possible total is 16.

    Example 2:

    Input: value = [4,2,6], limit = [1,1,1]

    Output: 6

    Explanation:

    One optimal activation order is:

    Step	Activated i	value[i]	Active Before i	Active After i	Becomes Inactive j	Inactive Elements	Total
    1	2	6	0	1	j = 0, 1, 2 as limit[j] = 1	[0, 1, 2]	6
    Thus, the maximum possible total is 6.

    Example 3:

    Input: value = [4,1,5,2], limit = [3,3,2,3]

    Output: 12

    Explanation:

    One optimal activation order is:​​​​​​​​​​​​​​

    Step	Activated i	value[i]	Active Before i	Active After i	Becomes Inactive j	Inactive Elements	Total
    1	2	5	0	1	-	[ ]	5
    2	0	4	1	2	j = 2 as limit[2] = 2	[2]	9
    3	1	1	1	2	-	[2]	10
    4	3	2	2	3	j = 0, 1, 3 as limit[j] = 3	[0, 1, 2, 3]	12
    Thus, the maximum possible total is 12.

    

    Constraints:

    1 <= n == value.length == limit.length <= 10^5
    1 <= value[i] <= 10^5​​​​​​​
    1 <= limit[i] <= n
'''
from typing import List, Dict
from bisect import bisect_right as br
class Solution: # Very interesting problem!
    def maxTotal(self, value: List[int], limit: List[int]) -> int:
        l_map:Dict[int,List[int]] = {}; max_limit = 0
        I = sorted([i for i in range(n)], key=lambda i:value[i]); n = len(value)
        for i in I:
            if limit[i] not in l_map: l_map[limit[i]]=[]
            l_map[limit[i]].append(value[i]); max_limit = max(max_limit,limit[i])
        
        inactive_max = 0; x = 0; res = 0
        while x<max_limit and l_map.keys():
            srr = sorted([int(v) for v in l_map.keys()])
            key = srr[br(srr,inactive_max)]
            x+=1; res += l_map[key].pop()
            inactive_max = max(inactive_max, x)
            if x==key: x-=1
            if not l_map[key]: del l_map[key]


        return res

            
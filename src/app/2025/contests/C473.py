from typing import Dict,List
class Solution:
    def countStableSubarrays(self, capacity: List[int]) -> int:
        '''
        #3728 Stable Subarrays With Equal Boundary and Interior Sum

        You are given an integer array capacity.

        A subarray capacity[l..r] is considered stable if:

        Its length is at least 3.
        The first and last elements are each equal to the sum of all elements strictly between them (i.e., capacity[l] = capacity[r] = capacity[l + 1] + capacity[l + 2] + ... + capacity[r - 1]).
        Return an integer denoting the number of stable subarrays.

        Example 1:

        Input: capacity = [9,3,3,3,9]
        Output: 2

        Explanation:
        [9,3,3,3,9] is stable because the first and last elements are both 9, and the sum of the elements strictly between them is 3 + 3 + 3 = 9.
        [3,3,3] is stable because the first and last elements are both 3, and the sum of the elements strictly between them is 3.
        Example 2:

        Constraints:

        3 <= capacity.length <= 10^5
        -10^9 <= capacity[i] <= 10^9
        '''
        Sn=0; freq:Dict[int,Dict[int,int]]={}; res=0
        for i,num in enumerate(capacity):
            if num not in freq: freq[num]={}
            Rn=Sn-num*2
            res+=freq[num].get(Rn,0)
            freq[num][Sn]=1+freq[num].get(Sn,0)
            if i>0 and num==capacity[i-1]==0: res-=1
            Sn+=num
        return res
        
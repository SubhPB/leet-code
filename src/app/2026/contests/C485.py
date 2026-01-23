from typing import List
class Solution:
    '''
    3814. Maximum Capacity Within Budget

    You are given two integer arrays costs and capacity, both of length n,
    where costs[i] represents the purchase cost of the ith machine and capacity[i] represents its performance capacity.
    You are also given an integer budget.
    You may select at most two distinct machines such that the total cost of the selected machines is strictly less than budget.
    Return the maximum achievable total capacity of the selected machines.

    Example 1:
    Input: costs = [4,8,5,3], capacity = [1,5,2,7], budget = 8
    Output: 8
    Explanation:
    Choose two machines with costs[0] = 4 and costs[3] = 3.
    The total cost is 4 + 3 = 7, which is strictly less than budget = 8.
    The maximum total capacity is capacity[0] + capacity[3] = 1 + 7 = 8.

    Constraints:
    1 <= n == costs.length == capacity.length <= 10^5
    1 <= costs[i], capacity[i] <= 10^5
    1 <= budget <= 2 * 10^5
    '''
    def maxCapacity(self, costs: List[int], capacity: List[int], budget: int) -> int:
        capacity.append(0)
        n=len(costs); idx=[i for i in range(n)]
        idx.sort(key=lambda i:costs[i])
        mx1,mx2=0,-1; res=0
        for i,ci in enumerate(idx):
            [_,mx2,mx1]=sorted([mx1,mx2,ci], key=lambda x:capacity[x])
            idx[i]=[ci,mx1,mx2]
        for [ci,mx1,_mx2] in idx:
            rem=budget-costs[ci]
            l=0; r=n-1
            if rem>=0:
                while l<r: 
                    m=(l+r+1)//2
                    if costs[idx[m][0]]<=rem: l=m
                    else: r=m-1 
                res=max(
                    res, capacity[ci]+capacity[idx[l][1+int(idx[l][1]==ci)]]
                )
        return res

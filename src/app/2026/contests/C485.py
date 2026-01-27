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
        n=len(costs); dp=[0]*n; res=0
        idx=sorted([i for i in range(n)], key=lambda i:costs[i])
        for i in range(1,n): dp[i]=max(dp[i-1],capacity[idx[i]-1])
        for i in idx:
            rem=budget-costs[i]
            if rem<0: continue
            elif rem<costs[0]: res=max(res,capacity[i])
            else:
                l=0; r=i
                while l<r:
                    m=(l+r+1)//2
                    if costs[idx[m]]<=rem: l=m
                    else: r=m-1
                res=max(res,capacity[i]+dp[idx[l]])
        return res
    '''
    3816. Lexicographically Smallest String After Deleting Duplicate Characters

    You are given a string s that consists of lowercase English letters.
    You can perform the following operation any number of times (possibly zero times):
    Choose any letter that appears at least twice in the current string s and delete any one occurrence.
    Return the lexicographically smallest resulting string that can be formed this way.

    Example 1:
    Input: s = "aaccb"
    Output: "aacb"
    Explanation:
    We can form the strings "acb", "aacb", "accb", and "aaccb". "aacb" is the lexicographically smallest one.
    For example, we can obtain "aacb" by choosing 'c' and deleting its first occurrence.

    Example 2:
    Input: s = "z"
    Output: "z"
    Explanation:
    We cannot perform any operations. The only string we can form is "z".

    Constraints:
    1 <= s.length <= 10^5
    s contains lowercase English letters only
    '''
    def lexSmallestAfterDeletion(self, s: str) -> str:
        dt={};n=len(s);res=[]
        for c in s:
            if c not in dt: dt[c]=0
            dt[c]+=1
        for c in s:
            while res:
                if res[-1]>c and dt[res[-1]]>1:
                    dt[res[-1]]-=1; res.pop()
                else: break
            res.append(c)
        while res: # removing tail...
            if dt[res[-1]]>1: 
                dt[res[-1]]-=1; res.pop()
            else: break
        return "".join(res)
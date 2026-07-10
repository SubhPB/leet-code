from collections import Counter
class Solution:
    '''
    3946. Maximum Number of Items From Sale I
    You are given a 2D integer array items, where items[i] = [factori, pricei] represents the ith item. You are also given an integer budget.
    There are unlimited copies of each item available for purchase.You may buy any number of copies of any items such that the total cost of the purchased copies is at most budget.
    After buying items, you may receive free copies according to the following rules:
    For each item i that you bought at least one copy of, you receive one free copy of every item j such that j != i and factori divides factorj.
    Buying multiple copies of the same item i does not give additional free copies through item i.
    The same item j can be received multiple times for free if it is received from purchases of different item types.
    Return the maximum total number of item copies you can obtain, including both purchased copies and free copies, while spending at most budget on purchased items.
    
    Example 1:
    Input: items = [[6,2],[2,6],[3,4]], budget = 9
    Output: 4

    Constraints:
    1 <= items.length <= 1000
    items[i] = [factori, pricei]
    1 <= factori, pricei <= 1500
    1 <= budget <= 1500
    '''
    def maximumSaleItems(self, items: list[list[int]], budget: int) -> int:
        n=len(items); gain=[0]*n
        for i in range(n):
            for j in range(n):
                if i!=j and items[j][0]%items[i][0]==0:
                    gain[i]+=1
        dp=[0]*(budget+1)
        for i in range(n):
            ndp=[*dp]
            first=1+gain[i]; cost=items[i][1]
            for b in range(cost,budget+1):
                ndp[b]=max(ndp[b],dp[b-cost]+first)
            for b in range(cost,budget+1):
                ndp[b]=max(ndp[b],ndp[b-cost]+1)
            dp=ndp
        return dp[budget]
    '''
    3947. Maximum Number of Items From Sale II

    You are given a 2D integer array items, where items[i] = [factori, pricei] represents the ith item. You are also given an integer budget.
    There are unlimited copies of each item available for purchase. You may buy any number of copies of any items such that the total cost of the purchased copies is at most budget.
    After buying items, you may receive free copies according to the following rules:
    Each purchased copy of item i can give you at most one free copy of another item j.
    The free item must satisfy i != j and factori divides factorj.
    For each ordered pair (i, j), you can receive a free copy of item j from purchases of item i at most once, regardless of how many copies of item i you buy.
    The same item j can be received multiple times for free if it is received from purchases of different item types.
    Return the maximum total number of item copies you can obtain, including both purchased copies and free copies, while spending at most budget on purchased items.

    Example 1:
    Input: items = [[1,6],[2,4],[3,5]], budget = 19
    Output: 5

    Constraints:
    1 <= items.length <= 10**5
    items[i] = [factori, pricei]
    1 <= factori <= items.length
    1 <= pricei <= 10**9
    1 <= budget <= 10**9
    '''
    def maximumSaleItems(self, items: list[list[int]], budget: int) -> int:
        vals=[item[0] for item in items]
        n=len(items); mx=max(vals)
        freq=Counter(vals)
        factor={}

        for val in freq:
            c=-1;m=val
            while m<=mx:
                if m in freq:
                    c+=freq[m]
                m+=val
            factor[val]=c
        
        pre=[];mn=float('inf')
        for [fac,cost] in items:
            c=factor[fac]; mn=min(cost,mn)
            pre.append([fac,cost,c,cost/(2 if c>0 else 1)])

        pre.sort(key=lambda x:(x[3],-x[2])) # priorité: (cost_per_item, most_free_items)
        res=budget//mn
        cnt=0

        for _,cost,free,__ in pre:
            c=min(free,budget//cost)
            budget-=c*cost
            cnt+=c*2
            res=max(res,cnt+budget//mn)

        return res
    '''
    3948. Lexicographically Maximum MEX Array

    You are given an integer array nums.
    You want to construct an array result by repeatedly performing the following operation until nums becomes empty:
    Choose an integer k such that 1 <= k <= len(nums).
    Compute the MEX of the first k elements of nums.
    Append this MEX to result.
    Remove the first k elements from nums.
    Return the lexicographically maximum array result that can be obtained after performing the operations.
    The MEX of an array is the smallest non-negative integer not present in the array.
    An array a is lexicographically greater than an array b if in the first position where a and b differ, array a has an element that is greater than the corresponding element in b. If the first min(a.length, b.length) elements do not differ, then the longer array is the lexicographically greater one.

    Example 1:
    Input: nums = [0,1,0]
    Output: [2,1]
    Explanation:
    Take the first k = 2 elements [0, 1] which has MEX = 2. Current result = [2].
    Remaining array [0] has MEX = 1. Thus, the final result = [2, 1].

    Constraints:
    1 <= nums.length <= 10**5
    0 <= nums[i] <= 10**5
    '''
    def maximumMEX(self, nums: list[int]) -> list[int]:
        pass
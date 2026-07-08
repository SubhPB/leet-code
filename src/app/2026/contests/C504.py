
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
        pass
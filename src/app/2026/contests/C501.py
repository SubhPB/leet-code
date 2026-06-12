from collections import Counter
class Solution:
    '''
    3926. Count Valid Word Occurrences

    You are given an array of strings chunks. Concatenate all strings in chunks in order to form a string s.
    You are also given an array of strings queries.
    A joiner hyphen is a hyphen character '-' in s whose previous and next characters both exist and are lowercase English letters.
    A word is a maximal substring of s consisting only of lowercase English letters and joiner hyphens.
    All other characters, including spaces and hyphens that are not joiner hyphens, are treated as separators.
    Return an integer array ans, where ans[i] is the number of times queries[i] appears as a word in s.
    
    Example 1:
    Input: chunks = ["hello wor","ld hello"], queries = ["hello","world","wor"]
    Output: [2,1,0]
    Explanation:
    After concatenating all strings in chunks, s = "hello world hello".
    The words are "hello", "world", and "hello".
    The substring "wor" appears inside "world", but it is not a full word.

    Constraints:
    1 <= chunks.length <= 10**5
    1 <= chunks[i].length <= 10**5
    The total length of all strings in chunks does not exceed 105.
    chunks[i] consists only of lowercase English letters, spaces, and '-'.
    1 <= queries.length <= 10**5
    1 <= queries[i].length <= 10**5
    '''
    def countWordOccurrences(self, chunks: list[str], queries: list[str]) -> list[int]:
        ischar = lambda c: 'a'<=c<='z'
        s=''.join(chunks); fq={}
        i=0; n=len(s)
        while i<n:
            if ischar(s[i]):
                w=[]
                while i<n:
                    if ischar(s[i]):
                        w.append(s[i])
                    elif 0<i<n-1 and s[i]=='-' and ischar(s[i-1]) and ischar(s[i+1]):
                        w.append(s[i])
                    else: break
                    i+=1
                ky=''.join(w)
                fq[ky]=1+fq.get(ky,0)
            else:
                i+=1
        return [fq.get(tg,0) for tg in queries]
    '''
    3927. Minimize Array Sum Using Divisible Replacements

    You are given an integer array nums.
    You can perform the following operation any number of times:
    Choose two indices a and b such that nums[a] % nums[b] == 0.
    Replace nums[a] with nums[b].
    Return the minimum possible sum of the array after performing any number of operations.

    Example 1:
    Input: nums = [3,6,2]
    Output: 7
    Explanation:

    Choose a = 1, b = 2, where nums[a] = 6 and nums[b] = 2. Since 6 % 2 == 0, replace nums[1] with nums[2].
    The array becomes [3, 2, 2].
    No further operation reduces the sum. Thus, the final sum is 3 + 2 + 2 = 7.

    Constraints:
    1 <= nums.length <= 10**5
    1 <= nums[i] <= 10**​​​​​​​5
    '''
    def minArraySum(self, nums: list[int]) -> int:
        cnt=Counter(nums);nums=sorted(cnt);res=0
        for num in nums:
            if not cnt[num]: continue
            for b in range(num,nums[-1]+1,num):
                if cnt[b]:
                    res+=cnt[b]*num
                    cnt[b]=0
        return res
    '''
    3928. Minimum Cost to Buy Apples II

    You are given an integer n and an integer array prices of length n, where prices[i] is the price of apples at shop i.
    You are also given a 2D integer array roads, where roads[i] = [ui, vi, costi, taxi] represents a bidirectional road:
    ui and vi are the shops connected by the road.
    costi is the cost to travel the road without carrying apples.
    taxi is the multiplier applied to costi when traveling with apples.
    For each shop i, you can either:
    Buy apples locally at shop i for prices[i].
    Travel empty to any shop j using any number of roads, buy apples for prices[j], and return to shop i while carrying apples, paying cost * tax on each road used for the return trip.
    The forward path, where you travel empty, and the return path may be different.
    Return an integer array ans of length n, where ans[i] is the minimum total cost to buy apples starting from shop i.

    Example 1:
    Input: n = 2, prices = [8,3], roads = [[0,1,1,2]]
    Output: [6,3]
    Thus, the answer is [6, 3].

    Constraints:
    1 <= n <= 1000
    prices.length == n
    1 <= prices[i] <= 10**9
    0 <= roads.length <= min(n × (n - 1) / 2, 2000)
    roads[i] = [ui, vi, costi, taxi]
    0 <= ui, vi <= n - 1
    ui != vi
    1 <= costi <= 10**9
    ​​​​​​​1 <= tax​​​​​​​i <= 100​​​​​​​
    There are no repeated edges.
    '''
    def minCost(self, n: int, prices: list[int], roads: list[list[int]]) -> list[int]:
        inf=int(float('inf'))
        dp=[
            [(inf,inf) for v in range(n)] for u in range(n)
        ]

        parent=[-1]*n
        def find(u:int):
            p=u
            while parent[p]>=0:
                p=parent[p]
            if p!=u: parent[u]=p
            return u
        def union(u:int,v:int):
            pofu=find(u); wofu=-parent[pofu]
            pofv=find(v); wofv=-parent[pofv]
            if pofu!=pofv:
                if wofu>wofv:
                    parent[pofv]=pofu
                    parent[pofu]-=wofv
                else: 
                    parent[pofu]=pofv
                    parent[pofv]-=wofu
                return True
            return False

        G=[[] for _ in range(n)]
        for [u,v,c,t] in roads:
            G[u].append((v,c,t))
            G[v].append((u,c,t))
            union(u,v)
        
        res=[*prices]
        # for u in range(n):
        #     for v in range(u+1,v):
        #         if find(u)!=find(v):
        #             continue
        #         a,b=inf,inf
        #         for g,c,t in G[]

        res=[prices[i] for i in range(n)]
        for u in range(n):
            for v in range(u+1,n):
                if find(u)!=find(v):
                    continue
                a,b=inf,inf
                for g,c,t in G[u]:
                    # a1,b1=λ(g,v,) le complétera
                    pass
        return res
        
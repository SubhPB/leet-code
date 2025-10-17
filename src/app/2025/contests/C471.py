from typing import List

class Solution:
    '''
    You are given a string s consisting only of the characters 'a', 'b', and 'c'.
    A substring of s is called balanced if all distinct characters in the substring appear the same number of times.
    Return the length of the longest balanced substring of s.

    Example 1:
    Input: s = "abbac"
    Output: 4

    Explanation:
    The longest balanced substring is "abba" because both distinct characters 'a' and 'b' each appear exactly 2 times.

    Example 2:
    Input: s = "aabcc"
    Output: 3
    Explanation:
    The longest balanced substring is "abc" because all distinct characters 'a', 'b' and 'c' each appear exactly 1 time.

    Example 3:
    Input: s = "aba"
    Output: 2
    Explanation:
    One of the longest balanced substrings is "ab" because both distinct characters 'a' and 'b' each appear exactly 1 time. Another longest balanced substring is "ba".

    Constraints:

    1 <= s.length <= 10^5
    s contains only the characters 'a', 'b', and 'c'
    '''
    def longestBalanced(self, s: str) -> int:

        def longestZeroSum(c1:str,c2:str):
            longest=0;freq={0:-1} #basecase
            cnt=0
            for i,c in enumerate(s):
                if c == c1: cnt+=1
                elif c == c2: cnt-=1
                else: cnt=0; freq={0:i}
                if cnt in freq:
                    longest=max(longest,i-freq[cnt])
                else: freq[cnt]=i
            return longest
        
        res=0
        for ci in range(3): 
            
            cnt=0#C1
            for c in s:
                if c=="abc"[ci]: cnt+=1
                else: cnt=0
                res=max(res,cnt)

            for cj in range(ci+1,3):
                longest=longestZeroSum("abc"[ci],"abc"[cj])
                res=max(res,longest) #C2

        #Triplet algorthim needs to be researched to grab the core intuition!
        def longestTriplet(): #C3
            longest=0;freq={(0,0):-1} # need 2D imagination
            a=0;b=0;c=0
            for i,ch in enumerate(s):
                if ch=='a': a+=1
                elif ch=='b': b+=1
                else: c+=1
                x=a-b;y=a-c
                if (x,y) in freq:
                    longest=max(longest,i-freq[(x,y)])
                else: freq[(x,y)]=i
            return longest
        res=max(res,longestTriplet())
        return res

    '''
    3715. Sum of Perfect Square Ancestors
    You are given an integer n and an undirected tree rooted at node 0 with n nodes numbered from 0 to n - 1. This is represented by a 2D array edges of length n - 1, where edges[i] = [ui, vi] indicates an undirected edge between nodes ui and vi.

    You are also given an integer array nums, where nums[i] is the positive integer assigned to node i.
    Define a value ti as the number of ancestors of node i such that the product nums[i] * nums[ancestor] is a perfect square.
    Return the sum of all ti values for all nodes i in range [1, n - 1].
    Note:
    In a rooted tree, the ancestors of node i are all nodes on the path from node i to the root node 0, excluding i itself.    
   
    Example 1:

    Input: n = 3, edges = [[0,1],[1,2]], nums = [2,8,2]

    Output: 3

    Explanation:
    i	Ancestors	nums[i] * nums[ancestor]	Square Check	ti
    1	[0]	nums[1] * nums[0] = 8 * 2 = 16	16 is a perfect square	1
    2	[1, 0]	nums[2] * nums[1] = 2 * 8 = 16
    nums[2] * nums[0] = 2 * 2 = 4	Both 4 and 16 are perfect squares	2
    Thus, the total number of valid ancestor pairs across all non-root nodes is 1 + 2 = 3.

    Example 2:

    Input: n = 3, edges = [[0,1],[0,2]], nums = [1,2,4]

    Output: 1

    Explanation:

    i	Ancestors	nums[i] * nums[ancestor]	Square Check	ti
    1	[0]	nums[1] * nums[0] = 2 * 1 = 2	2 is not a perfect square	0
    2	[0]	nums[2] * nums[0] = 4 * 1 = 4	4 is a perfect square	1
    Thus, the total number of valid ancestor pairs across all non-root nodes is 1.


    Constraints:

    1 <= n <= 10^5
    edges.length == n - 1
    edges[i] = [ui, vi]
    0 <= ui, vi <= n - 1
    nums.length == n
    1 <= nums[i] <= 10^5
    The input is generated such that edges represents a valid tree.
    '''
        
    def sumOfAncestors(self, n: int, edges: List[List[int]], nums: List[int]) -> int:

        graph=[[] for _ in range(n)]; res=0 
        for [u,v] in edges: 
            graph[u].append(v)
            graph[v].append(u)

        freq={0:0} # zero refers count of all even exponents
        traversed={}
        def dfs(node:int):
            nonlocal res, traversed
            if node in traversed: return 
            frs=self.prime_factors(nums[node]);key = []
            for fr in frs:
                if frs[fr]&1: key.append(fr)
            key= tuple(sorted(key)) if key else 0

            if key not in freq: freq[key]=0
            freq[key]+=1

            traversed[node]=True
            # run dfs...
            for c in graph[node]: dfs(c)

            freq[key]-=1
            res+=freq[key]
            if not freq[key]: del freq[key]
        dfs(0)
        return res
    
    def prime_factors(self,n):
        if not hasattr(self,'cache'): self.cache={}
        if n in self.cache: return self.cache[n]
        orig=n;factors={}
        
        # Handle 2 separately
        while n % 2 == 0:
            factors[2] = factors.get(2, 0) + 1
            n //= 2
        
        # Check only odd numbers now
        d = 3
        while d * d <= n:
            while n % d == 0:
                factors[d] = factors.get(d, 0) + 1
                n //= d
            d += 2  # skip even numbers
        
        if n > 1: factors[n] = factors.get(n, 0) + 1
        self.cache[orig]=factors
        return factors
from typing import List
class Solution:
    '''
    3776. Minimum Moves to Balance Circular Array
    You are given a circular array balance of length n, where balance[i] is the net balance of person i.
    In one move, a person can transfer exactly 1 unit of balance to either their left or right neighbor.
    Return the minimum number of moves required so that every person has a non-negative balance. If it is impossible, return -1.
    Note: You are guaranteed that at most 1 index has a negative balance initially.

    Example 1:
    Input: balance = [5,1,-4]
    Output: 4
    Explanation:
    One optimal sequence of moves is:
    Move 1 unit from i = 1 to i = 2, resulting in balance = [5, 0, -3]
    Move 1 unit from i = 0 to i = 2, resulting in balance = [4, 0, -2]
    Move 1 unit from i = 0 to i = 2, resulting in balance = [3, 0, -1]
    Move 1 unit from i = 0 to i = 2, resulting in balance = [2, 0, 0]
    Thus, the minimum number of moves required is 4.

    Constraints:
    1 <= n == balance.length <= 10^5
    -10^9 <= balance[i] <= 10^9
    There is at most one negative value in balance initially.
    '''
    def minMoves(self, balance: List[int]) -> int:
        n=len(balance); x=0; t=0
        for i in range(n):
            if balance[i]<0: x=i
            t+=balance[i]
        if t<0: return -1
        l=x-1;r=x+1;m=0
        while balance[x]<0:
            ls=(x-l)%n; rs=(r-x)%n
            if ls<=rs:
                temp=min(-balance[x], balance[l%n])
                balance[x]+=temp; m+=temp*ls;l-=1
            else:
                temp=min(-balance[x],balance[r%n])
                balance[x]+=temp; m+=temp*rs; r+=1
        return m
    '''
    3777. Minimum Deletions to Make Alternating Substring

    You are given a string s of length n consisting only of the characters 'A' and 'B'.
    You are also given a 2D integer array queries of length q, where each queries[i] is one of the following:
    [1, j]: Flip the character at index j of s i.e. 'A' changes to 'B' (and vice versa). This operation mutates s and affects subsequent queries.
    [2, l, r]: Compute the minimum number of character deletions required to make the substring s[l..r] alternating. This operation does not modify s; the length of s remains n.
    A substring is alternating if no two adjacent characters are equal. A substring of length 1 is always alternating.

    Return an integer array answer, where answer[i] is the result of the ith query of type [2, l, r].

    Example 1:
    Input: s = "ABA", queries = [[2,1,2],[1,1],[2,0,2]]
    Output: [0,2]
    Explanation:
    i	queries[i]	j	l	r	s before query	s[l..r]	Result	Answer
    0	[2, 1, 2]	-	1	2	"ABA"	"BA"	Already alternating	0
    1	[1, 1]	1	-	-	"ABA"	-	Flip s[1] from 'B' to 'A'	-
    2	[2, 0, 2]	-	0	2	"AAA"	"AAA"	Delete any two 'A's to get "A"	2
    Thus, the answer is [0, 2].

    Constraints:
    1 <= n == s.length <= 10^5
    s[i] is either 'A' or 'B'.
    1 <= q == queries.length <= 10^5
    queries[i].length == 2 or 3
    queries[i] == [1, j] or,
    queries[i] == [2, l, r]
    0 <= j <= n - 1
    0 <= l <= r <= n - 1
    '''
    def minDeletions(self, s: str, queries: List[List[int]]) -> List[int]:
        pass
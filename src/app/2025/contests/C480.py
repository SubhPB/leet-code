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
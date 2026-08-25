
class Solution:
    '''
    3983. Subsequence After One Replacement
    You are given two strings s and t consisting of lowercase English letters.
    You may choose at most one index in s and replace the character at that index with any lowercase English letter.
    Return true if it is possible to make s a subsequence of t; otherwise, return false.

    Example 1:
    Input: s = "cat", t = "chat"
    Output: true
    Explanation:
    Replace s[1] from 'a' to 'h'. The resulting string is "cht".
    "cht" is a subsequence of "chat" because we can match 'c', 'h', and 't' in order.

    Constraints:
    1 <= s.length, t.length <= 10**5
    s and t consist only of lowercase English letters.
    '''
    def canMakeSubsequence(self, s: str, t: str) -> bool:
        n=len(s)
        m=len(t)
        left=0
        for ct in t:
            if ct==s[left]:
                left+=1
            if left==n: return True

        # remplacer nécessaire
        right=n-1
        for i in range(n-1,-1,-1):
            ct=t[i]; ch=s[right]
            if ct==ch: right-=1
        
        right+=1; left-=1 # les rendre inclusifs
        for i,ch in enumerate(s):
            pass
        return False
    '''
    3984. Divisible Game

    You are given an integer array nums of length n.
    Alice and Bob are playing a game. Alice chooses:
    An integer k such that k > 1.
    Two integers l and r such that 0 <= l <= r < n.
    Initially, both Alice's and Bob's scores are 0.
    For each index i in the range [l, r] (inclusive):
    If nums[i] is divisible by k, Alice's score increases by nums[i].
    Otherwise, Bob's score increases by nums[i].
    The score difference is Alice's score minus Bob's score.
    Alice wants to maximize the score difference. If there are multiple values of k that achieve the maximum score difference, she chooses the smallest such k.
    Return the product of the maximum score difference and the chosen value of k. Since the result can be large, return it modulo 1e9 + 7.

    Example 1:
    Input: nums = [1,4,6,8]
    Output: 36
    Explanation:

    Alice can choose k = 2, l = 1, and r = 3.
    All values in nums[1..3] are divisible by 2, so Alice's score is 4 + 6 + 8 = 18, while Bob's score is 0.
    The score difference is 18, which is the maximum possible. Among all values of k that achieve this score difference, the smallest is 2.
    Therefore, the answer is 18 * 2 = 36.

    Constraints:
    1 <= nums.length <= 1000
    1 <= nums[i] <= 10**6
    '''
    def divisibleGame(self, nums: list[int]) -> int:
        pass
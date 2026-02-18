from typing import List
class Solution:
    '''
    3839. Number of Prefix Connected Groups

    You are given an array of strings words and an integer k.
    Two words a and b at distinct indices are prefix-connected if a[0..k-1] == b[0..k-1].
    A connected group is a set of words such that each pair of words is prefix-connected.
    Return the number of connected groups that contain at least two words, formed from the given words.Note:

    Words with length less than k cannot join any group and are ignored.
    Duplicate strings are treated as separate words.

    Example 1:
    Input: words = ["apple","apply","banana","bandit"], k = 2
    Output: 2
    Explanation:
    Words sharing the same first k = 2 letters are grouped together:
    words[0] = "apple" and words[1] = "apply" share prefix "ap".
    words[2] = "banana" and words[3] = "bandit" share prefix "ba".
    Thus, there are 2 connected groups, each containing at least two words.

    Constraints:
    1 <= words.length <= 5000
    1 <= words[i].length <= 100
    1 <= k <= 100
    All strings in words consist of lowercase English letters.
    '''
    def prefixConnected(self, words: List[str], k: int) -> int:
        dt={};res=0
        for word in words:
            key=word[:k]
            if len(key)>=k: dt[key]=1+dt.get(key,0)
        for key in dt: res+=int(dt[key]>1)
        return res
    '''
    3840. House Robber V

    You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed and is protected by a security system with a color code.
    You are given two integer arrays nums and colors, both of length n, where nums[i] is the amount of money in the ith house and colors[i] is the color code of that house.
    You cannot rob two adjacent houses if they share the same color code.
    Return the maximum amount of money you can rob.

    Example 1:
    Input: nums = [1,4,3,5], colors = [1,1,2,2]
    Output: 9
    Explanation:
    Choose houses i = 1 with nums[1] = 4 and i = 3 with nums[3] = 5 because they are non-adjacent.
    Thus, the total amount robbed is 4 + 5 = 9.

    Constraints:
    1 <= n == nums.length == colors.length <= 10^5
    1 <= nums[i], colors[i] <= 10^5
    '''
    def rob(self, nums: List[int], colors: List[int]) -> int:
        n=len(nums); x=2; 
        for i in range(2): nums.append(0)
        for i in range(1,n):
            if colors[i]!=colors[i-1]: x=1
            if x>2:
                nums[i]+=max(nums[i-2],nums[i-3])
            else:
                nums[i]+=max(nums[i-x],nums[i-x-1])
            x+=1
        return max(nums[n-1],nums[n-2])
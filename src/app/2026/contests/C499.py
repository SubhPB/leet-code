class Solution:
    '''
    3913. Sort Vowels by Frequency

    You are given a string s consisting of lowercase English characters.
    Rearrange only the vowels in the string so that they appear in non-increasing order of their frequency.
    If multiple vowels have the same frequency, order them by the position of their first occurrence in s.
    Return the modified string.
    Vowels are 'a', 'e', 'i', 'o', and 'u'.
    The frequency of a letter is the number of times it occurs in the string.

    Example 1:
    Input: s = "leetcode"
    Output: "leetcedo"
    Explanation:​​​​​​​
    Vowels in the string are ['e', 'e', 'o', 'e'] with frequencies: e = 3, o = 1.
    Sorting in non-increasing order of frequency and placing them back into the vowel positions results in "leetcedo".

    Constraints:
    1 <= s.length <= 10**5
    s consists of lowercase English letters
    '''
    def sortVowels(self, s: str) -> str:
        freq={}; occr={}
        for i,c in enumerate(s):
            if c in 'aeiou':
                if c not in freq:
                    freq[c]=0
                    occr[c]=i
                freq[c]+=1
            
        keys=sorted(freq.keys(), key=lambda k: (-freq[k],occr[k]))
        j=0;s=[*s]
        for i,c in enumerate(s):
            if c in 'aeiou':
                s[i]=keys[j]
                freq[keys[j]]-=1
                if not freq[keys[j]]:
                    j+=1
        return ''.join(s)
    '''
    3914. Minimum Operations to Make Array Non Decreasing

    You are given an integer array nums of length n.
    In one operation, you may choose any subarray nums[l..r] and increase each element in that subarray by x, where x is any positive integer.
    Return the minimum possible sum of the values of x across all operations required to make the array non-decreasing.
    An array is non-decreasing if nums[i] <= nums[i + 1] for all 0 <= i < n - 1.
    
    Example 1:

    Input: nums = [3,3,2,1]
    Output: 2
    
    Constraints:
    1 <= n == nums.length <= 10**5
    1 <= nums[i] <= 10**9
    '''
    def minOperations(self, nums: list[int]) -> int:
        n=len(nums); res=0
        for i in range(1,n):
            if nums[i-1]>nums[i]:
                res+=nums[i-1]-nums[i]
        return res
    '''
    3915. Maximum Sum of Alternating Subsequence With Distance at Least K

    You are given an integer array nums of length n and an integer k.
    Pick a subsequence with indices 0 <= i1 < i2 < ... < im < n such that:
    For every 1 <= t < m, it+1 - it >= k.
    The selected values form a strictly alternating sequence. In other words, either:
    nums[i1] < nums[i2] > nums[i3] < ..., or
    nums[i1] > nums[i2] < nums[i3] > ...
    A subsequence of length 1 is also considered strictly alternating. The score of a valid subsequence is the sum of its selected values.
    Return an integer denoting the maximum possible score of a valid subsequence.

    Example 1:
    Input: nums = [5,4,2], k = 2
    Output: 7
    Explanation:
    An optimal choice is indices [0, 2], which gives values [5, 2].
    The distance condition holds because 2 - 0 = 2 >= k.
    The values are strictly alternating because 5 > 2.
    The score is 5 + 2 = 7.

    Constraints:
    1 <= n == nums.length <= 10**5
    1 <= nums[i] <= 10**5
    1 <= k <= n
    '''
    def maxAlternatingSum(self, nums: list[int], k: int) -> int:
        pass
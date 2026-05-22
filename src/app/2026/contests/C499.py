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
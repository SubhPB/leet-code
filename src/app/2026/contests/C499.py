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

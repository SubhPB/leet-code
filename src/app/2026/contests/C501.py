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
        β=[False]*(10**5+1); nums.sort()
        res=0
        for num in nums:
            for x in range(1,(num+2)//2):
                if β[x]:
                    num=x; break
            β[num]=True
            res+=num
        return res
            
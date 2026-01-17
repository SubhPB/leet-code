from typing import List
class Solution:
    '''  
    3804. Number of Centered Subarrays
    You are given an integer array nums.
    A subarray of nums is called centered if the sum of its elements is equal to at least one element within that same subarray.
    Return the number of centered subarrays of nums.

    Example 1:
    Input: nums = [-1,1,0]
    Output: 5
    Explanation:
    All single-element subarrays ([-1], [1], [0]) are centered.
    The subarray [1, 0] has a sum of 1, which is present in the subarray.
    The subarray [-1, 1, 0] has a sum of 0, which is present in the subarray.
    Thus, the answer is 5.

    Constraints:
    1 <= nums.length <= 500
    -10^5 <= nums[i] <= 10^5
    '''
    def centeredSubarrays(self, nums: List[int]) -> int:
        n=len(nums);E=[0]*(n+1);res=0
        for i in range(n): E[i]+=E[i-1]+nums[i]
        print(f'E={E}')
        for l in range(n):
            for r in range(l,n):
                for x in range(l,r+1):
                    if nums[x]==E[r]-E[l-1]: 
                        res+=1; break

        return res
    '''
    3805. Count Caesar Cipher Pairs
    You are given an array words of n strings. Each string has length m and contains only lowercase English letters.
    Two strings s and t are similar if we can apply the following operation any number of times (possibly zero times) so that s and t become equal.
    Choose either s or t.
    Replace every letter in the chosen string with the next letter in the alphabet cyclically. The next letter after 'z' is 'a'.
    Count the number of pairs of indices (i, j) such that:

    i < j
    words[i] and words[j] are similar.
    Return an integer denoting the number of such pairs.

    Example 1:
    Input: words = ["fusion","layout"]
    Output: 1
    Explanation:
    words[0] = "fusion" and words[1] = "layout" are similar because we can apply the operation to "fusion" 6 times. The string "fusion" changes as follows.
    "fusion"
    "gvtjpo"
    "hwukqp"
    "ixvlrq"
    "jywmsr"
    "kzxnts"
    "layout"

    Constraints:
    1 <= n == words.length <= 10^5
    1 <= m == words[i].length <= 10^5
    1 <= n * m <= 10^5
    words[i] consists only of lowercase English letters.
    '''
    def countPairs(self, words: List[str]) -> int:
        freq={}; res=0
        for word in words:
            sep=[]; n=len(word)
            for i in range(1,n):
                sep.append(
                    chr(97+(ord(word[i])-ord(word[i-1]))%26)
                )
            idx=''.join(sep)
            freq[idx]=freq.get(idx,0)+1
        for idx in freq: res+=(freq[idx]*(freq[idx]-1))//2
        return res
    '''
    3806. Maximum Bitwise AND After Increment Operations

    You are given an integer array nums and two integers k and m.
    You may perform at most k operations. In one operation, you may choose any index i and increase nums[i] by 1.
    Return an integer denoting the maximum possible bitwise AND of any subset of size m after performing up to k operations optimally.

    Example 1:
    Input: nums = [3,1,2], k = 8, m = 2
    Output: 6
    Explanation:
    We need a subset of size m = 2. Choose indices [0, 2].
    Increase nums[0] = 3 to 6 using 3 operations, and increase nums[2] = 2 to 6 using 4 operations.
    The total number of operations used is 7, which is not greater than k = 8.
    The two chosen values become [6, 6], and their bitwise AND is 6, which is the maximum possible.
    
    Constraints:
    1 <= n == nums.length <= 5*10^4
    1 <= nums[i] <= 10^9
    1 <= k <= 10^9
    1 <= m <= n
    '''
    def maximumAND(self, nums: List[int], k: int, m: int) -> int:
        pass
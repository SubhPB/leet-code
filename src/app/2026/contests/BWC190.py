from math import gcd
class Solution:
    '''
    4035. Maximum Valid Split Positions I

    You are given an integer array nums.
    You may remove at most one element from nums. Let arr be the array of remaining elements in their original order, and let m be its length.
    A split position i of arr is valid if:

    0 <= i < m - 1, and
    gcd(arr[0..i]) == gcd(arr[i + 1..m - 1]).
    An array of length 1 has no valid split positions.
    The score of arr is the number of valid split positions in it.
    Return the maximum possible score of arr.
    Here, gcd(a) denotes the greatest common divisor of all elements in the array a.

    Example 1:
    Input: nums = [10,30,15,10]
    Output: 2

    Constraints:
    2 <= nums.length <= 1000
    1 <= nums[i] <= 10**9​​​​​​​
    '''
    def maxValidSplits(self, nums: list[int]) -> int:
        n=len(nums)
        garr=[*nums]
        for i in range(1,n-1):
            garr[i]=gcd(garr[i-1],garr[i])
        res=0
        for i in range(n-2,-1,-1):
            if garr[i]==garr[i+1]:
                res+=1
            garr[i]=gcd(garr[i+1],nums[i])
        return res
    '''
    4036. Lexicographically Largest String After Pair Transformations

    You are given an integer array nums.

    For each integer x in nums, start with a string consisting of exactly x lowercase 'a' characters.
    You may perform the following operation any number of times (including zero):
    Choose two adjacent equal letters and replace them with the next letter in the alphabet.
    For example, "aa" can be replaced with "b", and "bb" can be replaced with "c". The pair "zz" cannot be replaced.
    For each x, determine the lexicographically largest string that can be obtained.
    Return an array of strings where the ith string is the answer for nums[i].
    A string a is lexicographically larger than a string b if, at the first position where they differ, a contains a letter that appears later in the alphabet than the corresponding letter in b. If the first min(a.length, b.length) characters are equal, the longer string is lexicographically larger.
    
    Example 1:
    Input: nums = [2,5,7]
    Output: ["b","ca","cba"]

    Constraints:
    1 <= nums.length <= 10**5
    1 <= nums[i] <= 10**8
    '''
    def largestString(self, nums: list[int]) -> list[str]:
        pass
    '''
    4037. Maximum Valid Split Positions II

    You are given an integer array nums.
    You may remove at most one element from nums. Let arr be the array of remaining elements in their original order, and let m be its length.
    A split position i of arr is valid if:
    0 <= i < m - 1, and
    gcd(arr[0..i]) == gcd(arr[i + 1..m - 1]).
    An array of length 1 has no valid split positions.
    The score of arr is the number of valid split positions in it.
    Return the maximum possible score of arr.
    Here, gcd(a) denotes the greatest common divisor of all elements in the array a.

    Example 1:
    Input: nums = [10,30,15,10]
    Output: 2

    Constraints:
    2 <= nums.length <= 10**5
    1 <= nums[i] <= 10**9​​​​​​​
    '''
    def maxValidSplits(self, nums: list[int]) -> int:
        pass
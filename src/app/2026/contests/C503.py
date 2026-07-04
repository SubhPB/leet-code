class Solution:
    '''
    3941. Password Strength

    You are given a string password.

    The strength of the password is calculated based on the following rules:

    1 point for each distinct lowercase letter ('a' to 'z').
    2 points for each distinct uppercase letter ('A' to 'Z').
    3 points for each distinct digit ('0' to '9').
    5 points for each distinct special character from the set "!@#$".
    Each character contributes at most once, even if it appears multiple times.

    Return an integer denoting the strength of the password.

    Constraints:
    1 <= password.length <= 105
    password consists of lowercase and uppercase English letters, digits, and special characters from "!@#$".
    '''
    def passwordStrength(self, password: str) -> int:
        res=0
        for char in set(password):
            if 'a'<=char<='z': res+=1
            elif 'A'<=char<='Z': res+=2
            elif char in '!@#$': res+=5
            elif 0<=int(char)<=9: res+=3
        return res
    '''
    3942. Minimum Operations to Sort a Permutation
    You are given an integer array nums of length n, where nums is a permutation of the integers from 0 to n - 1.
    You may perform only the following operations:
    Reverse the entire array.
    Rotate Left by One: Move the first element to the end of the array, and rest elements to left by one position.
    Return an integer denoting the minimum number of operations required to sort the array in increasing order. If it is not possible to sort the array using only the given operations, return -1.

    Example 1:
    Input: nums = [0,2,1]
    Output: 2
    Explanation:
    Rotate Left by one: [2, 1, 0]
    Reverse the array: [0, 1, 2]
    The array becomes sorted in 2 operations, which is minimal

    Constraints:
    1 <= n == nums.length <= 10**5
    0 <= nums[i] <= n - 1
    nums is a permutation of integers from 0 to n - 1.
    '''
    def minOperations(self, nums: list[int]) -> int:
        n=len(nums)
        if n<=2: return nums[0]
        i=nums[1]-nums[0]
        if i in [1-n,n-1]:
            i = 1 if i<0 else -1
        if abs(i)!=1: return -1
        for j in range(n):
            if (nums[j]+i)%n!=nums[(j+1)%n]:
                return -1
        if i>0: #inc 
            return min(-nums[0]%n,1 + (nums[0]-n+1)%n)
        return min(-nums[-1]%n + 1,1 + (nums[0]-n+1)%n)

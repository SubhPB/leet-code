from typing import List

class Solution:
    '''
    3766. Minimum Operations to Make Binary Palindrome

    You are given an integer array nums.
    For each element nums[i], you may perform the following operations any number of times (including zero):
    Increase nums[i] by 1, or
    Decrease nums[i] by 1.
    A number is called a binary palindrome if its binary representation without leading zeros reads the same forward and backward.
    Your task is to return an integer array ans, where ans[i] represents the minimum number of operations required to convert nums[i] into a binary palindrome.

    Constraints:

    1 <= nums.length <= 5000
    ​​​​​​​1 <= nums[i] <= 5000
    '''
    def minOperations(self, inp: List[int]) -> List[int]:
        # --- Better to either cache or set into global scope
        nums=[0];x=1
        while nums[-1]<=5000:
            n=x.bit_length();m=(n+1)//2
            nums.append(x)
            for i in range(m):
                if bool(x&(1<<(n-i-1))) != bool(x&(1<<i)):
                    nums.pop(); break
            x+=1
        
        for i,num in enumerate(inp):
            l=0; r=len(nums)-1
            while l<r:
                m=(l+r+1)//2
                if nums[m]>num:
                    r=m-1
                else: l=m
            inp[i]=min(
                num-nums[l],
                nums[l+1]-num
            )
        return inp
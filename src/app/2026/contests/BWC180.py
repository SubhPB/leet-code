# cache:#3896
N=10**5; cache=[0]*(N+1); prime=N
def isprime(x:int):
    if not x%2: return x==2
    elif not x%3: return x==3
    f=5
    while f*f<=x:
        if not x%f or not x%(f+2):
            return False
        f+=6
    return True
while not isprime(prime):
    prime+=1

for num in range(N,3,-1):
    if not isprime(num):
        cache[num]=prime-num
    else: prime=num
# cache:#3896

class Solution:
    '''
    3896. Minimum Operations to Transform Array into Alternating Prime
    You are given an integer array nums.
    An array is considered alternating prime if:
    Elements at even indices (0-based) are prime numbers.
    Elements at odd indices are non-prime numbers.
    In one operation, you may increment any element by 1.
    Return the minimum number of operations required to transform nums into an alternating prime array.
    A prime number is a natural number greater than 1 with only two factors, 1 and itself.

    Example 1:
    Input: nums = [1,2,3,4]
    Output: 3
    Explanation:
    The element at index 0 must be prime. Increment nums[0] = 1 to 2, using 1 operation.
    The element at index 1 must be non-prime. Increment nums[1] = 2 to 4, using 2 operations.
    The element at index 2 is already prime.
    The element at index 3 is already non-prime.
    Total operations = 1 + 2 = 3.

    Constraints:
    1 <= nums.length <= 10*5
    1 <= nums[i] <= 10**5
    '''

    def minOperations(self, nums: list[int]) -> int:
        n=len(nums); res=0
        for i in range(n):
            x=nums[i]
            if i%2:
                while isprime(x): #literally O(1)
                    x+=1
                res+=x-nums[i]
            else:
                res+=cache[x]
        return res
# cache:#3896
N=10**5; cache=[0]*(N+1); prime=N
cache[1]=1 # 1 is not prime.
def isprime(x:int):
    if x==1: return False
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

# cache:#3897
M=2*(10**5); mod=10**9+7; pow=[1]*(M+1)
def add(x:int,y:int):
    return (x%mod+y%mod)%mod
def mul(x:int,y:int):
    return (x%mod*y%mod)%mod
for i in range(1,M+1): 
    pow[i]=mul(2,pow[i-1])
# cache:#3897

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
    '''
    3897. Maximum Value of Concatenated Binary Segments

    You are given two integer arrays nums1 and nums0, each of size n.
    nums1[i] represents the number of '1's in the ith segment.
    nums0[i] represents the number of '0's in the ith segment.
    For each index i, construct a binary segment consisting of:
    nums1[i] occurrences of '1' followed by
    nums0[i] occurrences of '0'.
    You may rearrange the order of these segments in any way. After rearranging, concatenate all segments to form a single binary string.
    Return the maximum possible integer value of the concatenated binary string.
    Since the result can be very large, return the answer modulo 109 + 7.

    Example 1:
    Input: nums1 = [1,2], nums0 = [1,0]
    Output: 14
    Explanation:
    At index 0, nums1[0] = 1 and nums0[0] = 1, so the segment formed is "10".
    At index 1, nums1[1] = 2 and nums0[1] = 0, so the segment formed is "11".
    Reordering the segments as "11" followed by "10" produces the binary string "1110".
    The binary number "1110" has value 14 which is the maximum possible value.

    Constraints:
    1 <= n == nums1.length == nums0.length <= 10**5
    0 <= nums1[i], nums0[i] <= 10**4
    nums1[i] + nums0[i] > 0
    The total sum of all elements in nums1 and nums0 does not exceed 2 * 105.
    '''
    def maxValue(self, nums1: list[int], nums0: list[int]) -> int:
        #incomplete
        n=len(nums1); idx=[i for i in range(n)]
        idx.sort(key=lambda i:-(nums1[i]+nums0[i]))
        idx.sort(key=lambda i:nums0[i])

        l=0; res=0
        print(f'idx={[''.join(['1']*nums1[x]) + ''.join(['0']*nums0[x]) for x in idx]}')
        for i in range(n-1,-1,-1):
            x=idx[i]; c=nums1[x]; z=nums0[x]
            res=add(res, mul(pow[l],pow[c+z]-pow[z]))
            l+=c+z
        return res
    '''
    3898. Find the Degree of Each Vertex
    You are given a 2D integer array matrix of size n x n representing the adjacency matrix of an undirected graph with n vertices labeled from 0 to n - 1.
    matrix[i][j] = 1 indicates that there is an edge between vertices i and j.
    matrix[i][j] = 0 indicates that there is no edge between vertices i and j.
    The degree of a vertex is the number of edges connected to it.
    Return an integer array ans of size n where ans[i] represents the degree of vertex i.

    Example 1:
    Input: matrix = [[0,1,1],[1,0,1],[1,1,0]]
    Output: [2,2,2]
    Explanation:
    Vertex 0 is connected to vertices 1 and 2, so its degree is 2.
    Vertex 1 is connected to vertices 0 and 2, so its degree is 2.
    Vertex 2 is connected to vertices 0 and 1, so its degree is 2.
    Thus, the answer is [2, 2, 2].

    Constraints:
    1 <= n == matrix.length == matrix[i].length <= 100​​​​​​​
    ​​​​​​​matrix[i][i] == 0
    matrix[i][j] is either 0 or 1
    matrix[i][j] == matrix[j][i]
    '''   
    def findDegrees(self, matrix: list[list[int]]) -> list[int]:
        pass
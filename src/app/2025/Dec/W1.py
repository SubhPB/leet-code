from typing import List
class Solution:
    '''
        3756. Concatenate Non-Zero Digits and Multiply by Sum II

        You are given a string s of length m consisting of digits. You are also given a 2D integer array queries, where queries[i] = [li, ri].
        For each queries[i], extract the substring s[li..ri]. Then, perform the following:
        Form a new integer x by concatenating all the non-zero digits from the substring in their original order. If there are no non-zero digits, x = 0.
        Let sum be the sum of digits in x. The answer is x * sum.
        Return an array of integers answer where answer[i] is the answer to the ith query.

        Since the answers may be very large, return them modulo 109 + 7.
        Example 1:
        Input: s = "10203004", queries = [[0,7],[1,3],[4,6]]
        Output: [12340, 4, 9]
        Explanation:
        s[0..7] = "10203004"
        x = 1234
        sum = 1 + 2 + 3 + 4 = 10
        Therefore, answer is 1234 * 10 = 12340.
        s[1..3] = "020"
        x = 2
        sum = 2
        Therefore, the answer is 2 * 2 = 4.
        s[4..6] = "300"
        x = 3
        sum = 3
        Therefore, the answer is 3 * 3 = 9.

        Constraints:

        1 <= m == s.length <= 10^5
        s consists of digits only.
        1 <= queries.length <= 10^5
        queries[i] = [li, ri]
        0 <= li <= ri < m
    '''
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        n=len(s);sums=[0]*(n+1);concs=[0]*(n+1);M=10**9+7
        ADD=lambda x,y:(x%M+y%M)%M;MUL=lambda x,y:(x%M * y%M)%M
        for i,num in enumerate(s):
            sums[i]=ADD(sums[i-1],int(num)); concs[i]=concs[i-1]
            if int(num): concs[i]=MUL(concs[i],10)
            concs[i]=ADD(concs[i],int(num))

        for i,[l,r] in enumerate(queries):
            [n1,n2]=[len(str(concs[j])) for j in (l-1,r)]
            queries[i]=ADD(concs[r],-MUL(concs[l-1],10**(n2-n1)))
            queries[i]=MUL(queries[i],sums[r]-sums[l-1])
        return queries
    '''
    3759. Count Elements With at Least K Greater Values

    You are given an integer array nums of length n and an integer k.
    An element in nums is said to be qualified if there exist at least k elements in the array that are strictly greater than it.
    Return an integer denoting the total number of qualified elements in nums.

    Example 1:
    Input: nums = [3,1,2], k = 1
    Output: 2

    Explanation:

    The elements 1 and 2 each have at least k = 1 element greater than themselves.
    ​​​​​​​No element is greater than 3. Therefore, the answer is 2.

    Constraints:

    1 <= n == nums.length <= 10^5
    1 <= nums[i] <= 10^9
    0 <= k < n
    '''
    def countElements(self, nums: List[int], k: int) -> int:
        n=len(nums);nums.sort()
        nums.append(nums[-1]+1)
        if nums[n-k-1]!=nums[n-k]: return n-k
        l=0;r=n
        while l<r:
            m=(l+r)//2
            if nums[m]>=nums[n-k-1]: r=m
            else: l=m+1
        return l
    '''
    3761. Minimum Absolute Distance Between Mirror Pairs

    You are given an integer array nums.
    A mirror pair is a pair of indices (i, j) such that:
    0 <= i < j < nums.length, and
    reverse(nums[i]) == nums[j], where reverse(x) denotes the integer formed by reversing the digits of x. Leading zeros are omitted after reversing, for example reverse(120) = 21.
    Return the minimum absolute distance between the indices of any mirror pair. The absolute distance between indices i and j is abs(i - j).
    If no mirror pair exists, return -1.

    Example 1:
    Input: nums = [12,21,45,33,54]
    Output: 1

    Explanation:
    The mirror pairs are:
    (0, 1) since reverse(nums[0]) = reverse(12) = 21 = nums[1], giving an absolute distance abs(0 - 1) = 1.
    (2, 4) since reverse(nums[2]) = reverse(45) = 54 = nums[4], giving an absolute distance abs(2 - 4) = 2.
    The minimum absolute distance among all pairs is 1.

    Constraints:

    1 <= nums.length <= 10^5
    1 <= nums[i] <= 10^9​​​​​​​
    '''
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        prev={};n=len(nums);res=n
        for i in range(n-1,-1,-1):
            num=nums[i];rum=int(str(num)[::-1])
            if rum in prev: res=min(res,prev[rum]-i)
            prev[num]=i
        return res if res!=n else -1
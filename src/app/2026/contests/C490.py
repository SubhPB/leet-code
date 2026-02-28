class Solution:
    '''
    3848. Check Digitorial Permutation

    You are given an integer n.
    A number is called digitorial if the sum of the factorials of its digits is equal to the number itself.
    Determine whether any permutation of n (including the original order) forms a digitorial number.
    Return true if such a permutation exists, otherwise return false.
    Note:
    The factorial of a non-negative integer x, denoted as x!, is the product of all positive integers less than or equal to x, and 0! = 1.
    A permutation is a rearrangement of all the digits of a number that does not start with zero. Any arrangement starting with zero is invalid.
    
    Example 1:
    Input: n = 145
    Output: true
    Explanation:
    The number 145 itself is digitorial since 1! + 4! + 5! = 1 + 24 + 120 = 145. Thus, the answer is true.

    Constraints:
    1 <= n <= 10^9
    '''
    def isDigitorialPermutation(self, n: int) -> bool:
        fx=[1]*10
        for i in range(1,10): fx[i]=i*fx[i-1]
        return n==sum([fx[int(x)] for x in str(n)])
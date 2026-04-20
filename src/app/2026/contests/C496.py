class Solution:
    '''
    3890. Integers With Multiple Sum of Two Cubes

    You are given an integer n.
    An integer x is considered good if there exist at least two distinct pairs (a, b) such that:
    a and b are positive integers.
    a <= b
    x = a3 + b3
    Return an array containing all good integers less than or equal to n, sorted in ascending order.
    Example 1:
    Input: n = 4104
    Output: [1729,4104]
    Explanation:
    Among integers less than or equal to 4104, the good integers are:
    1729: 13 + 123 = 1729 and 93 + 103 = 1729.
    4104: 23 + 163 = 4104 and 93 + 153 = 4104.
    Thus, the answer is [1729, 4104].

    
    Constraints:
    1 <= n <= 10**9
    '''
    def findGoodIntegers(self, n: int) -> list[int]:
        pass
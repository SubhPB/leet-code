class Solution:
    '''
    3871. Count Commas in Range II
    You are given an integer n.
    Return the total number of commas used when writing all integers from [1, n] (inclusive) in standard number formatting.
    In standard formatting:
    A comma is inserted after every three digits from the right.
    Numbers with fewer than 4 digits contain no commas.

    Example 1:
    Input: n = 1002
    Output: 3
    Explanation:
    The numbers "1,000", "1,001", and "1,002" each contain one comma, giving a total of 3.

    Constraints:
    1 <= n <= 10^15
    '''
    def countCommas(self, n: int) -> int:
        r=0; thl=[10**3,10**6,10**9,10**12,10**15]
        for t in thl:
            if n>=t: r+=n-(t-1)
        return r
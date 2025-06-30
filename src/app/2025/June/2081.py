'''
2081. Sum of k-Mirror Numbers

    A k-mirror number is a positive integer without leading zeros that reads the same both forward and backward in base-10 as well as in base-k.

    For example, 9 is a 2-mirror number. The representation of 9 in base-10 and base-2 are 9 and 1001 respectively, which read the same both forward and backward.
    On the contrary, 4 is not a 2-mirror number. The representation of 4 in base-2 is 100, which does not read the same both forward and backward.
    Given the base k and the number n, return the sum of the n smallest k-mirror numbers.

    

    Example 1:

    Input: k = 2, n = 5
    Output: 25
    Explanation:
    The 5 smallest 2-mirror numbers and their representations in base-2 are listed as follows:
    base-10    base-2
        1          1
        3          11
        5          101
        7          111
        9          1001
    Their sum = 1 + 3 + 5 + 7 + 9 = 25. 
    Example 2:

    Input: k = 3, n = 7
    Output: 499
    Explanation:
    The 7 smallest 3-mirror numbers are and their representations in base-3 are listed as follows:
    base-10    base-3
        1          1
        2          2
        4          11
        8          22
        121        11111
        151        12121
        212        21212
    Their sum = 1 + 2 + 4 + 8 + 121 + 151 + 212 = 499.
    Example 3:

    Input: k = 7, n = 17
    Output: 20379000
    Explanation: The 17 smallest 7-mirror numbers are:
    1, 2, 3, 4, 5, 6, 8, 121, 171, 242, 292, 16561, 65656, 2137312, 4602064, 6597956, 6958596
    

    Constraints:

    2 <= k <= 9
    1 <= n <= 30
    python ./src/app/2025/June/2081.py
'''
import collections

class Solution:
    def kMirror(self, k: int, n: int) -> int:

        def exp(base:int, pow:int):
            res = 1
            while pow>0:
                if pow&1: res = res*base
                base = base*base
                pow >>= 1
            return res
        
        def baseK(val:int):
            res = collections.deque([])
            while val>0:
                val, rem = divmod(val,k)
                res.appendleft(str(rem))
            if res[0] == '0': res.popleft()
            return ''.join(res)
        
        def generatePalindromes(length:int, lmt=None) ->list[str]:
            if length==1: return [str(i) for i in range(1,10)]
            elif length>1:
                hfl,res = (length+1)//2, []
                mn,mx = exp(10, hfl-1), exp(10, hfl) - 1
                for i in range(mn, mx+1):
                    if lmt is not None and len(res) == lmt: break
                    pf = str(i)
                    sf = pf[-2::-1] if length&1 else pf[::-1]
                    res.append(pf+sf)
                return res
            return []
        
        def isPalindrome(s:str):
            if len(s) > 1:
                for i in range(len(s)//2):
                    if s[i] != s[-i-1]: return False
            return True

        res, size = 0, 1
        while n>0:
            decimalPalindromes = generatePalindromes(size)
            for pld in decimalPalindromes:
                if n<=0: break
                bseK = baseK(int(pld))
                if isPalindrome(bseK): 
                    res += int(pld)
                    n-=1
                    
            size+=1
        return res
    
if __name__ == "__main__":
    testcases:list[int, int] = []
    add = lambda k,n: testcases.append([k,n])
    
    add(k = 2, n = 5)
    add(k = 3, n = 7)
    add(k=7, n=17)

    sol = Solution()
    for [k,n] in testcases:
        ans = sol.kMirror(k,n)
        print(f'k={k} n={n} answer={ans}')
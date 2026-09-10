class Solution:
    '''
    3993. Maximum Value of an Alternating Sequence

    You are given three integers n, s, and m.
    A sequence seq of integers of length n is considered valid if:
    seq[0] = s.
    The sequence is alternating, meaning that either:
    seq[0] > seq[1] < seq[2] > ..., or
    seq[0] < seq[1] > seq[2] < ....
    For every adjacent pair, |seq[i] - seq[i - 1]| <= m.
    A sequence of length 1 is considered alternating.
    Return the maximum possible element that can appear in any valid sequence.

    Example 1:
    Input: n = 4, s = 3, m = 5
    Output: 12
    Explanation:
    One valid sequence is [3, 8, 7, 12].
    The maximum element in the sequence is 12.

    Constraints:
    1 <= n, s <= 10**9  
    1 <= m <= 10**5
    '''
    def maximumValue(self, n: int, s: int, m: int) -> int:
        if not n-1: return s
        fn = lambda i:s - (i//2) + m*((i+1)//2 )
        return max(fn(n-1), fn(n-2)) 
    '''
    3994. Minimum Adjacent Swaps to Partition Array

    You are given an integer array nums and two integers a and b such that a < b.
    An array is called good if it can be split into three contiguous parts, in this order, such that:
    Every element in the first part is less than a.
    Every element in the second part is in the range [a, b] inclusive.
    Every element in the third part is greater than b.
    Any of the three parts may be empty.
    In one adjacent swap, you may swap two neighboring elements of nums.
    Return the minimum number of adjacent swaps required to make nums good. Since the answer may be very large, return it modulo 109 + 7.

    Example 1:
    Input: nums = [1,3,2,4,5,6], a = 3, b = 4
    Output: 1
    Explanation:
    Swap nums[1] and nums[2]. The array becomes [1, 2, 3, 4, 5, 6].
    This array is good because it can be split into [1, 2], [3, 4], and [5, 6].

    Constraints:
    1 <= nums.length <= 10**5
    ​​​​​​​1 <= nums[i] <= 10**9
    1 <= a < b <= 10**9
    '''
    def minAdjacentSwaps(self, nums: list[int], a: int, b: int) -> int:
        mod = 10**9 + 7
        mb = rb = ans = 0

        for x in nums:
            if x < a:
                ans += mb + rb
            elif x <= b:
                ans += rb
                mb += 1
            else:
                rb += 1

        return ans % mod
    '''
    3995. Minimum Cost to Convert String III

    You are given two strings, source and target.
    You are also given a 2D string array rules, where rules[i] = [patterni, replacementi], and an integer array costs, where costs[i] is the base cost of applying rules[i]. Both arrays have the same length. Additionally, patterni and replacementi have the same length.
    You may apply any rule any number of times. Each rule application works as follows:
    Choose an index l such that the range of positions from l to l + patterni.length - 1 exists in the current string and none of these positions has been used in a previous rule application.
    For each index j, the character patterni[j] must either be equal to the current character at position l + j, or be '*'.
    Replace the characters in this range with replacementi. The replacement is used exactly as given and does not contain wildcards.
    The cost of this rule application is costs[i] plus the number of '*' characters in patterni.
    Once a character position has been used in a rule application, it cannot be used in any later rule application.
    Since every patterni and replacementi have the same length, character positions are preserved after every rule application.
    Return the minimum total cost required to transform source into target. If it is impossible, return -1.

    Example 1:
    Input: source = "hello", target = "world", rules = [["he","wo"],["llo","rld"]], costs = [3,4]
    Output: 7
    Explanation:
    Apply rules[0] to replace "he" with "wo" at cost 3, so the string becomes "wollo".
    Apply rules[1] to replace "llo" with "rld" at cost 4, so the string becomes "world".
    The total cost is 3 + 4 = 7.

    Constraints:
    1 <= source.length == target.length <= 5000
    source and target consist of lowercase English letters.
    1 <= rules.length == costs.length <= 200
    rules[i] = [patterni, replacementi]
    1 <= patterni.length == replacementi.length <= 20
    patterni contains at least one lowercase English letter and at most 5 '*' characters.
    replacementi contains only lowercase English letters.
    1 <= costs[i] <= 1000
    '''
    def minCost(self, source: str, target: str, rules: list[list[str]], costs: list[int]) -> int:
        n=len(source)
        m=len(target)
        if n!=m: return -1

        inf=10**18
        dp=[inf]*(n+1)
        dp[n]=0

        pro=[]
        for (pat,rep), c in zip(rules, costs):
            pro.append(
                (pat,rep,len(pat),c+pat.count('*'))
            )
        
        for i in range(n-1,-1,-1):
            if source[i]==target[i]:
                dp[i]=dp[i+1]
            
            for pat,rep,l,cost in pro:
                if i+l>n: continue

                okay=True
                for k in range(l): 
                    # match pattern with source
                    if pat[k]!='*' and pat[k]!=source[i+k]:
                        okay=False
                        break
                if not okay:
                    continue

                for k in range(l):
                    #match replacement with target
                    if rep[k]!=target[i+k]:
                        okay=False
                        break
                if not okay: 
                    continue

                dp[i]=min(
                    dp[i], cost+dp[i+l]
                )
        return -1 if dp[0]==inf else dp[0]
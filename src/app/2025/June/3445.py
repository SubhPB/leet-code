'''
    3445. Maximum Difference Between Even and Odd Frequency II

    You are given a string s and an integer k. Your task is to find the maximum difference between the frequency of two characters, freq[a] - freq[b], in a substring subs of s, such that:

    subs has a size of at least k.
    Character a has an odd frequency in subs.
    Character b has an even frequency in subs.
    Return the maximum difference.

    Note that subs can contain more than 2 distinct characters.

    Example 1:

    Input: s = "12233", k = 4

    Output: -1

    Explanation:

    For the substring "12233", the frequency of '1' is 1 and the frequency of '3' is 2. The difference is 1 - 2 = -1.

    Example 2:

    Input: s = "1122211", k = 3

    Output: 1

    Explanation:

    For the substring "11222", the frequency of '2' is 3 and the frequency of '1' is 2. The difference is 3 - 2 = 1.

    Example 3:

    Input: s = "110", k = 3

    Output: -1

    Constraints:

    3 <= s.length <= 3 * 104
    s consists only of digits '0' to '4'.
    The input is generated that at least one substring has a character with an even frequency and a character with an odd frequency.
    1 <= k <= s.length
'''


class Solution:
    def maxDifference(self, s: str, k: int) -> int:
        '''
            Fully working algorithm.
            T.C = O( n(n+1)/2 ) -> O(n^2)
        '''
        n = len(s)
        initialstate = [[0]*5 for i in range((n-k+1))]

        for i in range(n-k+1):
            if i != 0:
                prev, new = int(s[i-1]), int(s[i+k-1])
                initialstate[i] = [*initialstate[i-1]]
                initialstate[i][prev] -= 1
                initialstate[i][new] += 1
            else:
                for j in range(k): initialstate[0][int(s[j])] += 1
        
        inf = 10**9
        res = -inf

        def finddiff(state:list[int]):
            minevencnt, maxoddcnt = inf, -inf
            for i in range(5):
                if state[i]==0: continue
                if (state[i]&1): maxoddcnt = max(maxoddcnt, state[i])
                else: minevencnt = min(minevencnt, state[i])
            return maxoddcnt-minevencnt

        for i in range(n-k+1):
            currstate = initialstate[i]
            res = max(res, finddiff(currstate))
            for j in range(i+k, n):
                currstate[int(s[j])] += 1
                res = max(res, finddiff(currstate))

        return res

    def optimizedSol(self, s:str, k:int):
        n, inf = len(s), 10**9
        res = -inf

        def getState(a:int, b:int):
            state = 0
            state |= (1 if b&1 else 0)
            state |= (2 if a&1 else 0)
            return state

        for a in range(5):
            for b in range(5):
                if a!=b:
                    '''
                        Symbol{1} -> odd count
                        Symbol{0} -> even count
                        There are can at most 4 states possible
                        "00" -> even&even
                        "01" -> even&odd
                        "10" -> odd&even
                        "11" -> odd&odd
                    '''
                    minPrevState = [inf]*4

                    cnt_a, cnt_b = 0, 0
                    prev_cnt_a, prev_cnt_b = 0, 0

                    l, r = -1, 0

                    while r<n:
                        cnt_a += (1 if int(s[r])==a else 0)
                        cnt_b += (1 if int(s[r])==b else 0)

                        # (substr is of at least k size) and (b should be at least 2) and (s should be at least 1)
                        while r-l>=k and cnt_b-prev_cnt_b >=2 and cnt_a-prev_cnt_a>=1:
                            leftState = getState(prev_cnt_a, prev_cnt_b)
                            minPrevState[leftState] = min(minPrevState[leftState], prev_cnt_a-prev_cnt_b)

                            l+=1
                            if int(s[l]) == a: prev_cnt_a+=1
                            elif int(s[l])==b: prev_cnt_b+=1
                        
                        rightState = getState(cnt_a, cnt_b)
                        leftState = rightState^2
                        diff = minPrevState[leftState]

                        if diff != inf:
                            res = max(
                                res,
                                (cnt_a - cnt_b) - diff
                            )
                        r+=1
        return res
    

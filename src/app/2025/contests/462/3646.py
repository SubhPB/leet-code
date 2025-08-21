'''
3646. Next Special Palindrome Number

    You are given an integer n.

    A number is called special if:

    It is a palindrome.
    Every digit k in the number appears exactly k times.
    Return the smallest special number strictly greater than n.

    Example 1:

    Input: n = 2

    Output: 22

    Explanation:

    22 is the smallest special number greater than 2, as it is a palindrome and the digit 2 appears exactly 2 times.

    Example 2:

    Input: n = 33

    Output: 212

    Explanation:

    212 is the smallest special number greater than 33, as it is a palindrome and the digits 1 and 2 appear exactly 1 and 2 times respectively.

    python src/app/2025/contests/462/3646.py
'''
from typing import List

dp:List[List[int]] = [
    [] for _ in range(sum([2,4,6,8,10]))
]

def dfs(px:int):
    mask:List[int] = []; tn:List[int] = []
    for x in [2,4,6,8]:
        tn.append(px); mask.append((1<<px) if px else 0)
        for i, sm in enumerate(tn):
            totalSm = x+sm; newMask = mask[i] | 1<<x
            dp[totalSm].append(newMask)
            tn[i]=totalSm; mask[i]=newMask

dfs(0) # calculating dp for even only nums

for px in [1,3,5,7,9]:  # calculating dp evens + one odd scenario
    dfs(px)
    dp[px].append(1<<px) # obvious base-cases for odd nums

for i,x in enumerate(dp):
    print(f'i={i} W x={[bin(a) for a in (sorted(x))]}')

class Solution:
    def findBest(self,n:int, d:int):

        res = 0

        def reverse(arr:List[any]):
            narr = [arr[i] for i in range(len(arr)-1,-1,-1)]
            return narr
        def map(arr:List[any],fn:function):
            narr = [fn(x) for x in arr]
            return narr

        def hlfParse(x:List[int|str], m=[]):
            x = map(x,str); m = map(m,str)
            return int(''.join(x + m + reverse(x)))
        
        for candidate in sorted(dp[d]):
            digits:List[int] = []; m = []
            for i in range(candidate.bit_length()-1, -1, -1):
                if candidate&(1<<i):
                    digits.append(i)
                    if (i&1): m = [i]
            
            hlf = []
            for x in digits:
                for i in range(x//2): hlf.append(x)

            maxPossible = hlfParse(hlf,m)
            if maxPossible > n:
                res = maxPossible
                left, right = hlf[:1], hlf[1:]
                while right:
                    pq = left[-1]
                    for dgt in reverse(right):
                        newLeft = [*left]; newLeft[-1] = dgt; newLeft.append(pq)
                        newRight = [*right]; newRight.remove(dgt)
                        tempRes = hlfParse(newLeft+newRight, m)
                        if tempRes > n:
                            left = newLeft; right = newRight
                            res = min(res,tempRes)
                return res
        return res
    
    def specialPalindrome(self, n: int) -> int:
        d = len(str(n))
        # Observation: Using 2 odd digits is never possible to get right answer!
        #    To get the minimum result we will try to find smallest candidate of same digit length as of n
        #    If not found then we'll find smallest digit num with the digit length eql 'd+1', which is definitely an answer!

        # arr.reverse() & x[i] = int not str | FIX! 

        res = self.findBest(n,d)
        if res <= n: res = self.findBest(n,d+1)

        return res

from typing import List, Dict, Optional, Tuple

class Solution:
    # Entry point
    def specialPalindrome(self, n: int) -> int:
        s = str(n)
        L = len(s)

        masks_by_len = self._catalog_masks_by_length()

        # 1) Try same length
        if L in masks_by_len:
            best = self._min_palindrome_gt_for_length(s, L, masks_by_len[L])
            if best is not None:
                return best

        # 2) Try next feasible length(s) in increasing order
        for LL in range(L + 1, 30):  # max feasible length = 29
            if LL in masks_by_len:
                # Minimal candidate for this length across all masks
                ans = None
                for (center, left_counts) in masks_by_len[LL]:
                    cand = self._build_min_pal_from_left_counts(LL, center, left_counts)
                    if ans is None or cand < ans:
                        ans = cand
                if ans is not None:
                    return ans

        # If input is already >= 10^29 no special numbers exist beyond (by constraints)
        # Problem setters typically ensure we never reach here.
        return -1

    # ---------- Mask cataloguing (complete & tiny search space) ----------

    def _catalog_masks_by_length(self) -> Dict[int, List[Tuple[Optional[int], Dict[int, int]]]]:
        """
        Returns a map: length -> list of (center_digit or None, left_half_counts)
        where left_half_counts[d] = how many copies of digit d must be placed in the left half.
        """
        evens = [2, 4, 6, 8]
        odds  = [1, 3, 5, 7, 9]

        res: Dict[int, List[Tuple[Optional[int], Dict[int, int]]]] = {}

        # Enumerate all subsets of evens (16 choices)
        for mask in range(1 << len(evens)):
            sum_even = 0
            even_counts_left = {}  # digit -> count in LEFT half (k/2)
            ok = True
            for i, k in enumerate(evens):
                if mask & (1 << i):
                    sum_even += k
                    even_counts_left[k] = even_counts_left.get(k, 0) + (k // 2)
                    # (even k contributes k/2 copies to left)

            # Option A: no odd (even length)
            L = sum_even
            if 1 <= L <= 29:  # length 0 would be "empty number", disallow
                res.setdefault(L, []).append((None, dict(even_counts_left)))

            # Option B: exactly one odd
            for o in odds:
                L2 = sum_even + o
                if L2 <= 29:
                    left_counts = dict(even_counts_left)
                    left_counts[o] = left_counts.get(o, 0) + ((o - 1) // 2)
                    res.setdefault(L2, []).append((o, left_counts))

        return res

    # ---------- Build the minimal palindrome for a given mask ----------

    def _build_min_pal_from_left_counts(self, L: int, center: Optional[int], left_counts: Dict[int, int]) -> int:
        # Build the lexicographically smallest left half (ascending digits)
        P = L // 2
        left = []
        counts = dict(left_counts)
        for _ in range(P):
            for d in range(1, 10):
                if counts.get(d, 0) > 0:
                    left.append(d)
                    counts[d] -= 1
                    break

        if center is None:
            digits = left + left[::-1]
        else:
            digits = left + [center] + left[::-1]

        return self._digits_to_int(digits)

    # ---------- Find minimal palindrome > n for fixed length L ----------

    def _min_palindrome_gt_for_length(
        self, s: str, L: int, masks: List[Tuple[Optional[int], Dict[int, int]]]
    ) -> Optional[int]:
        """
        For all masks feasible at length L, find the lexicographically smallest palindrome > s.
        """
        assert len(s) == L
        best: Optional[int] = None

        for (center, left_counts) in masks:
            cand = self._first_pal_gt_n_with_mask(s, L, center, left_counts)
            if cand is not None and (best is None or cand < best):
                best = cand

        return best

    def _first_pal_gt_n_with_mask(
        self, s: str, L: int, center: Optional[int], left_counts: Dict[int, int]
    ) -> Optional[int]:
        """
        Build the minimal palindrome with this (center, left_counts) that is strictly > s.
        Strategy: lexicographic DFS on the defining prefix: left half (+ center if odd),
        trying digits in ascending order and backtracking with a bound against s's prefix.
        """
        P = L // 2
        T = P + (1 if center is not None else 0)  # length of defining prefix

        # Bound prefix from s (first T digits)
        bound_prefix = [int(ch) for ch in s[:T]]

        # Prepare multiset for the P left positions
        counts = dict(left_counts)  # digit -> remaining slots in LEFT half
        prefix: List[int] = []

        # We implement iterative backtracking with state per position.
        # At pos < P: we can choose any digit with counts[d] > 0.
        # At pos == P (only if odd): forced digit = center.
        pos = 0
        # For each left position, remember which digits we've tried already at that pos.
        tried_stack: List[List[int]] = [[] for _ in range(T)]
        tight_stack: List[bool] = []
        tight = True  # are we equal to bound so far?

        def can_finish_min(prefix_so_far: List[int], pos_now: int, tight_now: bool) -> bool:
            """
            Quick feasibility check (optional). Here we only need to know if the remaining
            left slots can be filled at all; since counts sum is fixed, this is always true
            unless we've overused counts. We'll rely on counts only, so return True.
            """
            return True

        while True:
            if pos == T:
                # Prefix complete → build full palindrome and check > s
                full = self._pal_from_prefix(L, center, prefix)
                if full > int(s):
                    return full
                # Need to backtrack and increase prefix lexicographically
                pos -= 1
                if pos < 0:
                    break
                # Undo last step
                if pos < P:
                    last = prefix.pop()
                    counts[last] += 1
                else:
                    # pos == P and it was center (no counts change)
                    prefix.pop()
                tight = tight_stack.pop()
                # Continue trying next candidate at this pos (handled below)

            else:
                if pos < P:
                    # Left-half position with choices from counts
                    # Determine lower bound digit if tight
                    lb = bound_prefix[pos] if tight else 1

                    progressed = False
                    for d in range(max(lb, 1), 10):
                        if d in tried_stack[pos]:
                            continue
                        if counts.get(d, 0) <= 0:
                            continue
                        # try d
                        tried_stack[pos].append(d)
                        # Save tight, place
                        tight_stack.append(tight)
                        prefix.append(d)
                        counts[d] -= 1
                        new_tight = tight and (d == lb)
                        # If lb arose from tight, but we picked d > lb, tight becomes False
                        if d > lb:
                            new_tight = False
                        # (Feasibility always OK because counts control exact total)
                        tight = new_tight
                        pos += 1
                        progressed = True
                        break

                    if not progressed:
                        # Exhausted options at this pos → backtrack
                        tried_stack[pos].clear()
                        if pos == 0:
                            break
                        pos -= 1
                        if pos < P:
                            last = prefix.pop()
                            counts[last] += 1
                        else:
                            prefix.pop()  # center
                        tight = tight_stack.pop()
                        continue

                else:
                    # pos == P and odd length: forced center
                    forced = center
                    lb = bound_prefix[pos] if tight else 1
                    tried_stack[pos] = [forced]  # mark as done
                    tight_stack.append(tight)
                    prefix.append(forced)
                    if tight and forced < lb:
                        # Center is too small under tight → must backtrack earlier left digit
                        prefix.pop()
                        tight_stack.pop()
                        tried_stack[pos].clear()
                        # backtrack
                        pos -= 1
                        if pos < 0:
                            break
                        if pos < P:
                            last = prefix.pop()
                            counts[last] += 1
                        else:
                            prefix.pop()
                        tight = tight_stack.pop()
                    else:
                        # proceed
                        tight = tight and (forced == lb)
                        pos += 1

        return None

    def _pal_from_prefix(self, L: int, center: Optional[int], prefix: List[int]) -> int:
        P = L // 2
        if center is None:
            left = prefix[:P]
            digits = left + left[::-1]
        else:
            left = prefix[:P]
            digits = left + [center] + left[::-1]
        return self._digits_to_int(digits)

    @staticmethod
    def _digits_to_int(digs: List[int]) -> int:
        x = 0
        for d in digs:
            x = x * 10 + d
        return x

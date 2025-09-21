from typing import List

class BiweeklyContest165:
    ''' Question-II
        You are given two integers w and m, and an integer array arrivals, where arrivals[i] is the type of item arriving on day i (days are 1-indexed).
        Items are managed according to the following rules:
        Each arrival may be kept or discarded; an item may only be discarded on its arrival day.
        For each day i, consider the window of days [max(1, i - w + 1), i] (the w most recent days up to day i):
        For any such window, each item type may appear at most m times among kept arrivals whose arrival day lies in that window.
        If keeping the arrival on day i would cause its type to appear more than m times in the window, that arrival must be discarded.
        Return the minimum number of arrivals to be discarded so that every w-day window contains at most m occurrences of each type.
    '''
    def minArrivalsToDiscard(self, arrivals: List[int], w: int, m: int) -> int:
        n = len(arrivals); res = 0
        freq = {}; discarded = [False]*(n+1)

        for right in range(1,n+1):
            left = max(right-w+1, 1)
            if left>1 and not discarded[left-1]: 
                oldItem = arrivals[left-2]
                freq[oldItem] -= 1
            todayItem = arrivals[right-1]
            if freq.get(todayItem,0)==m:
                # remember day:right is not appended to window so left pointer need to be aware of it through 'discarded'
                discarded[right]=True
                res+=1
            else: freq[todayItem]=1+freq.get(todayItem,0)


        return res


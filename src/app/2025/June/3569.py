'''
3569. Maximize Count of Distinct Primes After Split
    You are given an integer array nums having length n and a 2D integer array queries where queries[i] = [idx, val].

    For each query:

    Update nums[idx] = val.
    Choose an integer k with 1 <= k < n to split the array into the non-empty prefix nums[0..k-1] and suffix nums[k..n-1] such that the sum of the counts of distinct prime values in each part is maximum.
    Note: The changes made to the array in one query persist into the next query.

    Return an array containing the result for each query, in the order they are given.

    Example 1:

    Input: nums = [2,1,3,1,2], queries = [[1,2],[3,3]]

    Output: [3,4]

    Explanation:

    Initially nums = [2, 1, 3, 1, 2].
    After 1st query, nums = [2, 2, 3, 1, 2]. Split nums into [2] and [2, 3, 1, 2]. [2] consists of 1 distinct prime and [2, 3, 1, 2] consists of 2 distinct primes. Hence, the answer for this query is 1 + 2 = 3.
    After 2nd query, nums = [2, 2, 3, 3, 2]. Split nums into [2, 2, 3] and [3, 2] with an answer of 2 + 2 = 4.
    The output is [3, 4].
    Example 2:

    Input: nums = [2,1,4], queries = [[0,1]]

    Output: [0]

    Explanation:

    Initially nums = [2, 1, 4].
    After 1st query, nums = [1, 1, 4]. There are no prime numbers in nums, hence the answer for this query is 0.
    The output is [0].
    

    Constraints:

    2 <= n == nums.length <= 5 * 104
    1 <= queries.length <= 5 * 104
    1 <= nums[i] <= 105
    0 <= queries[i][0] < nums.length
    1 <= queries[i][1] <= 105

    python ./src/app/2025/June/3569.py
'''

import math, collections, heapq

class SegmentTree:
    def __init__(self, arr:list[int]):
        self.n = len(arr)
        self.N = 1
        while self.N < self.n: #self.N to make perfect binary segment tree
            self.N *= 2
        space = self.N*2 
        self.tree = [0]*space
        self.lazy = [0]*space
        
        for i, v in enumerate(arr):
            self.tree[self.N+i] = v #Lying the leaf nodes
        for i in range(self.N-1, 0, -1):#Assigning range sum
            self.tree[i] = self.tree[2*i]+self.tree[2*i+1]


    def _apply(self, idx, add, length):
        #Apply the pending add to the node idx covering 'length' array elements
        self.tree[idx] += add*length
        self.lazy[idx] += add #For the future reference

    def _push(self, idx, length):
        #Work on pending add at idx all down to its children
        if self.lazy[idx] == 0: return
        add = self.lazy[idx]
        #Child node would have half the # of children as this current node has.
        self._apply(2*idx, add, length//2)
        self._apply(2*idx+1, add, length//2)
        self.lazy[idx]=0

    def range_add(self, l, r, val):
        if l>r: return
        def _add(idx, left, right, ql, qr, val): 
            if qr < left or right < ql: return
            
            if ql <= left and right <= qr: #Fully covered
                self._apply(idx, val, right-left+1)
                return 
            self._push(idx, right-left+1)
            mid = (left+right)//2
            _add(2*idx, left, mid, ql, qr, val)
            _add(2*idx+1, mid+1, right, ql, qr, val)
            self.tree[idx] = self.tree[2*idx]+self.tree[2*idx+1]
        _add(1, 0, self.N-1, l, r, val)

    def max_leaf(self)->int:
        inf = 10**9
        def _dfs(idx, left, right):
            if left > self.n-1:
                return -inf
            if left == right:
                return self.tree[idx]
            self._push(idx, right-left+1)
            mid = (left+right)//2
            return max(
                _dfs(2*idx, left, mid),
                _dfs(2*idx+1, mid+1, right)
            )
        return _dfs(1, 0, self.N-1)


class Solution:
    def maximumCount(self, nums: list[int], queries: list[list[int]]) -> list[int]:
        
        isPrime = [False]*106
        for i in range(2,106):
            if i in [2,3,5,7]: isPrime[i] = True
            elif 0 in [i%2, i%3]: continue
            elif i>10:
                isPrime[i] = True#Assume it was a prime
                limit, k = int(math.sqrt(i)), 5
                while k <= limit and isPrime:
                    if i%k==0 or i%(k+2)==0: 
                        isPrime[i] = False
                    k+=6
        
        n, m = len(nums), len(queries)
        indexes = collections.defaultdict(list)

        #scores[k] means what was max score after array was partitioned right after nums[k] element
        scores, res = [0]*(n-1), [0]*m
        leftCounter, rightCounter = collections.Counter(), collections.Counter()
        for i, num in enumerate(nums):
            if isPrime[num]:
                indexes[num].append(i)
                rightCounter[num]+=1
        for i in range(n-1):
            if isPrime[nums[i]]:
                leftCounter[nums[i]]+=1
                rightCounter[nums[i]]-=1
                if not rightCounter[nums[i]]:
                    del rightCounter[nums[i]]
            scores[i] = len(leftCounter)+len(rightCounter)
            res[0] = max(res[0], scores[i])
        
        segmentTree = SegmentTree(scores)

        for i, [idx, val] in enumerate(queries):
            existing_val = nums[idx]
            if existing_val != val:
                #Remove the existing value
                if isPrime[existing_val]:
                    is_uniq_prime = len(indexes[existing_val])==1
                    if is_uniq_prime:
                        segmentTree.range_add(0, n-2, -1)
                        del indexes[existing_val]
                        res[i] = res[max(i-1, 0)]-1
                    else: #existing value is repeating prime
                        fi, li = indexes[existing_val][0], indexes[existing_val][-1]
                        if idx <= fi:
                            heapq.heappop(indexes[existing_val])
                            if idx==fi: fi = indexes[existing_val][0]
                            segmentTree.range_add(idx, fi-1, -1)
                            res[i] = segmentTree.max_leaf()
                        elif idx >= li:
                            indexes[existing_val].pop()
                            if idx==li: li = indexes[existing_val][-1]
                            segmentTree.range_add(li, idx-1, -1)
                            res[i] = segmentTree.max_leaf()
                        else:#No effect on score
                            l, r = 0, len(indexes[existing_val])-1
                            while l<r:
                                mid = (l+r)//2
                                if idx<indexes[existing_val][mid]:
                                    r=mid-1
                                elif idx>indexes[existing_val][mid]:
                                    l=mid+1
                                else:
                                    l, r, = mid, mid
                            indexes[existing_val].pop(l)
                            res[i] = res[max(i-1, 0)]

                nums[idx] = val

                #Add the new value
                if isPrime[val]:
                    is_uniq_prime = val not in indexes
                    if is_uniq_prime:
                        segmentTree.range_add(0, n-2, 1)
                        res[i] = res[i]+1 if isPrime[existing_val] else res[max(i-1, 0)]+1
                        indexes[val].append(idx)
                    else:#repeating prime
                        fi, li = indexes[val][0], indexes[val][-1]
                        if idx < fi:
                            segmentTree.range_add(idx, fi-1, 1)
                            heapq.heappush(indexes[val], idx)
                            res[i] = segmentTree.max_leaf()
                        elif idx > li:
                            segmentTree.range_add(li, idx-1, 1)
                            indexes[val].append(idx)
                            res[i] = segmentTree.max_leaf()
                        else:
                            heapq.heappush(indexes[val], idx)
                            res[i] = res[i] if isPrime[existing_val] else res[max(i-1, 0)]

                if not isPrime[existing_val] and not isPrime[val]:
                    res[i] = res[max(i-1, 0)]
                
            else:
                res[i] = res[max(i-1, 0)] 
        return res
        


if __name__ == "__main__":
    Testcases = []
    add = lambda nums,queries: Testcases.append([nums, queries])
    # add(nums = [2,1,3,1,2], queries = [[1,2],[3,3]])
    # add(nums = [2,1,4], queries = [[0,1]])
    # add(nums=[42,16],queries=[[1,65],[1,70]])
    # add(nums=[2,34], queries=[[1,2],[1,3]])
    add(nums=[11,65,13,90,5,5,40,3,76], queries=[[8,31],[1,5],[8,76],[5,23],[6,5],[5,10],[5,99],[4,47],[6,73]])
    sol = Solution()
    for [nums, queries] in Testcases:
        print(f'Nums={nums} Queries={queries} result={sol.maximumCount(nums, queries)}')
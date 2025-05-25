'''
3362. Zero Array Transformation III

You are given an integer array nums of length n and a 2D array queries where queries[i] = [li, ri].

Each queries[i] represents the following action on nums:

Decrement the value at each index in the range [li, ri] in nums by at most 1.
The amount by which the value is decremented can be chosen independently for each index.
A Zero Array is an array with all its elements equal to 0.

Return the maximum number of elements that can be removed from queries, such that nums can still be converted to a zero array using the remaining queries. If it is not possible to convert nums to a zero array, return -1.

 

Example 1:

Input: nums = [2,0,2], queries = [[0,2],[0,2],[1,1]]

Output: 1

Explanation:

After removing queries[2], nums can still be converted to a zero array.

Using queries[0], decrement nums[0] and nums[2] by 1 and nums[1] by 0.
Using queries[1], decrement nums[0] and nums[2] by 1 and nums[1] by 0.
Example 2:

Input: nums = [1,1,1,1], queries = [[1,3],[0,2],[1,3],[1,2]]

Output: 2

Explanation:

We can remove queries[2] and queries[3].

Example 3:

Input: nums = [1,2,3,4], queries = [[0,3]]

Output: -1

Explanation:

nums cannot be converted to a zero array even after using all the queries.

 

Constraints:

1 <= nums.length <= 105
0 <= nums[i] <= 105
1 <= queries.length <= 105
queries[i].length == 2
0 <= li <= ri < nums.length

python ./src/app/2025/May/3362.py
'''
import heapq
class Solution:
    def maxRemoval(self, nums: list[int], queries: list[list[int]]) -> int:
        
        queries.sort(key= lambda x: x[0]-x[1])#keep longest ranges at first
        queries.sort(key= lambda x: x[0])#keep ranges with smallest 'st' at first
        # print(f'queries',queries)
        n, qn = len(nums), len(queries)
        q, used = 0, 0

        dec, diff = 0, [0]*(n+1)
        print(f'Queries={queries}')

        for i in range(n):
            dec += diff[i]
            if nums[i] - dec <= 0: continue

            while q<qn and nums[i] - dec > 0 and queries[q][0] <= i:
                
                # print(f'{queries[q]} i={i} num={nums[i]} sortedQ=',queries)
                if not queries[q][1]<i: 
                    #Can greedly pick the one with farthest range
                    gq, gqi, farthest = q, q, queries[q][1] - i
                    while gqi<qn and queries[gqi][0] <= i:
                        if (queries[gqi][1] - i) > farthest: 
                            farthest = queries[gqi][1] - i
                            gq = gqi
                        gqi += 1
                    
                    st, ed = queries[gq]

                    diff[st] += 1
                    diff[ed+1] -= 1
                    dec += 1

                    if gq != q: # means queries[q] still not used
                        queries.pop(gq)
                        queries.insert(q+1,queries[q])
                    used+=1
                q+=1
            
            if nums[i]-dec >0: return -1
        return qn-used

    def maxRemoval2(self, nums: list[int], queries: list[list[int]]) -> int:
        n, used_query, available_query = len(nums), [], []
        # "used_query" stores end points
        # "available_query" works as max-heap using -ve values

        queries.sort(key=lambda x:x[0])

        query_pos = 0
        applied_cnt = 0

        for i in range(n):
            '''
            Push all queries starting at 'i' into "available-query"
            '''
            while query_pos < len(queries) and queries[query_pos][0] == i:
                end = queries[query_pos][1]
                heapq.heappush( #MaxHeap '-end' to keep longest range at front
                    available_query, -end
                )
                query_pos+=1
            
            nums[i] -= len(used_query)

            #Apply queries if num[i] > 0
            while nums[i]>0 and available_query and -available_query[0] >= i:
                end = -heapq.heappop(available_query)
                heapq.heappush(used_query, end)
                nums[i] -= 1
                applied_cnt += 1
            
            if nums[i]>0: return -1

            #Remove queries that end at 'i' from used_query
            while used_query and used_query[0] == i:
                heapq.heappop(used_query)


        return len(queries) - applied_cnt
if __name__ == '__main__':
    Tcases = [
        [
            [1,1,1,1], [[1,3],[0,2],[1,3],[1,2]]
        ]
    ]

    sol = Solution()
    for [nums, queries] in Tcases:
        print('\n')
        print(f'nums={nums} queries={queries}')
        print(f'sol1={sol.maxRemoval(nums, queries)}')
        print('--Sol2--')
        print(f'sol2={sol.maxRemoval2(nums, queries)}')
            
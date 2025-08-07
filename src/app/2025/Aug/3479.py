'''
    3479. Fruits Into Baskets III

    You are given two arrays of integers, fruits and baskets, each of length n, where fruits[i] represents the quantity of the ith type of fruit, and baskets[j] represents the capacity of the jth basket.

    From left to right, place the fruits according to these rules:

    Each fruit type must be placed in the leftmost available basket with a capacity greater than or equal to the quantity of that fruit type.
    Each basket can hold only one type of fruit.
    If a fruit type cannot be placed in any basket, it remains unplaced.
    Return the number of fruit types that remain unplaced after all possible allocations are made.

    Example 1:

    Input: fruits = [4,2,5], baskets = [3,5,4]

    Output: 1

    Explanation:

    fruits[0] = 4 is placed in baskets[1] = 5.
    fruits[1] = 2 is placed in baskets[0] = 3.
    fruits[2] = 5 cannot be placed in baskets[2] = 4.
    Since one fruit type remains unplaced, we return 1.

    Example 2:

    Input: fruits = [3,6,1], baskets = [6,4,7]

    Output: 0

    Explanation:

    fruits[0] = 3 is placed in baskets[0] = 6.
    fruits[1] = 6 cannot be placed in baskets[1] = 4 (insufficient capacity) but can be placed in the next available basket, baskets[2] = 7.
    fruits[2] = 1 is placed in baskets[1] = 4.
    Since all fruits are successfully placed, we return 0.

    Constraints:

    n == fruits.length == baskets.length
    1 <= n <= 10^5
    1 <= fruits[i], baskets[i] <= 10^9
'''
from typing import List
class Tree:
    def __init__(self,nums:List[int]):
        self.__build(given_nums=nums)
    def __build(self,given_nums:List):
        n=len(given_nums); msb = (n-1).bit_length()+1; tree_len = (1<<msb)-1
        self.nums = [-1]*tree_len; leafs_cnt=1<<(msb-1)
        for i in range(msb):
            # length of each element in this row equals 2^(i)
            # length of row equals leafs_cnt/2^(i)
            row_len = leafs_cnt//(1<<i); prefix = (1<<(msb-i-1))-1
            for j in range(row_len):
                idx = prefix+j
                if i==0:
                    self.nums[idx] = given_nums[j] if j<n else -1
                else:
                    self.nums[idx] = max(self.nums[2*idx+1],self.nums[2*idx+2])

class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        tree = Tree(baskets).nums; res = 0

        def dfs(idx:int,value:int):
            if tree[idx]<value: return -1
            elif 2*idx+1>=len(tree): return idx
            else:
                lcv = tree[2*idx+1]
                if lcv>=value:
                    return dfs(2*idx+1,value)
                else: return dfs(2*idx+2,value)


        for fruit in fruits:
            idx = dfs(0,fruit)
            if idx != -1:
                pdx = (idx-1)//2; tree[idx] = -1
                while pdx>=0:
                    tree[pdx] = max(tree[2*pdx+1], tree[2*pdx+2])
                    pdx = (pdx-1)//2
                
            else: res +=1
        return res
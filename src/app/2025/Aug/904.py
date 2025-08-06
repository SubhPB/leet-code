'''
    904. Fruit Into Baskets
    You are visiting a farm that has a single row of fruit trees arranged from left to right. The trees are represented by an integer array fruits where fruits[i] is the type of fruit the ith tree produces.

    You want to collect as much fruit as possible. However, the owner has some strict rules that you must follow:

    You only have two baskets, and each basket can only hold a single type of fruit. There is no limit on the amount of fruit each basket can hold.
    Starting from any tree of your choice, you must pick exactly one fruit from every tree (including the start tree) while moving to the right. The picked fruits must fit in one of your baskets.
    Once you reach a tree with fruit that cannot fit in your baskets, you must stop.
    Given the integer array fruits, return the maximum number of fruits you can pick.

    Example 1:

    Input: fruits = [1,2,1]
    Output: 3
    Explanation: We can pick from all 3 trees.
    Example 2:

    Input: fruits = [0,1,2,2]
    Output: 3
    Explanation: We can pick from trees [1,2,2].
    If we had started at the first tree, we would only pick from trees [0,1].
    Example 3:

    Input: fruits = [1,2,3,2,2]
    Output: 4
    Explanation: We can pick from trees [2,3,2,2].
    If we had started at the first tree, we would only pick from trees [1,2].

    Constraints:

    1 <= fruits.length <= 10^5
    0 <= fruits[i] < fruits.length
    python ./src/app/2025/Aug/904.py
'''
from typing import List
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        n = len(fruits); res = min(2,n)
        if n>2:
            for i in range(1,n): 
                if fruits[i]!=fruits[i-1]: break
            [a,b] = [fruits[0], fruits[i]]
            sizeA, sizeB = i, 1; ai = i-1; bi = i
            res = sizeA+sizeB
            for i in range(i+1,n):
                if fruits[i]==a: sizeA+=1; ai=i
                elif fruits[i]==b: sizeB+=1; bi=i
                else:
                    if fruits[i-1] == a: 
                        # 'a' still be 'a'
                        sizeA = i-bi-1
                    else:
                        a = b; sizeA = i-ai-1; ai=bi
                    b=fruits[i];sizeB=1; bi=i
                res=max(res,sizeA+sizeB)
        return res
    
if __name__ == '__main__':
    testcases = [
        # [3,3,3,1,2,1,1,2,3,3,4],
        # [1,0,1,4,1,4,0,7],
        # [1,2,3,2,2],
        # [1,0,3,4,3],
        [6,2,1,1,3,6,6],
        [0,0,1,1]
    ]
    for fruits in testcases:
        print(f'fruits={fruits} res={Solution().totalFruit(fruits)}')
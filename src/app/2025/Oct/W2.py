from bisect import bisect_left as bl
from typing import List
class Solution:
    '''
    2300. Successful Pairs of Spells and Potions

    You are given two positive integer arrays spells and potions, of length n and m respectively, where spells[i] represents the strength of the ith spell and potions[j] represents the strength of the jth potion.

    You are also given an integer success. A spell and potion pair is considered successful if the product of their strengths is at least success.

    Return an integer array pairs of length n where pairs[i] is the number of potions that will form a successful pair with the ith spell.

    Example 1:

    Input: spells = [5,1,3], potions = [1,2,3,4,5], success = 7
    Output: [4,0,3]
    Explanation:
    - 0th spell: 5 * [1,2,3,4,5] = [5,10,15,20,25]. 4 pairs are successful.
    - 1st spell: 1 * [1,2,3,4,5] = [1,2,3,4,5]. 0 pairs are successful.
    - 2nd spell: 3 * [1,2,3,4,5] = [3,6,9,12,15]. 3 pairs are successful.
    Thus, [4,0,3] is returned.
    Example 2:

    Input: spells = [3,1,2], potions = [8,5,8], success = 16
    Output: [2,0,2]
    Explanation:
    - 0th spell: 3 * [8,5,8] = [24,15,24]. 2 pairs are successful.
    - 1st spell: 1 * [8,5,8] = [8,5,8]. 0 pairs are successful. 
    - 2nd spell: 2 * [8,5,8] = [16,10,16]. 2 pairs are successful. 
    Thus, [2,0,2] is returned.
    

    Constraints:

    n == spells.length
    m == potions.length
    1 <= n, m <= 10^5
    1 <= spells[i], potions[i] <= 10^5
    1 <= success <= 10^10
    '''
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        m=len(potions); pairs=[]
        potions.sort()
        for spell in spells:
            # numerator that {rounds up / ceil} according to the divider/spell
            delta = (success+spell-1)//spell
            pairs.append(
                m-bl(potions,delta)
            )
        return pairs
    '''
    3494. Find the Minimum Amount of Time to Brew Potions
 
    You are given two integer arrays, skill and mana, of length n and m, respectively.

    In a laboratory, n wizards must brew m potions in order. Each potion has a mana capacity mana[j] and must pass through all the wizards sequentially to be brewed properly. The time taken by the ith wizard on the jth potion is timeij = skill[i] * mana[j].

    Since the brewing process is delicate, a potion must be passed to the next wizard immediately after the current wizard completes their work. This means the timing must be synchronized so that each wizard begins working on a potion exactly when it arrives. ​

    Return the minimum amount of time required for the potions to be brewed properly.

    Example 1:

    Input: skill = [1,5,2,4], mana = [5,1,4,2]

    Output: 110

    Explanation:

    Potion Number	Start time	Wizard 0 done by	Wizard 1 done by	Wizard 2 done by	Wizard 3 done by
    0	0	5	30	40	60
    1	52	53	58	60	64
    2	54	58	78	86	102
    3	86	88	98	102	110
    As an example for why wizard 0 cannot start working on the 1st potion before time t = 52, consider the case where the wizards started preparing the 1st potion at time t = 50. At time t = 58, wizard 2 is done with the 1st potion, but wizard 3 will still be working on the 0th potion till time t = 60.

    Constraints:

    n == skill.length
    m == mana.length
    1 <= n, m <= 5000
    1 <= mana[i], skill[i] <= 5000
    '''  
    def minTimeBinarySearch(self, skill: List[int], mana: List[int]) -> int:
        n=len(skill)

        def go(nums:List[int],potion:int,startTime:int):
            for i,ws in enumerate(skill):
                nums[i]=potion*ws
                nums[i]+=(nums[i-1] if i>0 else startTime)
                if i!=n-1 and nums[i]<nums[i+1]:
                    return []
            return nums
        
        nums=[0]*n
        for i,potion in enumerate(mana):
            if not i: 
                for j,ws in enumerate(skill):
                    nums[j]=potion*ws
                    if j>0:nums[j]+=nums[j-1]
            else:
                bestStartTime=nums[0]; worstStartTime=nums[-1]
                while bestStartTime<worstStartTime:
                    startTime=(bestStartTime+worstStartTime)//2
                    if go(list(nums),potion,startTime):
                        worstStartTime=startTime
                    else:
                        bestStartTime=startTime+1
                nums=go(nums,potion,bestStartTime)
            # print(f'potion#={i} nums={nums}')
        return nums[-1]

    def minTimeOptimal(self, skill: List[int], mana: List[int]) -> int:
        n=len(skill);nums=[0]*n
        for i,potion in enumerate(mana):
            if not i:
                for j,ws in enumerate(skill):
                    nums[j]=ws*potion+nums[j-1]
            else:
                for j,ws in enumerate(skill):
                    if not j:
                        nums[j]+=potion*ws
                    else:
                        nums[j]=max(nums[j],nums[j-1])+potion*ws
                for j in range(n-2,-1,-1):
                    nums[j]=nums[j+1]-potion*skill[j+1]
        return nums[-1]
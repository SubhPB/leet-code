class Solution:
    '''
    4044. Count Good Cyclic Rotations

    You are given an integer array nums of even length n.
    A cyclic rotation of nums is obtained by choosing a prefix of nums whose length is between 0 and n - 1 (inclusive), and moving it to the end of the array while preserving the order of all elements.
    A cyclic rotation is good if the sum of its first n / 2 elements is strictly greater than the sum of its last n / 2 elements.
    Return the number of cyclic rotations of nums that are good.

    Example 1:
    Input: nums = [1,2,3,4,5,6]

    Output: 3

    Constraints:
    2 <= n == nums.length <= 10**5
    1 <= nums[i] <= 10**9
    n is even.
    '''
    def countGoodRotations(self, pre: list[int]) -> int:
        n=len(pre)
        for i in range(1,n):
            pre[i]+=pre[i-1]
        total=pre[n-1]
        res=0
        for i in range(n):
            if pre[i]>=total-pre[i]:
                l=-1; r=i
                while l<r:
                    m=(l+r+1)//2
                    curr=pre[i]-pre[m-1]
                    if curr>=total-curr:
                        l=m
                    else:
                        r=m-1
                res+=n-(i-l+1)-1
            else:
                l=i; r=n-1
                while l<r:
                    m=(l+r+1)//2
                    curr= pre[i] + pre[n-1]-pre[m-1]
                    if curr>=total-curr:
                        l=m
                    else:
                        r=m-1
                if l>i+1: # reconsider
                    res+= n-((i+1)+(n-1)-l+1)-1
        return res
    '''
    4045. Count Robot Groups

    You are given a strictly increasing integer array position, where position[i] is the initial position of the ith robot at time t = 0.
    You are also given an integer array speed, where speed[i] is the constant speed of the ith robot in units per second, and an integer distance.
    Time is continuous and measured in seconds. A robot or group with speed v moves v * t units to the right over any interval of t seconds.
    Whenever the distance between two robots or groups becomes at most distance, they merge into a single group.
    If multiple robots or groups satisfy the merging condition at the same time, all merges happen simultaneously.
    In particular, every connected collection of robots or groups whose consecutive positions differ by at most distance merges into one group.
    After a merge, the resulting group takes the current position and speed of the rightmost robot in that group. Once merged, robots never separate.
    Return the number of groups remaining after all possible merges have occurred.
    
    Example 1:
    Input: position = [1,5,6,20], speed = [4,3,2,3], distance = 1
    Output: 2

    Explanation:
    Initially, the groups are {R1}, {R2}, {R3}, and {R​​​​​​​4}.
    At t = 0, the robots R2 and R3 at positions 5 and 6, respectively, merge because they are 1 unit apart.
    The resulting group moves with the position and speed of the rightmost robot R3. The groups are now {R1}, {R2, R3}, and {R​4}.
    Later at t = 2, the robot R1 catches up to the group {R2, R3} and merges with it. The groups are now {R1, R2, R3} and {R​4}.
    Thus, the answer is 2.

    Constraints:
    1 <= position.length == speed.length <= 10***5
    1 <= position[i], speed[i], distance <= 10**9
    position is strictly increasing.
    '''
    def countGroups(self, position: list[int], speed: list[int], distance: int) -> int:
        pass
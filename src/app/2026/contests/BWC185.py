class Solution:
    '''
    3964. Minimum Lights to Illuminate a Road

    You are given an integer array lights of length n, representing positions 0 through n - 1 on a road.
    For each position i:
    If lights[i] = v, where v > 0, there is a working bulb at position i that illuminates every position from max(0, i - v) to min(n - 1, i + v), inclusive.
    If lights[i] = 0, there is no working bulb at position i.
    A position is visible if it is illuminated by at least one working bulb.
    You may install additional bulbs at any positions. Each additional bulb installed at position j illuminates positions from max(0, j - 1) to min(n - 1, j + 1), inclusive.
    Return the minimum number of additional bulbs required to make every position on the road visible.
    
    Example 1:
    Input: lights = [0,0,0,0]
    Output: 2

    Explanation:
    One optimal placement is:
    Install an additional bulb at position 1, illuminating positions [0, 1, 2].
    Install an additional bulb at position 3, illuminating positions [2, 3].
    Therefore, the minimum number of additional bulbs required is 2.

    Constraints:
    1 <= n == lights.length <= 10**5
    0 <= lights[i] <= n
    '''
    def minLights(self, lights: list[int]) -> int:
        n=len(lights); res=0
        for i in range(n):
            if lights[i]>0:
                # increment bcz indexes are inclusive
                lights[i]+=1 
            if i>0:
                lights[i]=max(0,lights[i-1]-1,lights[i])
        for i in range(n-2,-1,-1):
            lights[i]=max(0,lights[i+1]-1,lights[i])
        for i in range(1,n+1):
            if lights[i-1]<=0:
                res+=1
                if i<n:
                    lights[i]=1 #any +ve value
                if i<n-1:
                    lights[i+1]=1 #any +ve value
        return res
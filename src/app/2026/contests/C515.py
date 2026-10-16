class Solution:
    '''
    4025. Minimize the Maximum Waiting Time at Synchronized Traffic Lights

    You are given an integer period and an integer array lights, where lights[i] is the duration, in seconds, of the green phase of the ith traffic light.
    At time 0, every traffic light starts at the beginning of its green phase. Their cycles are synchronized: every traffic light starts a new cycle at the same time, and every cycle lasts exactly period seconds. Therefore, the red phase of the ith traffic light lasts for period - lights[i] seconds.
    You are also given an integer array arrivalTime, where arrivalTime[j] is the arrival time, in seconds, of the jth car.
    Each car must be assigned to exactly one traffic light. Multiple cars may be assigned to the same traffic light. Any number of cars may cross the same traffic light simultaneously while it is green. Cars do not block or delay one another.
    For a car j assigned to the ith traffic light, let r = arrivalTime[j] % period. If r < lights[i], its waiting time is 0. Otherwise, its waiting time is period - r.
    The penalty of an assignment is the maximum waiting time among all cars.
    Return an integer denoting the minimum possible penalty.

    Example 1:
    Input: period = 8, lights = [2,3], arrivalTime = [2,5,8,11]
    Output: 5
    Explanation:
    One optimal solution is:
    Assign arrivalTime[0] to the traffic light with lights[1] = 3. Here, r = 2 % 8 = 2. Since 2 < 3, the waiting time is 0.
    Assign arrivalTime[1] to the traffic light with lights[0] = 2. Here, r = 5 % 8 = 5. Since 5 >= 2, the waiting time is 8 - 5 = 3.
    Assign arrivalTime[2] to the traffic light with lights[0] = 2. Here, r = 8 % 8 = 0. Since 0 < 2, the waiting time is 0.
    Assign arrivalTime[3] to the traffic light with lights[0] = 2. Here, r = 11 % 8 = 3. Since 3 >= 2, the waiting time is 8 - 3 = 5.
    The penalty of this assignment is 5, which is the minimum possible. Other optimal assignments may exist.

    Constraints:
    2 <= period <= 10**9
    1 <= lights.length <= 10**4
    1 <= lights[i] <= period - 1
    1 <= arrivalTime.length <= 10**5
    1 <= arrivalTime[i] <= 10**9
    '''
    def minPenalty(self, period: int, lights: list[int], arrivalTime: list[int]) -> int:
        pass
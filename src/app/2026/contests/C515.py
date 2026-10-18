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
    '''
    4026. Maximum Gap Between Stations

    You are given two strings skill and station of lengths n and m, respectively.
    skill[i] represents the skill of worker i, and station[j] represents the skill supported by station j.
    You must assign every worker to a distinct station. Let ji be the index of the station assigned to worker i. A valid assignment must satisfy:

    station[ji] == skill[i] for every 0 <= i < n.
    The assigned station indices must be strictly increasing in worker order, meaning j0 < j1 < ... < jn - 1.
    The gap of an assignment is the maximum difference between the station indices assigned to two consecutive workers.
    In other words, it is max(ji - ji - 1) over all 1 <= i < n.
    If there is only one worker, the gap is 0.
    Return the maximum possible gap among all valid assignments. It is guaranteed that at least one valid assignment exists.

    Example 1:
    Input: skill = "aa", station = "aaaa"
    Output: 3
    Explanation:
    The two workers must be assigned to two different 'a' stations.
    Assigning them to stations [0, 3] gives a gap of 3.

    Constraints:
    skill.length == n
    station.length == m
    1 <= n <= m <= 10**5
    skill and station consist of lowercase English letters.
    It is guaranteed that a valid assignment exists for every worker.
    '''
    def maximumGap(self, skill: str, station: str) -> int:
        pass
    '''
    4027. Elevator Requests III

    You are given an integer n denoting the number of floors in a building, where the floors are numbered from 0 to n - 1.
    You are also given an integer start and a 2D integer array requests, where requests[i] = [arrivali, floori] indicates that a request for floori is made at time arrivali.
    At time 0, the elevator is at floor start.
    At each second, the elevator may move up by 1 floor, move down by 1 floor, or remain on its current floor.
    A request can be fulfilled only at or after its arrival time; it is fulfilled instantly when the elevator is on its requested floor at any time from its arrival time onward.
    Return the minimum time needed to fulfill all requests.

    Example 1:
    Input: n = 9, start = 0, requests = [[0,8],[6,5]]
    Output: 9
    Explanation:
    Move from floor 0 (start) to floor 5 (requests[1][1]) in 5 seconds, reaching at time 5. Since requests[1][0] = 6, wait until time 6 to fulfill it.
    Move from floor 5 to floor 8 (requests[0][1]) in 3 seconds, fulfilling it at time 9.
    Thus, all requests are fulfilled by time 9.

    Constraints:
    1 <= n <= 10**9
    1 <= requests.length <= 16
    requests[i] == [arrivali, floori]
    0 <= arrivali <= 10**9
    0 <= start, floori <= n - 1
    '''
    def elevatorRequests(self, n: int, start: int, requests: list[list[int]]) -> int:
        pass
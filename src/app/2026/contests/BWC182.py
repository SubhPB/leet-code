from typing import List
class Solution:
    '''
    3922. Minimum Flips to Make Binary String Coherent

    You are given a binary string s.
    A string is considered coherent if it does not contain "011" or "110" as subsequences.
    In one operation, you can flip any character in s ('0' to '1' or '1' to '0').
    Return an integer denoting the minimum number of operations required to make s coherent.
    Example 1:
    Input: s = "1010"
    Output: 1
    Explanation:
    Flip s[0] to get "0010", which contains no "011" or "110" subsequences.

    Constraints:
    1 <= s.length <= 10**5
    s[i] is either '0' or '1'.
    '''
    def minFlips(self, s: str) -> int:
        n=len(s); x=s.count('1')
        if n<3: return 0
        k=x-int(s[0])-int(s[-1])
        return min(
            x,n-x,
            max(0,x-1),
            k+[1,0][int(s[0])]+[1,0][int(s[-1])]
        )
    '''
    3923. Minimum Generations to Target Point

    You are given a 2D integer array points where points[i] = [xi, yi, zi] represents a point in 3D space, and an integer array target representing a target point.
    Define generation 0 as the initial list of points. For each integer k >= 1, form generation k as follows:
    Consider every pair of two distinct points a = [x1, y1, z1] and b = [x2, y2, z2] taken from all points produced in generations 0 through k - 1.
    For each such pair, compute c = [floor((x1 + x2) / 2), floor((y1 + y2) / 2), floor((z1 + z2) / 2)] and collect every such c into a generation k.
    All points in the generation k are produced simultaneously from points in generations 0 through​​​​​​​ k - 1.
    After generation k is formed, the points in the generation k are considered available for forming later generations.
    Return the smallest integer k such that the target appears in one of the generations 0 through k. If the target is already in the initial points, return 0. If it is impossible to obtain the target, return -1.

    Notes:
    floor denotes rounding down to the nearest integer.
    "Two distinct points" means the two chosen points must have different (x, y, z) coordinates. A point cannot be paired with itself, and pairing two points with identical coordinates is not possible.
    
    Example 1:
    Input: points = [[0,0,0],[6,6,6]], target = [3,3,3]
    Output: 1

    Constraints:
    1 <= points.length <= 20
    points[i] = [xi, yi, zi​​​​​​​]
    0 <= xi, yi, zi <= 6
    target.length == 3
    ​​​​​​​0 <= target[i] <= 6
    The initial set of points contains no duplicates.
    '''
    def minGenerations(self, points: List[List[int]], target: List[int]) -> int:
        encode = lambda x,y,z: x*100+y*10+z
        target=encode(*target)
        decode = lambda q:[q//100,(q%100)//10,(q%100)%10]
        λ = lambda q1,q2: [(a+b)//2 for (a,b) in zip(decode(q1),decode(q2))]
        src=set([encode(*point) for point in points]) 
        res=0; l=len(src)
        while src:
            l=len(src)
            lt=list(src)
            for i in range(l):
                for j in range(l):
                    q1,q2=lt[i],lt[j]
                    if i!=j:
                        src.add(encode(*λ(q1,q2)))
                    elif q1==target: return res
            if len(src)==l:
                break
            res+=1; l=len(src)
        return -1
    '''
    3924. Minimum Threshold Path With Limited Heavy Edges

    There is an undirected weighted graph with n nodes labeled from 0 to n - 1.
    The graph is represented by a 2D integer array edges, where each edge edges[i] = [ui, vi, w​​​​​​​i] indicates that there is an undirected edge between nodes ui and vi with weight w​​​​​​​i.
    You are also given integers source, target and k.
    A threshold value determines whether an edge is considered light or heavy:
    An edge is light if its weight is less than or equal to threshold.
    An edge is heavy if its weight is greater than threshold.
    A path from source to target is valid if it contains at most k heavy edges.
    Return the minimum integer threshold such that at least one valid path exists from source to target. If no such path exists, return -1.

    Example 1:​​​​​​​​​​​​​​
    ​​​
    Input: n = 6, edges = [[0,1,5],[1,2,3],[3,4,4],[4,5,1],[1,4,2]], source = 0, target = 3, k = 1
    Output: 4
    Explanation:
    The minimum threshold such that a path from node 0 to node 3 uses at most 1 heavy edge is 4.
    Light edges: [1, 2, 3], [3, 4, 4], [4, 5, 1], [1, 4, 2]
    Heavy edges: [0, 1, 5]
    A valid path is 0 → 1 → 4 → 3. It uses only 1 heavy edge ([0, 1, 5]), which satisfies the limit k = 1.
    Any smaller threshold would make it impossible to reach node 3 without exceeding 1 heavy edge.

    Constraints:
    1 <= n <= 10**3​​​​​​​
    0 <= edges.length <= 10**3​​​​​​​
    edges[i] = [ui, vi, wi]
    0 <= ui, vi​​​​​​​ <= n - 1
    1 <= wi​​​​​​​ <= 10**9
    0 <= source, target <= n - 1
    0 <= k <= edges.length
    '''
    def minimumThreshold(self, n: int, edges: List[List[int]], source: int, target: int, k: int) -> int:
        pass
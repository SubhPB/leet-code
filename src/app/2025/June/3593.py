'''
3593. Minimum Increments to Equalize Leaf Paths
    You are given an integer n and an undirected tree rooted at node 0 with n nodes numbered from 0 to n - 1. This is represented by a 2D array edges of length n - 1, where edges[i] = [ui, vi] indicates an edge from node ui to vi .

    Each node i has an associated cost given by cost[i], representing the cost to traverse that node.

    The score of a path is defined as the sum of the costs of all nodes along the path.

    Your goal is to make the scores of all root-to-leaf paths equal by increasing the cost of any number of nodes by any non-negative amount.

    Return the minimum number of nodes whose cost must be increased to make all root-to-leaf path scores equal.


    Example 1:

    Input: n = 3, edges = [[0,1],[0,2]], cost = [2,1,3]

    Output: 1

    Explanation:

    There are two root-to-leaf paths:

    Path 0 → 1 has a score of 2 + 1 = 3.
    Path 0 → 2 has a score of 2 + 3 = 5.
    To make all root-to-leaf path scores equal to 5, increase the cost of node 1 by 2.
    Only one node is increased, so the output is 1.

    Example 2:

    Input: n = 3, edges = [[0,1],[1,2]], cost = [5,1,4]

    Output: 0

    Explanation:

    There is only one root-to-leaf path:

    Path 0 → 1 → 2 has a score of 5 + 1 + 4 = 10.

    Since only one root-to-leaf path exists, all path costs are trivially equal, and the output is 0.

    Example 3:

    Input: n = 5, edges = [[0,4],[0,1],[1,2],[1,3]], cost = [3,4,1,1,7]

    Output: 1

    Explanation:

    There are three root-to-leaf paths:

    Path 0 → 4 has a score of 3 + 7 = 10.
    Path 0 → 1 → 2 has a score of 3 + 4 + 1 = 8.
    Path 0 → 1 → 3 has a score of 3 + 4 + 1 = 8.
    To make all root-to-leaf path scores equal to 10, increase the cost of node 1 by 2. Thus, the output is 1.

    Constraints:

    2 <= n <= 10^5
    edges.length == n - 1
    edges[i] == [ui, vi]
    0 <= ui, vi < n
    cost.length == n
    1 <= cost[i] <= 10^9
'''

class Solution:
        def minIncrease(self, n: int, edges: list[list[int]], cost: list[int]) -> int:
            '''
            KEY OBSERVATIONS: At any node 'u'
                [1] All root->u prefix cost is same for all descendent leaf
                [2] To equalize everything beneath 'u' each child subtree must independently end up with same total path-sum 'suffix'.
            '''
            graph = [[] for _ in range(n)]
            for nodes in edges:
                for i in range(2): graph[nodes[i]].append(nodes[(i+1)%2])

            '''
            dfs(node, parent) -> (
                [i] {Max-Score} Max score of path that exist in subtree where node is parent,
                [ii] {ops} All the child of node now has same score and achieved after doing #'ops' operations
            )
            '''
            def dfs(node:int,parent:int)->tuple[int, int]:
                #If leaf, only subtree has exactly path to itself whose suffix is simply its own cost
                #Already balanced! needs 0 ops
                if not graph[node]:
                    return (cost[node], 0) #(suffix, ops)
                max_child_suffix, total_ops = 0, 0
                #What's largest suffix among children and max ops?
                subtree_suffix = [0 for _ in range(n)]
                for child in graph[node]:
                    if child != parent:
                        (suffix, sub_ops) = dfs(child, node)
                        subtree_suffix[child] = suffix
                        max_child_suffix = max(
                            max_child_suffix, subtree_suffix[child]
                        )
                        total_ops += sub_ops
                        
                #Now we've figured out max_suffix and max_ops any child taking!
                for child in graph[node]:
                    if child != parent and subtree_suffix[child] < max_child_suffix:
                        total_ops += 1
                            
                return (cost[node]+max_child_suffix, total_ops)
            
            return dfs(0,-1)[1]
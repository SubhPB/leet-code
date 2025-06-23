/**
 * 3593. Minimum Increments to Equalize Leaf Paths
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
 */

class Solve3593{
    constructor(public n:number, public edges:number[][], public cost:number[]){
        this.n=n; this.edges=edges; this.cost=cost;
    };
    solution(n=this.n, edges=this.edges, cost=this.cost){
        const graph:number[][] =  Array.from({length:n},()=>[]);
        for(const edge of edges){
            for(let i=0; i<2; i+=1) graph[edge[i]].push(edge[(i+1)%2])
        };
        const dfs = (node:number, parent:number):[number,number] => {
            let pathCost = cost[node], ops = 0;
            const isLeaf = !graph[node].length;
            if (!isLeaf){
                const subPathCosts:{[k:string]:number} = {};
                let maxSubPathCost = 0;
                for(let child of graph[node]){
                    if (child!==parent){
                        const [subPathCost, subOps] = dfs(child, node);
                        maxSubPathCost = Math.max(
                            maxSubPathCost, subPathCost
                        );
                        subPathCosts[child] = subPathCost;
                        ops += subOps;
                    }
                };
                //Till now we've info about what is the max subPath and subops of each subPath
                //Let's now make all the subPaths equal eachother
                for(let child of graph[node]){
                    if (child!==parent && subPathCosts[child]<maxSubPathCost){
                        ops += 1; //Operation to increment its cost
                    }
                };
                pathCost += maxSubPathCost;
            };
            //pathCost:All paths under 'node' are now equal so what is pathCost from node to any leaf 
            //ops: How many ops it took to make all descendant subpaths equalivalent
            return [pathCost,ops]
        };
        const [_maxScore, minIncs] = dfs(0, -1);
        return minIncs;
    }
}
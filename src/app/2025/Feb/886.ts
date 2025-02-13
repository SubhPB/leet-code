/**
 * 886. Possible Bipartition

We want to split a group of n people (labeled from 1 to n) into two groups of any size. Each person may dislike some other people, and they should not go into the same group.

Given the integer n and the array dislikes where dislikes[i] = [ai, bi] indicates that the person labeled ai does not like the person labeled bi, return true if it is possible to split everyone into two groups in this way.

Example 1:

Input: n = 4, dislikes = [[1,2],[1,3],[2,4]]
Output: true
Explanation: The first group has [1,4], and the second group has [2,3].
Example 2:

Input: n = 3, dislikes = [[1,2],[1,3],[2,3]]
Output: false
Explanation: We need at least 3 groups to divide them. We cannot put them in two groups.

npx ts-node ./src/app/2025/Feb/886.ts
 */

class Solve886{
    constructor(public n:number,public dislikes:number[][]){
        this.dislikes=dislikes
    };
    /**
     * This problem is direct application to check whether graph is bipartite or not!
     * [Disjoint] One node exist only in one group.
     * [Independent] Adjacent nodes can't be in same group
     */
    solution1(){
        const n = this.n, graph:{[k:string]:number[]} = {};
        this.dislikes.forEach(([ai,bi])=>{
            if (!(ai in graph)) graph[ai] = [];
            graph[ai].push(bi);
        });

        /**Note:A graph does not guarantee whether it will be connected or disconnected.
         * So, If it is connected then any node as an starting node can give us answer.
         * But, If is disconnected then we would need to check for every node as starting node
        */
        const state = Array.from({length:n+1}, ()=>0); /**[0] means unvisited, [-1] means node in group1 [1] means node is in group2  */

        const bfs = (initialNode:number) => {
                const queue = [initialNode];
                state[initialNode] = -1;/**initialNode is in group 1 by default */
                while(queue.length){
                    const node = queue.shift()!, neighbors = node in graph ? graph[node] : [];
                    for(let neighbor of neighbors){
                        if (state[node]===state[neighbor]) return false;
                        if (state[neighbor]===0){
                            state[neighbor]=-state[node];
                            queue.push(neighbor)
                        }
                    }
                };
                return true
        };

        for(let i=1; i<=n; i++){
            if (state[i]===0&&!bfs(i)) return false
        };
       return true
    }
};

(
    ()=>{
        const ARGS:[number,number[][]][] = [
            [4, [[1,2],[1,3],[2,4]]],
            [3, [[1,2],[1,3],[2,3]]]
        ];
        ARGS.forEach(([n,dislikes])=>{
            console.log(`Leetcode-886 n=${n} dislikes=[${dislikes.join(" ")}] solution -> ${new Solve886(n,dislikes).solution1()}`)
        })
    }
)()
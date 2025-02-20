/**
 * 802. Find Eventual Safe States (medium)
There is a directed graph of n nodes with each node labeled from 0 to n - 1.
 The graph is represented by a 0-indexed 2D integer array graph where graph[i] is an integer array of nodes adjacent to node i,
  meaning there is an edge from node i to each node in graph[i].

A node is a terminal node if there are no outgoing edges.
 A node is a safe node if every possible path starting from that node leads to a terminal node (or another safe node).

Return an array containing all the safe nodes of the graph. The answer should be sorted in ascending order.

Example 1:
Input: graph = [[1,2],[2,3],[5],[0],[5],[],[]]
Output: [2,4,5,6]
Explanation: The given graph is shown above.
Nodes 5 and 6 are terminal nodes as there are no outgoing edges from either of them.
Every path starting at nodes 2, 4, 5, and 6 all lead to either node 5 or 6.
Example 2:

Input: graph = [[1,2,3,4],[1,2],[3,4],[0,4],[]]
Output: [4]
Explanation:
Only node 4 is a terminal node, and every path starting at node 4 leads to node 4.

npx ts-node ./src/app/2025/Feb/802.ts
 */

class Solve802{
    constructor(public G:number[][]){
        this.G=G
    };
    solution1(graph=this.G){
        const n = graph.length;
        const checkList:(-1|0|1)[] = Array.from({length:n},
            (_,i)=>graph[i].length ? 0 : 1 //-1 means not a safe node, 0 means not yet know , 1 is safe node
        );
        const safeNodes:number[] = []
        for(let i=0; i<n; i++){
            if (checkList[i]===0){
                const traversed = Array.from({length:n}, ()=>false);
                let queue = [i];
                while(queue.length){
                    const node = queue.shift()!;

                    if (checkList[node]===-1||traversed[node]){
                        //if a cycle detected, or child node found to be unsafe node, then this node and child node is indeed a unsafe node
                        checkList[i]=-1;
                        queue = []
                    } else if (checkList[node]===0){
                        traversed[node] = true;
                        for(let child of graph[node]){
                            if (checkList[child]===1) continue;
                            queue.push(child)
                        }
                    };
                };
                //If above loop doesn't assign checklist[i] to be unsafe and it still untraversed then it should be safe node
                if (checkList[i]===0) checkList[i]=1;
            }
            if (checkList[i]===1) safeNodes.push(i);
        };
        return safeNodes
    }
};

(
    ()=>{
        const ARGS = [
            [[1,2],[2,3],[5],[0],[5],[],[]],
            [[1,2,3,4],[1,2],[3,4],[0,4],[]]
        ];
        ARGS.forEach(graph => console.log(`[Leetcode-802] SafeNodes = ${new Solve802(graph).solution1()}`))
    }
)()
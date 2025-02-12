/**
 * 785. Is Graph Bipartite?

There is an undirected graph with n nodes, where each node is numbered between 0 and n - 1.
You are given a 2D array graph, where graph[u] is an array of nodes that node u is adjacent to.
More formally, for each v in graph[u], there is an undirected edge between node u and node v.
The graph has the following properties:

There are no self-edges (graph[u] does not contain u).
There are no parallel edges (graph[u] does not contain duplicate values).
If v is in graph[u], then u is in graph[v] (the graph is undirected).
The graph may not be connected, meaning there may be two nodes u and v such that there is no path between them.
A graph is bipartite if the nodes can be partitioned into two independent sets A and B such that every edge in the graph connects a node in set A and a node in set B.

Return true if and only if it is bipartite.

Example 1:

Input: graph = [[1,2,3],[0,2],[0,1,3],[0,2]]
Output: false
Explanation: There is no way to partition the nodes into two independent sets such that every edge connects a node in one and a node in the other.
Example 2:

Input: graph = [[1,3],[0,2],[1,3],[0,2]]
Output: true
Explanation: We can partition the nodes into two sets: {0, 2} and {1, 3}.
 */

/**
 * A bipartite has simple 2 charteristics:-
 * 1) [Disjoint] Non overlapping, an element occurs in exactly one group/set.
 * 2) [Independent] No edge b/w elements of same group/set.
 * 
 * npx ts-node ./src/app/2025/Feb/785.ts
 */

class Solve785{
    constructor(public Graph:number[][]){
        this.Graph=Graph
    };
    solution1(graph=this.Graph){
        const n = graph.length;
        /**
         * Graph Theory tells that every graph is bipartite graph unless it has odd cycle length.
         * If we are able to detect if a graph contains a cycle having odd length, we have simply found the answer.
         * How? -> DFS + state of 2 groups. 
         */

        // index refers to node and its value if 0 means unvisited, if -1 means group 1, if 1 means group 2.
        const state: (0|1|-1)[] = Array.from({length:n}, ()=>0);
        const queue:number[] = [];
        if (n){
            queue.push(0);
            state[0] = 1; //first node will be in group 1 by default
        };
        while(queue.length){
            const node = queue.shift()!;
            for(let neighbor of graph[node]){
                if (state[neighbor]===state[node]) return false; //Means 2 nodes adjacent to each other are lying in same group/set
                if(state[neighbor]===0) queue.push(neighbor); //If first time to visit, push in queue
                state[neighbor] = -state[node] as -1|1;
            }
        };
        return !state.includes(0); // if graph was not connected 
    }
};

(
    ()=>{
        const ARGS: ([number[][], boolean])[] = [
            [[[1,2,3],[0,2],[0,1,3],[0,2]], false],
            [[[1,3],[0,2],[1,3],[0,2]], true]
        ];
        ARGS.forEach(([graph, expected],i) =>{
            console.log(`Graph-${i} expected=${expected} and answer found is ${new Solve785(graph).solution1()}`)
        })
    }
)()
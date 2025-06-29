/**
 * '''
3553. Minimum Weighted Subgraph With the Required Paths II

    You are given an undirected weighted tree with n nodes, numbered from 0 to n - 1. It is represented by a 2D integer array edges of length n - 1, where edges[i] = [ui, vi, wi] indicates that there is an edge between nodes ui and vi with weight wi.​

    Additionally, you are given a 2D integer array queries, where queries[j] = [src1j, src2j, destj].

    Return an array answer of length equal to queries.length, where answer[j] is the minimum total weight of a subtree such that it is possible to reach destj from both src1j and src2j using edges in this subtree.

    A subtree here is any connected subset of nodes and edges of the original tree forming a valid tree.

    

    Example 1:

    Input: edges = [[0,1,2],[1,2,3],[1,3,5],[1,4,4],[2,5,6]], queries = [[2,3,4],[0,2,5]]

    Output: [12,11]

    Explanation:

    The blue edges represent one of the subtrees that yield the optimal answer.



    answer[0]: The total weight of the selected subtree that ensures a path from src1 = 2 and src2 = 3 to dest = 4 is 3 + 5 + 4 = 12.

    answer[1]: The total weight of the selected subtree that ensures a path from src1 = 0 and src2 = 2 to dest = 5 is 2 + 3 + 6 = 11.

    Example 2:

    Input: edges = [[1,0,8],[0,2,7]], queries = [[0,1,2]]

    Output: [15]

    Explanation:



    answer[0]: The total weight of the selected subtree that ensures a path from src1 = 0 and src2 = 1 to dest = 2 is 8 + 7 = 15.
    

    Constraints:

    3 <= n <= 105
    edges.length == n - 1
    edges[i].length == 3
    0 <= ui, vi < n
    1 <= wi <= 104
    1 <= queries.length <= 105
    queries[j].length == 3
    0 <= src1j, src2j, destj < n
    src1j, src2j, and destj are pairwise distinct.
    The input is generated such that edges represents a valid tree.

    npx ts-node ./src/app/2025/May/3553.ts

 */

class Solve3553{
    constructor(public edges:number[][], public queries:number[][]){
        this.edges=edges; this.queries=queries
    };
    solution(edges=this.edges, queries=this.queries){
        const m = edges.length, n = m+1, q = queries.length;
        const graph:number[][][] = Array.from({length:n}, ()=>[]);

        for(let [u,v, w] of edges){
            graph[u].push([v,w]);
            graph[v].push([u,w]);
        };

        const liftLimit = (n-1).toString(2).length;

        //depth[root] = 0
        const depth = Array.from({length:n}, ()=> 0);
        const rootDist = Array.from({length:n}, ()=>0);
        const ancestor = Array.from(
            {length:liftLimit}, () => Array.from(
                {length:n},() => -1
            )
        );

        const dfs = (node:number, parent:number) => {
            ancestor[0][node] = parent;
            const neighbors = node in graph ? graph[node] : []
            for(let [v,w] of neighbors){
                if (parent!==v){
                    depth[v] = depth[node] + 1;
                    rootDist[v] = rootDist[node] + w;
                    dfs(v, node)
                }
            }
        };
        dfs(0,-1);

        //computing ancestor
        for(let pow=1; pow<liftLimit; pow+=1){
            for(let node=0; node<n; node+=1){
                const parent = ancestor[pow-1][node]
                if (ancestor[pow-1][parent]!==-1) ancestor[pow][node] = ancestor[pow-1][parent]
            }
        };

        const lowestCommonAncestor = (u:number,v:number) => {
            // 'u' supposed to be deeper
            if (depth[u]<depth[v]){
                [u,v] = [v,u]
            };
            const diff = depth[u]-depth[v];
            for(let k=0; k<liftLimit && diff>0; k++){
                if ((diff>>k)&1){
                    u = ancestor[k][u]
                };
                if (u===v) return u
            };
            //Till here both nodes should be at same depth
            while (ancestor[0][u] !== ancestor[0][v]){
                u = ancestor[0][u];
                v = ancestor[0][v]
            }
            return ancestor[0][u]
        };

        const findDist = (u:number,v:number) => {
            const lca = lowestCommonAncestor(u,v);
            return rootDist[u]+rootDist[v]-2*rootDist[lca]
        };

        const res = Array.from({length:q}, ()=>-1);
        for(let i=0; i<q; i++){
            const [src1, src2, dest] = queries[i];
            const dist = findDist(src1,src2)+findDist(src1,dest)+findDist(src2,dest);
            res[i] = Math.floor(dist/2)
        }
        return res;
    }
};

(
    ()=>{
        const Testcases:[number[][], number[][]][] = [
            [[[0,1,2],[1,2,3],[1,3,5],[1,4,4],[2,5,6]], [[2,3,4],[0,2,5]]],
            [[[1,0,8],[0,2,7]], [[0,1,2]]]
        ];

        for(let [edges, queries] of Testcases){
            const ans = new Solve3553(edges, queries).solution()
            console.log(`Edges=[${edges.join(',')}] Queries=[${queries.join(',')}] ans=[${ans.join(',')}]`)
        }
    }
)()
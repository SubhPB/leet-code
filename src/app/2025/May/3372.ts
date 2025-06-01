/**
 * 3372. Maximize the Number of Target Nodes After Connecting Trees I
    There exist two undirected trees with n and m nodes, with distinct labels in ranges [0, n - 1] and [0, m - 1], respectively.

    You are given two 2D integer arrays edges1 and edges2 of lengths n - 1 and m - 1, respectively, where edges1[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the first tree and edges2[i] = [ui, vi] indicates that there is an edge between nodes ui and vi in the second tree. You are also given an integer k.

    Node u is target to node v if the number of edges on the path from u to v is less than or equal to k. Note that a node is always target to itself.

    Return an array of n integers answer, where answer[i] is the maximum possible number of nodes target to node i of the first tree if you have to connect one node from the first tree to another node in the second tree.

    Note that queries are independent from each other. That is, for every query you will remove the added edge before proceeding to the next query.

    

    Example 1:

    Input: edges1 = [[0,1],[0,2],[2,3],[2,4]], edges2 = [[0,1],[0,2],[0,3],[2,7],[1,4],[4,5],[4,6]], k = 2

    Output: [9,7,9,8,8]

    Explanation:

    For i = 0, connect node 0 from the first tree to node 0 from the second tree.
    For i = 1, connect node 1 from the first tree to node 0 from the second tree.
    For i = 2, connect node 2 from the first tree to node 4 from the second tree.
    For i = 3, connect node 3 from the first tree to node 4 from the second tree.
    For i = 4, connect node 4 from the first tree to node 4 from the second tree.

    Example 2:

    Input: edges1 = [[0,1],[0,2],[0,3],[0,4]], edges2 = [[0,1],[1,2],[2,3]], k = 1

    Output: [6,3,3,3,3]

    Explanation:

    For every i, connect node i of the first tree with any node of the second tree.


    

    Constraints:

    2 <= n, m <= 1000
    edges1.length == n - 1
    edges2.length == m - 1
    edges1[i].length == edges2[i].length == 2
    edges1[i] = [ai, bi]
    0 <= ai, bi < n
    edges2[i] = [ui, vi]
    0 <= ui, vi < m
    The input is generated such that edges1 and edges2 represent valid trees.
    0 <= k <= 1000

    npx ts-node ./src/app/2025/May/3372.ts
 */

class Solve3372{
    constructor(public edges1:number[][], public edges2:number[][], public k:number){
        this.edges1=edges1; this.edges2=edges2; this.k=k;
    };

    private findTargetNodes(node:number, depth:number, graph:number[][]){
        const queue = [[node, -1, 0]];
        let targetNodes = 0, head = 0;
        while (head<queue.length){
            const [currNode, parent, lvl] = queue[head];
            targetNodes+=1;
            head+=1;
            if (lvl>=depth) continue;
    
            for(let v of graph[currNode]){
                if (v===parent) continue;
                queue.push([v, currNode, lvl+1])
            }
        };
        return targetNodes;
    };
    solution(edges1=this.edges1, edges2=this.edges2, k=this.k){
        const [n,m] = [edges1, edges2].map(E => E.length+1);
        const res:number[] = Array(n).fill(1);
    
        if (k>0){
            const graphs = [n,m].map(size => Array.from(
                {length: size}, () => [] as number[]
            )) ;
        
            for(let tree=0; tree<2; tree+=1){
                for(let [u,v] of [edges1, edges2][tree]){
                    graphs[tree][u].push(v);
                    graphs[tree][v].push(u)
                }
            };
        
            const [G1, G2] :number[][][] = graphs;
            
            //In tree2, let's find a node who have most target nodes at k-1
            let mostNodesInTree2 = 0;
            for(let node=0; node<m; node+=1) mostNodesInTree2 = Math.max(
                mostNodesInTree2, this.findTargetNodes(node, k-1, G2)
            );
    
            for(let node=0; node<n; node+=1){
                res[node] = this.findTargetNodes(
                    node, k, G1
                ) + mostNodesInTree2
            }
        };
        return res
    }
};

(
    ()=>{
        const TestCases: [number[][], number[][], number][] = [
            [    
                [[0,1],[0,2],[2,3],[2,4]],
                [[0,1],[0,2],[0,3],[2,7],[1,4],[4,5],[4,6]],
                2,
            ],
            [
                [[0,1],[0,2],[0,3],[0,4]],
                [[0,1],[1,2],[2,3]],
                1,
            ],
            [
                [[2,1],[7,3],[0,4],[7,5],[2,6],[0,2],[0,7]],
                [[3,0],[1,2],[5,1],[6,3],[9,4],[5,6],[7,5],[9,7],[8,9]],
                7,
            ]
        ];

        for(const [e1, e2, k] of TestCases){
            const sol = new Solve3372(e1,e2,k);
            console.log(`N=${e1.length+1} M=${e2.length+1} k=${k} ans=${sol.solution()}`)
        }
    }
)()
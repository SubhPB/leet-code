/**
 * 847. Shortest Path Visiting All Nodes

You have an undirected, connected graph of n nodes labeled from 0 to n - 1. You are given an array graph where graph[i] is a list of all the nodes connected with node i by an edge.

Return the length of the shortest path that visits every node. You may start and stop at any node, you may revisit nodes multiple times, and you may reuse edges.

Example 1:


Input: graph = [[1,2,3],[0],[0],[0]]
Output: 4
Explanation: One possible path is [1,0,2,0,3]
Example 2:


Input: graph = [[1],[0,2,4],[1,3,4],[2],[1,2]]
Output: 4
Explanation: One possible path is [0,1,4,2,3]

npx ts-node ./src/app/2025/Jan/847.ts
 */

class Solve847{
    public graph:{[k:number]:number[]}; private nodes:number;
    constructor(G:number[][]){
        this.graph = this.constructGraph(G); this.nodes = Object.keys(this.graph).length;
    };
    constructGraph(G:number[][]){
        const graph: {[k:number]:number[]} = {};
        for(let i=0; i<G.length; i++){
            if(!(i in graph)) graph[i] = [];
            graph[i].push(...G[i])
        };
        return graph
    };
    solution1(){
        const matrix:number[][] = [];
        for(let r=0; r<this.nodes; r++){
            matrix.push(Array.from({length:this.nodes}, (_,c) => r===c ? 0:Infinity))
            for(let c=0; c<this.nodes; c++){
                //what s the shortest distance from r --> c
                let selected:null|number = r, traversedNodes: {[k:string]:any} = {}, unTraversedNodes:{[k:string]:any} = {selected}, nodeFound = false
                while(selected!==null){
                    for(let neighbor of selected in this.graph ? this.graph[selected] : []){
                        if (
                            matrix[r][selected]+1 < matrix[r][neighbor]
                        ) matrix[r][neighbor] = matrix[r][selected] + 1;
                        if (!(neighbor in traversedNodes) && !(neighbor in unTraversedNodes)) unTraversedNodes[neighbor] = null;
                        if ((neighbor)===c){
                            nodeFound = true; break
                        }
                    };
                    if (nodeFound) break;
                    traversedNodes[selected] = null; delete unTraversedNodes[selected];
                    const nextSelect:number = Number(Object.keys(unTraversedNodes).sort((a,b) => matrix[r][parseInt(a)]-matrix[r][parseInt(b)])[0]);
                    selected = Number.isInteger(nextSelect) ? nextSelect : null;
                };

            }
        };

        let minLength = Infinity, minPath:number[] = []
        //since now we have shortest dist from every node to any other node.
        let fn = (node:number, path:number[], dist:number) => {
            if (dist>minLength) return;
            if (path.length===matrix.length){
                if (dist<minLength){
                    minLength = dist;
                    minPath = [...path]
                }
            } else{
                const unTraversedNodes = Array.from({length:matrix.length}, (_,i) => i).filter(i=>!path.includes(i));
                for(let unTraversedNode of unTraversedNodes){
                    fn(unTraversedNode, [...path, unTraversedNode], dist+matrix[node][unTraversedNode])
                }
            }
        };
        for(let i=0; i<matrix.length; i++) fn(i, [i], 0);
        
        return minPath
    }
};

(
    () => {
        const Graphs = [
            [[1,2,3],[0],[0],[0]],
            [[1],[0,2,4],[1,3,4],[2],[1,2]]
        ];
        Graphs.forEach(graph => console.log(`Graph=${JSON.stringify(graph)} solution ->${new Solve847(graph).solution1()}`))   
    }
)()
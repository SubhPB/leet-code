/**Traveling Salesperson problem
 * Having a graph, where distance from A->B could be equal or different from the B->A.
 * The problem requires us to select a node and make a path that covers all the nodes
 * and return back to starting node forming a cycle with least cost
 * 
 * npx ts-node ./src/app/2025/Jan/tsp.ts
 */

class TravelingSalesperson{
    constructor(public graph:number[][]){
        this.graph = graph
    };
    solution1(){
        const [m,n] = [this.graph.length, this.graph[0].length];
        const dfs: [number/**currNode*/, string/**path*/, number/**cost*/][] = [];
        dfs.push([0,'0',0]) //starting node
        let minCost = Infinity;
        while(dfs.length){
            const [currNode, path, cost] = dfs.pop()!;
            if (cost>minCost) continue;
            const [startNode, lastNode] = [path[0], path[path.length-1]].map(Number);
            if (path.length===Math.max(m,n)){
                const lastToStartCost = lastNode<m&&startNode<n ? this.graph[lastNode][startNode] : Infinity;
                if (cost+lastToStartCost < minCost) minCost = cost+lastToStartCost
            } else {
                for(let i=0; i<Math.max(m,n); i++){
                    if (path.includes(String(i))) continue;
                    const nextCost = currNode<m&&i<n ? this.graph[currNode][i] : Infinity 
                    dfs.push([i, path+String(i), cost+nextCost])
                }
            }
        };
        return minCost
    }
};

(
    ()=>{
        const ARGS:(number[][])[] = [
            [
                [0,10,15,20],
                [5,0,9,10],
                [6,13,0,12],
                [8,8,9,0]
            ]
        ];
        ARGS.forEach(
            (matrix, i)=> console.log(`Graph-${i=1} Traveling Salesperson solution = ${new TravelingSalesperson(matrix).solution1()}`)
        )
    }
)()
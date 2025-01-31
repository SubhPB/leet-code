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
    };
    solution2(){
        const n = this.graph.length;
        // #-rows = 2**n (each row represents which nodes are visited e.g 0110 -> 1st and 2nd nodes are visited)
        // #-cols = n (col value represent which node we are at e.g c=2 means we are at 2nd node)
        // [r,c] each slot represent minimum cost to reach city c, having already visited nodes represented by mask-<r> 
        const dp:number[][] = Array.from({length:1<<n}, ()=>Array(n).fill(Infinity));
        dp[1][0] = 0; // mask = 0001 and currNode = 0, what's the min dist to reach node-0 when visited nodes are 0001
        
        for(let mask=0; mask<(1<<n); mask++){
            for(let u=0; u<n; u++){
                // if u-th node is already visited in the mask
                if (mask&(1<<u)){
                    for(let v=0; v<n; v++){
                        //try to move to another city...
                        //if `v` is not yet visited in the mask
                        if (!(mask&(1<<v))){
                            const newBitMask = mask | (1<<v);
                            dp[newBitMask][v] = Math.min(
                                dp[newBitMask][v],
                                dp[mask][u]+this.graph[u][v]
                            )
                        }
                    }
                }
            }
        };
        let minCost = Infinity;
        for(let u=1; u<n; u++){
            minCost = Math.min(minCost, dp[(1<<n)-1][u]+this.graph[u][0]) 
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
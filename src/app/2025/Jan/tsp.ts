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
        
        //If we need to track back the path, parent[][] would help us!
        const parent:number[][] = Array.from({length:1<<n}, ()=>Array(n).fill(-1));

        
        //If starting can be any node
        for(let i=0; i<n; i++) dp[1<<i][i] = 0;

        for(let mask=1; mask<(1<<n); mask++){
            /* We need to travel from a visited node to a un-visited node. e.g r=0110 -> node-1, node-2 are visited
            * So `u` must be visited and `v` should be unvisited node
            */
            for(let u=0; u<n; u++){
                if (mask&(1<<u)){//Ensures u-th node is visited in the mask
                    for(let v=0; v<n; v++){//need to visit a new unvisited node from u
                        if (!(mask&(1<<v))){//Ensures `v` is not yet visited in the mask
                            const newBitMask = mask | (1<<v), newCost = dp[mask][u]+this.graph[u][v];
                            if (newCost<dp[newBitMask][v]){
                                dp[newBitMask][v] = newCost;
                                parent[newBitMask][v] = u; //Track the previous city
                            };
                        }
                    }
                }
            }
        };
        let minCost = Infinity, finalMask = (1<<n)-1;
        for(let u=0; u<n; u++){
            let prevNode = u, path = [], mask = finalMask;
            while(prevNode!==-1){ //job of `while` is to track back the path in order to get the startingNode of this path
                path.push(prevNode);
                let currNode = prevNode
                prevNode = parent[mask][currNode];
                mask ^= (1<<currNode);
            };
            if (path.length){
                const cost = dp[finalMask][u] + this.graph[u][path[0]]; //So now also inc. cost to go back to starting node
                if (cost<minCost) minCost = cost;
            }
        };
        return {
            minCost,
            lastMask: dp[(1<<n)-1],
        }
    };
    solution3(){
        /**This solution may not be most efficient, but focuses to solve this problem using `Branch And Bound` approach */
        function utils(matrix: number[][]) {
            return {
                getCol: (c: number) => {
                    return matrix.map(row => row[c]); // Get column c
                },
                reduceMatrix: () => {
                    const m = matrix.length, n = matrix[0].length;
                    const reducedMatrix = matrix.map(row => [...row]); // Create a copy
                    let reduceCost = 0;
        
                    // Row Reduction
                    for (let r = 0; r < m; r++) {
                        const rowMin = Math.min(...reducedMatrix[r]); // Use reducedMatrix, not matrix
                        reduceCost += rowMin;
                        if (rowMin !== 0) {
                            reducedMatrix[r] = reducedMatrix[r].map(rv => rv - rowMin);
                        }
                    }
        
                    // Column Reduction
                    for (let c = 0; c < n; c++) {
                        const col = reducedMatrix.map(row => row[c]); // Corrected column retrieval
                        const colMin = Math.min(...col);
                        reduceCost += colMin;
                        if (colMin !== 0) {
                            for (let r = 0; r < m; r++) {
                                reducedMatrix[r][c] -= colMin;
                            }
                        }
                    }
        
                    return { reduceCost, reducedMatrix };
                }
            };
        };
        const m = this.graph.length, n = this.graph[0].length;
        for(let r=0; r<m; r++) this.graph[r][r] = Infinity;

        // const queue: ({parentReducedMatrix:number[][], parentReducedCost:number[], path:number[]})[] = [];
        /**suppose 0 is our starting node */
        let {reducedMatrix, reduceCost:lowerBound} = utils(this.graph).reduceMatrix(), path = [0], upperBound = Infinity;
        while(path.length!==m){
            const traversed: {currUpperBound:number,currReducedMatrix:number[][], currPath:number[]}[] = []
            for(let childNode=0; childNode<m; childNode++){
                if (path.includes(childNode)) continue;
                const parentNode = path[path.length-1];
                //updating reducedMatrix
                const currMatrix = reducedMatrix.map((r, ri) => r.map((c,ci)=> {
                    if (ri===parentNode||ci===childNode) return Infinity;
                    else return c
                }));
                currMatrix[childNode][parentNode] = Infinity; 

                const {reduceCost:currReduceCost, reducedMatrix:currReducedMatrix} = utils(currMatrix).reduceMatrix();
                const currUpperBound = this.graph[parentNode][childNode] + lowerBound + currReduceCost;
                if (currUpperBound<upperBound) traversed.push({currReducedMatrix, currUpperBound, currPath:[...path,childNode]})
            };
            if (traversed.length){
                let minTraverse: typeof traversed[number] = traversed.pop()!;
                while(traversed.length){
                    const currTraverse = traversed.pop()!;
                    if (currTraverse.currUpperBound<minTraverse.currUpperBound) minTraverse = currTraverse
                };
                //updating the global state
                reducedMatrix = minTraverse.currReducedMatrix, upperBound = minTraverse.currUpperBound, path = minTraverse.currPath;
            } else break;
        };
        return upperBound
    };
};

(
    ()=>{
        const ARGS:(number[][])[] = [
            [
                [0,10,15,20],
                [5, 0, 9,10],
                [6,13, 0,12],
                [8, 8, 9, 0]
            ],
            [
                [0, 20, 30, 10, 11],
                [15, 0, 16, 4, 2],
                [3, 5, 0, 2, 4],
                [19, 6, 18, 0, 3],
                [16, 4, 7, 16, 0]
            ]
        ];
        ARGS.forEach(
            (matrix, i)=> console.log(`Graph-${i=1} Traveling Salesperson solution = %O`, new TravelingSalesperson(matrix).solution3())
        )
    }
)()
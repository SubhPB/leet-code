/**
 * Input 1: a maze represented by a 2D array

0 0 1 0 0
0 0 0 0 0
0 0 0 1 0
1 1 0 1 1
0 0 0 0 0

Input 2: start coordinate (rowStart, colStart) = (0, 4)
Input 3: destination coordinate (rowDest, colDest) = (4, 4)

Output: 12

Explanation: One shortest way is : left -> down -> left -> down -> right -> down -> right.
             The total distance is 1 + 1 + 3 + 1 + 2 + 2 + 2 = 12.

Input 1: a maze represented by a 2D array

0 0 1 0 0
0 0 0 0 0
0 0 0 1 0
1 1 0 1 1
0 0 0 0 0

Input 2: start coordinate (rowStart, colStart) = (0, 4)
Input 3: destination coordinate (rowDest, colDest) = (3, 2)

Output: -1

Explanation: There is no way for the ball to stop at the destination.

 CMD npx ts-node ./src/app/2025/Jan/505.ts
 */

class Solve505{
    constructor(public maze:number[][], public startCoordinate:[number, number], public destCoordinate:[number, number]){
        this.maze= maze; this.startCoordinate=startCoordinate, this.destCoordinate=destCoordinate;
    };
    getNeighbors([r,c]:[number, number]){
        const isValid = (a:number,b:number) => a<this.maze.length&&a>=0&&b<this.maze[0].length&&b>=0&&this.maze[a][b]!==1;
        if (!isValid(r,c)) throw new Error(`Invalid indexes R:${r}, C:${c}, index does not lie in maze matrix`);
        return [-1,1,-1,1].map((v,i)=>i>1?[r,c+v]:[r+v, c]).filter(([nr,nc])=>isValid(nr,nc)) as [number,number][];
    }
    solution1(){
        const coordinateKey = (c:[number, number]) => c.join("-"), coordinate = (k:string) =>  k.split('-').map(Number) as [number,number];
        /**distMap tracks the shortest distance from starting node to node-k */
        const destinationKey = coordinateKey(this.destCoordinate), startKey = coordinateKey(this.startCoordinate)
        const distMap: {[k:string]:number} = {[startKey]:0};
        const unTraversedNodes = [startKey];
        const traversedNodes:string[] = []

        while(!!unTraversedNodes.length){
            const node = unTraversedNodes.sort((a,b)=>distMap[b]-distMap[a]).pop() as string;
            let distFound = false;
            for(let nodeNeighbor of this.getNeighbors(coordinate(node)).map(coordinateKey)){
                const startToNeighborDist = nodeNeighbor in distMap ? distMap[nodeNeighbor] : Infinity;
                if (distMap[node]+1<startToNeighborDist) distMap[nodeNeighbor] = distMap[node]+1;
                if (!traversedNodes.includes(nodeNeighbor)) unTraversedNodes.push(nodeNeighbor);
                if (nodeNeighbor === destinationKey){
                    distFound = true; break;
                }
            };
            if (distFound) break
            traversedNodes.push(node);
        };

        return destinationKey in distMap ? distMap[destinationKey] : Infinity
    }
};

(
    ()=>{
        const ARGS = [
            [
                [  // Maze
                    [0, 0, 1, 0, 0],
                    [0, 0, 0, 0, 0],
                    [0, 0, 0, 1, 0],
                    [1, 1, 0, 1, 1],
                    [0, 0, 0, 0, 0]
                ],
                [0, 4], // Start coordinate
                [4, 4]  // Destination coordinate
            ],
            [
                [  // Maze
                    [0, 0, 1, 0, 0],
                    [0, 0, 0, 0, 0],
                    [0, 0, 0, 1, 0],
                    [1, 1, 0, 1, 1],
                    [0, 0, 0, 0, 0]
                ],
                [0, 4], // Start coordinate
                [3, 2]  // Destination coordinate
            ]
        ] as const;
        ARGS.forEach(([maze, startCoordinate, destinationCoordinate]) =>{
            console.log('\r\nMaze');
            for(let r of maze) console.log(`${" ".repeat(5)+r.join(" ")}`);
            console.log(`start=${startCoordinate}, destination=${destinationCoordinate}`);
            //@ts-ignore
            console.log(`Solution -> ${new Solve505(maze,startCoordinate,destinationCoordinate).solution1()}`)
        })
    }
)()
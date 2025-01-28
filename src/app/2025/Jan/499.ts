/**
 * Input 1: a maze represented by a 2D array

0 0 0 0 0
1 1 0 0 1
0 0 0 0 0
0 1 0 0 1
0 1 0 0 0

Input 2: ball coordinate (rowBall, colBall) = (4, 3)
Input 3: hole coordinate (rowHole, colHole) = (0, 1)

Output: "lul"

Explanation: There are two shortest ways for the ball to drop into the hole.
The first way is left -> up -> left, represented by "lul".
The second way is up -> left, represented by 'ul'.
Both ways have shortest distance 6, but the first way is lexicographically smaller because 'l' < 'u'. So the output is "lul".

Input 1: a maze represented by a 2D array

0 0 0 0 0
1 1 0 0 1
0 0 0 0 0
0 1 0 0 1
0 1 0 0 0

Input 2: ball coordinate (rowBall, colBall) = (4, 3)
Input 3: hole coordinate (rowHole, colHole) = (3, 0)

npx ts-node ./src/app/2025/Jan/499.ts
 */

class Solve499{
    constructor(public maze:number[][],public ballCoordinate:[number, number], public holeCoordinate:[number, number]){
        this.maze = maze; this.ballCoordinate = ballCoordinate; holeCoordinate = holeCoordinate;
    };
    constructGraph(){
        const graph: {[k:string]:[number,number][]} = {};
        const r = this.maze.length, c = this.maze[0].length, [ri, ci] = this.ballCoordinate, [rn,cn] = this.holeCoordinate;

        let tw = Array.from({length:c},()=>-1)
        for(let i=0; i<r; i++){
            let lw=-1
            for(let j=0; j<c; j++){
                if (this.maze[i][j]===1){
                    tw[j] = i;
                    lw=j;
                } else if (i===rn&&j==cn){
                    lw=j-1;
                    tw[j]=i-1
                } else {
                    const key = `${i}-${j}`;
                    if (!(key in graph)) graph[key] = [];
                    graph[key].push([tw[j]+1, j])//top
                    let rw = j;
                    while(rw<c&&this.maze[i][rw]===0){
                        if (rw++===cn&&i===rn) break;
                    };
                    graph[key].push([i, rw-1]) //right
                    let bw = i;
                    while(bw<r&&this.maze[bw][j]===0){
                        if (bw++===rn&&j===cn) break
                    }
                    graph[key].push([bw-1, j]) //bottom
                    graph[key].push([i, lw+1]) //left
                }
            }
        };
        return graph
    }
    solution1(){
        const r = this.maze.length, c = this.maze[0].length, [ri, ci] = this.ballCoordinate, [rn,cn] = this.holeCoordinate;
        if ([ri,rn].every(rv=>rv>=0&&rv<r)&&[ci,cn].every(cv=>cv>=0&&cv<c)&&this.maze[rn][cn]!==1){
            const graph = this.constructGraph();
            
            const queue: [string/**currKey */, string/**path */][] = [[`${ri}-${ci}`, '']];
            const visited :{[k:string]:any} = {}
            //running bfs
            while(queue.length){
                const [currKey, path] = queue.shift()!;
                if (currKey===`${rn}-${cn}`) return path;

                const dir = ['u','r','d', 'l'];
                visited[currKey] = true;
                for(let i=0; i<4; i++){
                    const neighbor = graph[currKey][i].join('-');
                    if (!(neighbor in visited)) queue.push([neighbor, path+dir[i]])
                }
            };
        };
        return 'impossible'
    }
};


(
    ()=>{
        const ARGS = [
            [
                [
                    [0, 0, 0, 0, 0],
                    [1, 1, 0, 0, 1],
                    [0, 0, 0, 0, 0],
                    [0, 1, 0, 0, 1],
                    [0, 1, 0, 0, 0]
                ],
                [4,3], [0,1] 
            ]
        ] as const;
        ARGS.forEach(
            //@ts-ignore
            ([maze, start, end]) => console.log(`start=${start}, end=${end} Sol-> ${new Solve499(maze, start, end).solution1()}`)
        )
    }
)()
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
    };

    solution2(){
        class PQ<T>{
            private heap: T[] = [];
            constructor(private compareFn:(a:T,b:T)=>number){
                this.compareFn = compareFn
            };
            push(elem:T){
                this.heap.push(elem); this.heap.sort(this.compareFn)
            };
            pop():T|undefined{
                return this.heap.shift()
            };
            size(){
                return this.heap.length
            }
        };

        const fn = () => {
            const dirs = [
                [1, 0, 'd'], [-1, 0, 'u'], [0, -1, 'l'], [0, 1, 'r']
            ] as const;
            const [m,n] = [this.maze.length, this.maze[0].length];
            const [ri,ci] = this.ballCoordinate;
            const [rn, cn] = this.holeCoordinate;
            const distKey = (r:number,c:number) => `${r}-${c}`
            const dist = new Map<string , [number/**Min steps */,string/**lexicographically smallest path */]>();
            const pq = new PQ<
                [number/**distance */, string /**traveled path e.g: lru */, number /**row-index */, number/**col-index */]
            >( /**Shortest paths would have priority in heap */
                ([distA,pathA],[distB, pathB]) => (
                    (distA-distB) || (
                        /**in the case both paths are equal, then sort them lexicographically e.g `dlr` -> `ldr` */
                        pathA.localeCompare(pathB)
                    )
                )
            );
            /**Begin process of traversing */
            pq.push([0, "", ri, ci]);
            dist.set(distKey(ri,ci), [0,""]);
            while(pq.size()){
                const [d, path, r, c] = pq.pop()!;
                if (r===rn&&c===cn) return path;
                for(const [dr,dc,dir] of dirs){
                    let [nr, nc, steps] = [r, c, 0];
                    while(nr+dr>=0&&nr+dr<m&&nc+dc>=0&&this.maze[nr+dr][nc+dc]===0){
                        nr+=dr; nc+=dc; steps++;
                    };
                    const newDist = d+steps, newPath=path+dir, key = distKey(nr, nc)
                    if(
                        !dist.has(key) //doesn't have key
                        || newDist < dist.get(key)![0] //less distance
                        || ( //equal dist but less path
                            newDist === dist.get(key)![0] && newPath<dist.get(key)![1]
                        )
                    ){
                        pq.push([newDist,newPath, nr,nc]);
                        dist.set(key, [newDist, newPath])
                    }
                }
            };
            return 'impossible'
        }
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
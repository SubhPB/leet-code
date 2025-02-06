/**
 * 1631. Path With Minimum Effort

You are a hiker preparing for an upcoming hike. You are given heights, a 2D array of size rows x columns, where heights[row][col] represents the height of cell (row, col). You are situated in the top-left cell, (0, 0), and you hope to travel to the bottom-right cell, (rows-1, columns-1) (i.e., 0-indexed). You can move up, down, left, or right, and you wish to find a route that requires the minimum effort.

A route's effort is the maximum absolute difference in heights between two consecutive cells of the route.

Return the minimum effort required to travel from the top-left cell to the bottom-right cell.
Example 1:

Input: heights = [[1,2,2],[3,8,2],[5,3,5]]
Output: 2
Explanation: The route of [1,3,5,3,5] has a maximum absolute difference of 2 in consecutive cells.
This is better than the route of [1,2,2,2,5], where the maximum absolute difference is 3.
Example 2:

Input: heights = [[1,2,3],[3,8,4],[5,3,5]]
Output: 1
Explanation: The route of [1,2,3,4,5] has a maximum absolute difference of 1 in consecutive cells, which is better than route [1,3,5,3,5].
Example 3:


Input: heights = [[1,2,1,1,1],[1,2,1,2,1],[1,2,1,2,1],[1,2,1,2,1],[1,1,1,2,1]]
Output: 0
Explanation: This route does not require any effort.

CMD npx ts-node ./src/app/2025/Feb/1631.ts
 */

class Solve1631{
    constructor(public heights:number[][]){
        this.heights = heights
    };
    solution1(){
        const m = this.heights.length, n = this.heights[0].length;
        class PQ<T>{
            private queue:T[] = [];
            constructor(public sort: (a:T,b:T)=>number){
                this.sort = sort
            }
            pop(){return this.queue.shift()};
            insert(v:T){
                this.queue.push(v);
                this.queue.sort(this.sort)
            };
            size(){return this.queue.length}
        };
        const startingNode= {
            traversedNodes: 1, // 1<<0
            currRow:0, currCol:0, maxDiff:0
        };
        const getNode = (r:number,c:number) => r*n+(c+1);
        const utils = (v:number) => ({inRange: (l:number,h:number)=>l<=v&&v<h, positive:()=>v<0?-v:v});
        const pq = new PQ<typeof startingNode>((a,b)=>a.maxDiff-b.maxDiff);
        pq.insert(startingNode);

        while(pq.size()){
            const {traversedNodes, currRow, currCol, maxDiff} = pq.pop()!;
            const currNode = getNode(currRow, currCol);
            if (currNode===m*n) return {traversedNodes, maxDiff};
            for(let [row,col] of [[0,1],[1,0],[0,-1],[-1,0]].map(([r,c])=>[currRow+r,currCol+c])){//left, down, right, up
                const nextNode = getNode(row,col);
                if(
                    utils(row).inRange(0,m)
                    &&utils(col).inRange(0,n)
                    &&(!(traversedNodes&1<<nextNode))
                ){
                    const nextDiff = utils(this.heights[currRow][currCol]-this.heights[row][col]).positive();
                    pq.insert({
                        traversedNodes: traversedNodes|1<<nextNode,
                        currRow: row, currCol: col,
                        maxDiff: Math.max(
                            maxDiff,
                            utils(this.heights[currRow][currCol]-this.heights[row][col]).positive()
                        )
                    })
                }
            };
        };
        return {traversedNodes:-1, maxDiff:Infinity}
    }
};

(
    ()=>{
        const ARGS:{heights:number[][], expected:number}[] = [
            {
                heights: [[1,2,2],[3,8,2],[5,3,5]],
                expected: 2,
            },
            {
                heights: [[1,2,3],[3,8,4],[5,3,5]],
                expected: 1,
            },
            {
                heights: [[1,2,1,1,1],[1,2,1,2,1],[1,2,1,2,1],[1,2,1,2,1],[1,1,1,2,1]],
                expected: 0
            }
        ];
        ARGS.forEach(({heights,expected})=>{
            console.log(`Leetcode-[1631], size=[${heights.length}, ${heights[0].length}] expected=${expected} found=%O`,new Solve1631(heights).solution1())
        })
    }
)();


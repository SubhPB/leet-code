/**
 * 827. Making A Large Island

You are given an n x n binary matrix grid. You are allowed to change at most one 0 to be 1.
Return the size of the largest island in grid after applying this operation.
An island is a 4-directionally connected group of 1s.

Example 1:

Input: grid = [[1,0],[0,1]]
Output: 3
Explanation: Change one 0 to 1 and connect two 1s, then we get an island with area = 3.
Example 2:

Input: grid = [[1,1],[1,0]]
Output: 4
Explanation: Change the 0 to 1 and make the island bigger, only one island with area = 4.
Example 3:

Input: grid = [[1,1],[1,1]]
Output: 4
Explanation: Can't change any 0 to 1, only one island with area = 4.


npx ts-node ./src/app/2025/Feb/827.ts

 */


class Solve827{
    constructor(public G:number[][]){
        this.G=G
    };
    solution1(grid=this.G){

        const m = grid.length, n = grid[0].length;

        class Island {
            public land:{[k:string]:any} = {};
            landKey(r:number,c:number){
                return `${r}-${c}`
            };
            area(){
                return Object.keys(this.land).length;
            }
            add(r:number,c:number){
                if (this.includes(r,c)) return false;
                this.land[this.landKey(r,c)] = true;
                return true
            };
            includes(r:number,c:number){
                return this.landKey(r,c) in this.land
            };
        };

        const left = [0,-1], top = [-1,0], right = [0,1], down = [1,0];
        
        const islands: Island[] = [];
        let islandLabel = -1; //Labels starts from -1 to -n
        const getIsland = (label:number) => islands[label + 2*(-label) - 1];

        for(let r=0; r<m; r++){
            for(let c=0; c<n; c++){
                //If grid[currRow][currCol] holds a -ve values then it means it's been a part of a island and been traversed.
                if (grid[r][c]===1){
                    const island = new Island();
                    const queue = [[r,c]];
                    while(queue.length){
                        const [currRow,currCol] = queue.shift()!;
                        
                        island.add(currRow,currCol);
                        grid[currRow][currCol] = islandLabel;

                        for(let [ri,ci] of [left,top,right,down]){
                            const nextRow = currRow+ri, nextCol = currCol+ci;
                            if (nextRow>=0&&nextRow<m&&nextCol>=0&&nextCol<n
                                &&grid[nextRow][nextCol]===1
                            ){
                                queue.push([nextRow,nextCol])
                            }
                        }
                    };
                    islands.push(island)
                    islandLabel--;
                };
            }
        };

        let maxArea = 0;
        
        for(let r=0; r<m; r++){
            for(let c=0; c<n; c++){
                if (grid[r][c]===0){
                    let tempArea = 1; 
                    const islandLabels:number[] = []
                    for(let [ri,ci] of [left,top,right,down]){
                        const nextRow = r+ri, nextCol = c+ci;
                        if (nextRow>=0&&nextRow<m&&nextCol>=0&&nextCol<n
                            &&grid[nextRow][nextCol]!==0&&!islandLabels.includes(grid[nextRow][nextCol])
                        ){
                            islandLabels.push(grid[nextRow][nextCol]);
                            tempArea += getIsland(grid[nextRow][nextCol]).area()
                        }
                    };
                    if (tempArea>maxArea) maxArea = tempArea
                } else {
                    maxArea = Math.max(maxArea, getIsland(grid[r][c]).area())
                }
            }
        };

        return maxArea

    }
};

(
    ()=>{
        const ARGS = [
            [[1,0],[0,1]],
            [[1,1],[1,0]],
            [[1,1],[1,1]],
            [[0,0],[0,0]],
            [[1,1],[1,1]],
            [[1,1,0,1],[1,0,0,1],[1,0,0,1],[1,0,0,1]],
            [[1,0,1,0],[0,0,0,1],[1,0,1,0],[1,0,1,0]],
            [[0,0,0,1,1],[1,0,0,1,0],[1,1,1,1,1],[1,1,1,0,1],[0,0,0,1,0]],
            [[0,1,1,1,0,0,1,1,1,1,0],[0,1,1,1,0,0,1,1,1,1,0],[0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0]],
            [[1,1,0,0,0,1,1,0,0,1,1,0,0,1,0,0,0,0,0,1,0,0,1,1,1,1,1,1,0,0,1,0,1,0,1,0,1,1,0,0,1,0,0,1,1,1,0,1,1],[0,0,1,1,0,0,0,1,0,1,0,0,1,1,1,1,0,1,0,0,0,0,0,1,1,0,1,0,0,0,1,0,1,0,1,1,0,1,1,1,1,1,0,0,1,0,0,0,1],[0,0,1,0,0,1,1,0,0,0,0,1,1,1,1,0,1,0,1,0,0,0,0,0,1,0,1,0,1,0,0,0,1,0,1,0,1,0,1,0,1,0,1,1,0,0,0,0,0],[1,1,1,1,1,1,1,1,0,1,0,1,0,0,1,1,1,1,0,1,0,1,0,0,1,1,1,0,1,0,1,1,0,1,1,1,1,0,0,0,1,0,1,1,0,0,0,1,1],[1,0,0,0,1,1,0,1,0,0,1,0,0,0,0,0,0,0,0,1,0,1,1,1,0,1,0,1,0,0,1,0,1,1,1,1,1,1,0,0,0,1,0,0,0,0,1,1,1],[1,0,0,0,0,1,1,0,1,1,1,1,1,1,0,1,1,1,0,0,0,1,0,1,1,1,0,0,0,0,0,1,1,1,0,0,0,1,0,1,1,1,0,0,0,0,0,0,1],[0,0,0,0,0,1,1,0,0,0,1,1,1,0,1,0,0,0,0,1,0,0,0,0,0,1,0,0,1,0,1,0,1,0,1,0,0,1,0,1,0,0,1,1,1,0,1,0,1],[0,1,0,0,0,1,1,0,1,1,0,0,1,1,0,0,1,0,0,0,0,1,1,1,1,0,1,1,1,1,1,0,1,0,0,1,0,1,1,0,0,0,1,1,0,1,0,1,0],[0,1,1,0,0,0,1,0,0,0,1,1,0,0,1,0,1,1,1,1,0,1,1,1,0,0,1,0,0,1,0,1,1,1,1,0,0,1,1,0,1,0,0,1,0,0,1,1,0],[1,1,1,1,0,1,0,1,1,0,1,1,1,1,0,1,0,0,0,0,0,1,1,1,0,1,0,0,1,0,0,1,0,0,1,0,1,1,1,0,1,0,0,1,0,0,1,1,0],[1,1,0,1,1,1,0,1,0,1,1,1,1,0,0,0,1,0,0,0,1,0,0,1,1,0,1,0,0,0,0,0,1,0,0,1,0,0,0,1,1,1,1,1,1,0,0,0,0],[1,1,0,1,1,1,1,1,1,0,1,1,1,0,0,0,1,0,0,0,0,0,0,0,0,1,1,1,1,1,0,1,0,0,1,1,0,1,1,0,0,0,1,1,1,0,0,1,0],[0,1,0,0,1,1,1,1,0,0,0,1,1,1,0,1,0,1,0,0,1,0,0,1,0,1,1,0,0,0,0,0,0,1,1,1,1,0,1,1,1,0,1,0,0,0,1,0,0],[0,1,1,0,1,0,1,1,0,0,1,1,0,1,0,1,1,1,0,0,0,1,1,1,1,1,1,1,1,0,0,0,0,0,1,0,0,1,1,1,0,1,1,0,1,1,1,0,1],[0,1,1,1,0,0,1,1,0,0,1,1,0,1,0,1,1,0,0,0,0,1,1,0,0,0,1,1,0,1,1,0,1,1,0,0,0,0,0,0,0,0,1,0,0,0,1,1,0],[0,0,1,1,1,0,1,1,0,0,1,0,0,0,1,1,1,1,0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,0,0,1,1,1,0,0,0,0,0,1,1,1,1,0,0],[0,1,0,0,1,1,0,0,1,1,0,0,0,1,1,0,0,1,1,0,1,0,1,1,0,0,0,1,0,0,0,0,1,1,0,1,0,1,0,0,0,0,0,1,0,1,1,1,0],[1,1,0,0,1,1,1,0,1,0,0,1,0,0,0,0,1,1,0,1,0,0,0,1,1,0,1,0,1,1,1,1,0,0,0,0,1,1,0,1,0,0,1,0,0,1,1,0,0],[1,0,1,0,0,1,1,0,0,0,1,1,1,1,0,0,0,1,0,0,0,1,1,0,0,1,1,1,0,0,1,0,1,0,1,0,0,1,1,1,0,1,0,0,1,1,0,0,1],[0,0,0,0,0,0,1,1,1,1,0,0,1,1,1,0,0,1,1,1,0,0,1,1,1,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0,1,0,0,1,1,1,0,0,0],[0,0,0,0,1,1,0,0,0,1,0,1,1,1,1,1,1,1,1,1,1,0,0,1,1,1,0,1,0,0,0,0,1,1,1,1,0,1,1,0,1,1,0,1,1,1,0,1,0],[0,0,1,0,0,0,0,0,1,0,0,1,1,1,0,0,1,0,0,1,1,0,1,1,0,0,0,1,0,0,0,0,1,1,1,0,0,1,1,1,1,0,0,0,1,0,1,0,1],[0,0,0,1,0,0,1,1,0,1,0,0,1,1,1,0,1,0,0,1,1,0,1,1,0,1,1,1,0,0,0,1,0,0,0,0,0,0,1,0,0,1,0,1,0,0,1,1,1],[0,1,1,0,0,1,0,0,1,1,0,0,1,0,1,0,1,1,1,0,0,0,1,0,0,0,0,0,0,1,1,0,0,1,0,1,0,0,0,0,1,1,0,1,1,1,1,1,0],[0,1,1,1,1,1,0,1,0,1,0,0,0,1,1,1,1,1,0,0,1,1,0,0,1,1,0,0,0,1,1,1,1,0,0,1,1,1,0,1,0,1,1,0,1,0,1,1,0],[0,1,1,0,0,0,0,0,1,1,1,1,1,1,0,1,0,0,0,0,1,1,0,1,1,0,1,1,1,1,1,0,0,0,1,0,1,1,0,1,1,0,1,1,1,1,0,1,0],[0,0,0,0,1,1,1,0,0,0,1,0,0,0,1,1,0,0,1,0,0,1,1,0,0,1,1,0,1,0,0,1,0,0,1,0,1,0,0,0,0,0,1,1,1,1,0,1,1],[0,0,1,1,0,1,0,1,1,0,1,0,1,1,1,1,0,0,1,1,0,0,1,1,0,1,1,0,1,0,1,1,0,1,0,0,0,0,1,1,1,1,0,0,0,1,0,1,0],[0,1,1,0,1,1,0,1,1,1,0,1,1,1,0,0,0,1,0,0,1,1,1,0,0,0,1,1,1,1,1,0,1,0,1,0,0,1,1,1,0,0,0,0,1,0,1,1,1],[0,0,0,0,1,0,1,1,1,0,1,0,0,1,0,1,1,1,1,1,1,1,1,1,1,1,0,0,0,1,0,1,0,1,1,0,1,1,0,0,1,1,1,1,0,0,1,0,1],[1,0,1,1,0,0,0,0,0,0,1,1,0,1,1,1,1,0,0,1,0,1,0,1,1,1,1,1,0,0,1,0,0,1,1,0,0,0,1,0,0,1,0,1,0,0,1,0,1],[0,0,1,0,0,1,1,1,1,1,0,1,0,1,0,1,1,0,1,0,1,1,1,0,0,0,1,0,1,1,1,0,1,1,0,0,0,1,1,0,0,1,0,0,0,1,1,1,1],[0,1,1,1,0,0,0,1,0,1,1,0,0,1,1,1,0,0,1,1,1,0,1,0,1,1,1,1,1,0,1,1,0,0,1,0,1,0,1,1,0,1,0,0,0,0,0,1,1],[1,0,1,1,1,1,0,0,1,0,0,0,1,0,1,1,1,0,1,0,0,0,1,0,1,0,1,1,0,0,1,1,0,0,0,0,1,0,0,0,1,1,0,1,1,0,0,0,1],[0,0,0,0,1,0,1,0,0,1,0,0,0,1,0,0,0,1,1,0,1,0,0,1,1,0,1,1,1,1,0,0,1,1,1,1,0,0,0,1,1,0,0,1,1,1,1,1,1],[0,1,0,1,0,1,1,0,0,1,1,1,1,0,1,0,1,1,1,1,0,0,0,1,0,1,0,0,0,1,1,1,1,1,1,1,1,1,1,0,0,1,1,1,0,1,0,0,0],[0,1,0,1,0,0,0,0,1,1,0,0,0,1,1,0,0,0,1,0,1,1,1,0,0,1,1,1,1,1,1,0,0,0,1,0,1,1,1,1,0,1,1,0,1,1,1,0,1],[0,1,0,1,0,0,0,1,1,1,1,0,0,1,1,1,0,1,1,1,1,0,1,0,0,0,1,0,0,0,1,0,1,1,1,0,1,0,0,1,0,0,1,0,0,0,1,1,0],[1,0,0,0,1,0,1,1,1,0,0,1,0,0,0,0,1,1,1,1,0,0,0,0,1,0,0,0,0,1,1,1,1,1,0,0,1,1,1,0,0,0,1,1,1,0,1,1,0],[1,1,0,0,0,1,1,1,1,0,0,1,1,1,1,0,0,1,1,1,0,1,0,0,0,1,0,0,1,0,0,1,0,1,0,0,0,0,0,0,1,0,0,0,0,1,1,0,1],[1,1,1,1,1,1,0,1,0,0,0,0,0,1,0,0,0,0,0,1,0,1,1,1,1,1,1,0,0,0,1,0,1,0,0,0,1,0,1,0,1,0,1,0,0,0,0,1,0],[0,0,0,0,0,0,0,1,0,0,0,1,1,1,1,1,1,0,0,1,1,0,1,1,0,1,0,0,0,0,1,1,0,1,0,0,0,1,1,1,1,0,0,1,1,1,1,1,0],[0,1,1,1,1,0,0,1,1,0,0,1,0,1,0,0,0,1,1,1,0,1,1,0,0,1,1,1,1,0,1,1,0,1,0,1,1,1,0,1,0,0,1,1,0,0,1,1,0],[0,0,1,1,1,0,1,0,1,0,0,0,1,0,0,0,0,1,0,0,1,1,1,1,1,0,0,0,1,1,0,1,1,1,1,0,1,0,0,0,1,1,0,1,0,0,0,0,1],[1,1,0,1,1,1,0,1,1,1,1,0,1,0,1,0,0,0,0,1,0,0,1,1,0,1,1,0,0,0,0,0,0,1,1,0,1,0,1,0,0,0,1,0,1,0,0,1,1],[0,1,1,0,0,0,1,1,0,0,0,1,0,1,0,1,0,0,1,1,0,1,0,1,0,1,1,0,0,0,1,0,1,1,1,0,1,1,1,0,0,1,0,1,0,1,0,0,1],[1,1,0,1,0,1,1,1,0,1,0,0,0,0,0,1,1,1,0,1,1,1,0,0,1,1,1,1,0,1,0,0,0,0,1,0,1,0,1,1,0,0,1,1,0,0,0,0,0],[1,1,1,1,1,0,0,1,0,0,0,0,1,1,0,1,0,1,0,1,0,0,1,1,0,1,0,1,1,1,1,0,0,1,0,0,1,0,1,1,0,0,0,0,1,1,0,0,1],[1,0,0,1,1,0,1,0,1,1,1,1,0,0,0,1,0,1,0,0,1,1,0,1,1,1,1,1,1,0,0,1,0,1,0,0,0,1,0,0,1,1,1,0,1,0,0,0,0]],
            [[0,0,0,1,1,0,0,0,1,1,0,0,1,0,0,0,1,0,1,1,0,0,0,1,0,0,1,0,0,1,0,0,1,1,1,1,0,0,0,0,0,1,1,1,1,0,0,1,1,1],[1,1,1,1,1,0,0,0,1,1,1,0,0,1,0,1,1,1,1,1,0,1,0,1,1,0,1,1,1,1,1,1,0,0,1,1,1,0,1,1,0,0,1,0,0,0,0,0,1,1],[1,0,1,1,0,1,1,1,1,1,1,0,0,1,1,1,0,1,0,1,1,0,1,0,0,1,0,0,0,0,1,1,1,0,1,0,0,1,0,1,1,1,0,1,0,0,0,0,0,0],[1,1,1,1,1,1,1,1,1,0,1,0,0,0,0,0,1,0,0,0,0,1,1,0,0,1,1,1,0,1,0,0,1,1,1,1,0,1,1,1,1,1,0,0,0,1,0,0,1,0],[1,0,0,1,1,0,1,0,0,0,0,0,0,1,1,1,1,0,0,1,1,0,0,0,0,1,1,0,0,1,1,0,0,0,0,1,0,0,1,1,0,1,1,0,1,0,0,0,0,0],[0,0,1,0,0,1,0,1,0,1,1,0,0,0,0,1,1,1,1,0,0,1,1,1,0,1,1,1,0,0,1,1,0,1,0,1,0,1,1,0,0,1,0,1,1,0,1,1,1,0],[1,1,1,1,0,1,1,1,0,0,1,0,1,1,0,1,0,0,1,0,0,1,1,0,1,0,1,0,0,0,1,0,1,1,0,1,0,1,1,1,1,1,1,0,1,0,1,0,0,0],[0,0,1,0,1,1,0,1,1,0,0,0,1,1,1,0,0,0,0,0,1,1,1,0,1,0,0,1,0,0,0,0,1,0,0,0,0,1,1,1,0,0,0,0,1,0,1,1,0,1],[0,0,0,0,0,0,0,0,0,0,1,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,1,1,0,1,1,0,0,1,1,1,0,1,1,1,1,1,1,0,0,0,1,1,1,1],[1,0,0,0,1,0,1,0,0,0,0,0,1,1,0,0,0,1,1,1,0,0,1,0,0,1,0,0,0,0,1,1,0,1,0,1,0,0,0,1,1,1,0,1,0,1,1,1,0,1],[0,1,1,0,1,0,1,0,1,1,1,0,0,1,0,1,0,1,1,1,0,0,0,1,0,0,1,0,1,0,1,1,0,0,1,0,0,1,1,0,0,1,1,1,0,1,1,1,0,1],[0,0,1,0,0,0,1,0,0,0,0,1,0,1,1,0,1,1,1,0,1,0,1,0,0,1,0,0,0,0,0,1,1,0,0,0,0,0,0,1,0,0,1,1,0,0,0,0,0,1],[1,0,1,0,0,1,0,1,1,0,0,1,1,0,0,1,0,1,0,0,1,0,0,0,1,0,1,1,0,1,1,0,1,0,0,1,0,0,1,1,0,0,1,0,1,1,1,1,1,0],[0,0,1,0,0,0,1,0,1,1,1,0,1,0,0,1,1,0,1,0,1,0,1,0,0,0,0,1,1,0,1,0,0,1,1,0,0,1,0,0,0,1,0,0,0,0,0,0,1,0],[0,0,0,0,1,1,0,0,0,1,0,0,0,0,0,0,1,0,1,1,1,1,1,0,1,0,1,1,1,1,0,0,0,0,0,0,1,1,0,0,1,0,0,1,0,0,0,1,0,1],[1,0,0,1,1,0,1,1,1,0,1,0,1,1,0,0,1,0,1,1,0,1,1,0,1,0,1,1,1,1,1,1,0,0,0,1,0,0,0,0,1,1,1,1,0,0,0,0,1,1],[0,1,0,1,1,1,1,1,1,1,1,0,1,0,1,1,1,1,1,1,1,0,0,1,1,0,0,0,1,0,1,0,0,0,1,0,0,0,1,1,1,0,0,1,1,0,0,0,1,0],[1,1,0,0,1,1,1,1,0,1,0,0,1,0,0,0,1,1,1,0,1,1,1,1,1,1,0,1,1,1,1,0,1,1,0,1,0,1,1,1,1,0,1,0,1,1,0,1,1,0],[1,0,1,1,0,0,1,0,0,0,0,1,1,0,1,0,0,1,0,0,0,1,1,0,0,1,0,0,1,1,0,0,0,1,0,1,1,1,0,1,1,1,1,0,1,0,0,1,1,1],[1,1,1,0,0,0,1,1,0,1,1,1,1,1,1,0,0,1,0,1,1,1,1,1,0,1,0,1,1,0,0,1,1,1,0,0,1,1,1,0,0,0,1,0,1,0,1,0,0,1],[0,1,0,0,1,0,1,0,1,0,1,1,1,0,0,0,0,1,1,0,1,1,1,0,0,1,0,0,1,0,1,0,1,0,1,0,0,0,0,1,0,1,1,0,0,0,0,1,1,0],[0,1,1,0,0,0,0,1,0,0,1,1,0,1,1,0,1,0,0,1,1,1,0,1,1,1,0,0,0,0,0,0,1,0,0,1,1,0,1,0,1,0,1,0,1,0,1,1,1,1],[1,1,1,1,1,0,0,0,1,1,1,0,1,1,0,1,0,0,0,1,0,0,0,1,0,0,1,1,1,1,0,1,1,1,1,1,1,1,1,1,0,0,0,1,0,1,0,0,0,1],[0,0,0,1,1,0,1,0,1,0,1,1,0,0,0,0,0,0,1,1,1,0,1,0,1,0,1,1,1,0,1,0,0,0,0,1,1,0,1,0,1,0,0,1,1,0,1,0,0,1],[0,0,0,1,0,1,1,0,0,0,0,1,1,1,0,0,0,0,0,0,1,1,1,0,0,1,1,0,1,1,1,1,1,0,1,0,0,0,0,0,0,1,0,1,1,1,0,1,0,0],[0,0,0,0,1,0,1,1,1,0,1,0,1,0,1,1,0,1,1,1,1,0,1,1,0,0,1,0,1,0,0,1,1,1,1,0,0,0,0,0,1,1,1,1,0,1,1,0,1,0],[1,0,0,0,0,0,1,0,0,1,1,1,1,0,0,0,1,1,1,1,1,0,1,1,1,0,0,0,0,1,1,0,0,0,1,1,0,1,1,1,0,1,0,0,0,0,1,1,1,1],[0,1,0,1,0,0,1,1,0,0,0,0,1,1,0,0,0,0,0,1,0,0,1,1,0,0,0,1,0,1,0,0,1,0,0,0,1,0,1,0,0,0,0,0,1,0,1,0,1,1],[1,1,1,1,1,1,1,0,1,1,0,1,1,0,0,1,1,1,0,1,1,0,1,0,1,0,0,0,1,0,0,1,1,1,1,1,1,1,0,0,1,0,0,0,0,0,0,0,0,0],[1,1,0,0,1,0,1,0,0,0,1,1,1,0,0,1,1,1,0,1,1,0,0,0,1,0,1,1,1,0,0,0,1,0,0,0,0,1,0,0,1,1,0,0,1,1,1,0,1,0],[0,0,1,1,1,0,0,1,0,0,1,1,1,1,0,1,1,0,1,1,1,0,0,0,0,0,0,1,1,1,0,1,1,0,1,0,0,0,1,0,0,1,0,1,0,0,1,0,0,1],[1,0,0,0,1,1,0,0,0,1,1,0,1,1,1,0,0,1,1,0,0,0,0,0,1,1,1,0,0,1,0,1,0,1,1,0,1,0,0,0,0,0,0,1,1,1,0,1,0,1],[0,1,1,1,1,0,1,1,1,1,1,1,1,0,1,1,0,0,1,0,0,0,0,0,0,0,1,1,0,1,0,1,0,1,1,1,0,1,1,0,1,0,0,1,0,0,0,0,1,1],[1,1,0,0,1,1,1,0,1,1,0,1,1,0,1,1,1,1,0,1,1,1,0,1,1,0,0,1,0,0,1,1,1,1,1,1,0,0,1,0,1,0,1,0,0,0,1,0,1,1],[1,1,1,0,0,0,0,0,0,1,0,1,0,1,1,1,0,0,0,1,0,0,1,0,0,0,1,0,0,1,0,0,1,0,1,1,0,0,1,1,1,1,0,1,1,0,0,1,0,0],[1,1,1,1,0,0,1,1,0,0,1,0,1,0,1,0,0,0,0,1,1,0,0,1,1,1,0,1,0,0,0,1,0,0,1,1,1,1,1,0,0,1,0,0,1,1,0,1,0,0],[1,0,0,0,0,0,0,0,1,1,1,1,0,0,1,0,1,0,0,1,0,0,1,1,1,0,0,0,1,0,1,0,0,0,1,1,1,1,1,1,1,0,1,1,1,1,0,0,1,1],[0,1,0,0,1,0,1,1,0,0,0,0,0,0,1,1,0,1,1,0,1,0,0,0,0,0,1,1,1,0,0,1,0,1,1,0,0,0,1,1,0,0,0,1,1,0,0,1,1,0],[0,0,0,1,1,1,0,1,1,0,0,1,1,1,0,1,1,0,1,1,1,1,0,1,0,1,0,0,0,1,1,0,0,0,0,0,1,0,1,1,1,1,1,0,0,1,1,0,0,1],[1,0,1,0,1,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,1,1,0,1,0,1,1,0,0,0,0,1,0,1,1,1,0,0,0,1,1,0,0,1,1,1,1],[0,0,1,0,1,1,0,0,1,0,1,0,1,0,1,1,0,1,0,1,0,1,0,0,0,0,0,1,1,0,0,1,1,1,0,1,1,1,1,1,0,0,0,1,0,0,0,0,0,0],[0,0,1,1,1,1,0,1,0,1,0,0,0,1,1,1,1,0,1,0,1,0,1,0,1,1,1,0,1,0,1,1,0,1,1,0,1,1,0,0,0,1,0,0,0,1,1,1,1,1],[1,1,0,1,1,0,1,0,1,0,1,1,1,1,0,0,0,0,1,0,1,1,1,0,1,0,0,0,1,1,0,1,0,0,1,0,1,1,1,0,1,1,1,0,1,1,1,1,1,1],[0,0,0,0,1,0,0,1,0,1,0,1,0,1,0,1,1,0,1,0,1,0,1,1,1,1,1,0,0,0,0,0,0,0,0,0,1,0,0,1,1,1,0,1,1,0,0,1,0,0],[0,0,0,0,0,1,0,1,0,0,0,0,0,0,1,0,0,1,1,1,0,0,0,0,1,1,0,0,1,1,1,1,1,0,1,1,1,1,0,0,1,0,0,0,0,0,0,0,1,1],[0,1,0,1,0,0,0,0,1,0,0,0,1,1,1,1,1,1,0,0,0,1,1,1,0,0,1,0,1,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,1,1,0,0,1,0],[0,1,1,1,0,1,0,1,1,0,1,0,1,1,1,1,0,0,0,1,0,1,0,0,1,0,1,0,1,0,1,0,0,0,1,1,0,1,0,1,0,0,0,0,0,1,0,1,0,1],[0,1,1,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,1,0,0,0,1,1,1,0,1,0,0,0,0,1,0,0,1,0,1,1,0,0,1,1,0,1,0,0,0,0,1,0],[0,1,1,1,0,0,1,1,0,1,0,1,0,1,0,0,0,0,1,0,0,1,1,1,0,1,0,1,0,1,1,1,0,1,1,1,1,1,1,0,0,0,1,0,0,0,1,1,1,1],[0,1,1,0,1,1,0,0,1,1,0,1,1,0,1,1,0,1,0,0,1,0,0,1,1,0,0,1,1,0,1,1,0,0,1,0,1,1,0,0,0,1,1,0,0,1,1,1,0,0]]
        ];
        ARGS.forEach(grid=>console.log(`Leetcode-[827] Making a large Island solution -> ${new Solve827(grid).solution1()}`))
    }
)()
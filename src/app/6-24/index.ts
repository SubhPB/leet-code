// Byimaan

/**
 * Given an m x n binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area;
 * CMD npx ts-node ./src/app/6-24/maximal-area/index.ts
 */

import { deepCopy } from "../../lib/utils/functions";

type Binary = '0' | '1'

const matrix: Binary[][] = [
    ["1","0","1","0","0"],
    ["1","0","1","1","1"],
    ["1","1","1","1","1"],
    ["1","0","0","1","0"]
];
const [m, n] = [matrix.length, matrix[0].length];

class Histogram {
    constructor(public arr: number[]){
        this.arr = arr
    };

    private inValidIndex(index: number){
        return index < 0 || index >= this.arr.length
    }

    leftWidth(index: number){
        if (this.inValidIndex(index)){
            throw new Error("Invalid index")
        };

        let width = 0;

        for(let i = index - 1; i >= 0; i--){
            if (this.arr[i] >= this.arr[index]){
                width++;
            } else {
                return width
            }
        };
        return width
    }

    rightWidth(index: number){
        if (this.inValidIndex(index)){
            throw new Error("Invalid index")
        };
        
        let width = 0;
        for(let i = index+1; i < this.arr.length; i++){
            if (this.arr[i] >= this.arr[index]){
                width++;
            } else {
                return width
            }
        };
        return width
    };

    findWidthArray(){
        return Array.from({length: this.arr.length}, (val, ind) => 1 + this.leftWidth(ind) + this.rightWidth(ind))
    };

    findAreaArray(){
        return this.findWidthArray().map(
            (val, ind) => val*this.arr[ind]
        )
    };

    claculateMaxArea(){
        return this.findAreaArray().reduce(
            (acc, val) => acc > val ? acc : val, -Infinity
        )
    }

}

// First we will find the maximum area for a square in matrix;

const maxSquareInMatrix = () => {
    const dp = Array.from({length: m+1}, () => Array(n+1).fill(0));
    let maxSize = 0;
    for(let i = 1; i <= m; i++){
        for(let j = 1; j <= n; j++){

            if (matrix[i-1][j-1] === '1'){
                dp[i][j] = Math.min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1]) + 1;
                if (maxSize < dp[i][j]){
                    maxSize = dp[i][j]
                }
            }

        }
    };
    return maxSize**2
};

const maxRectangleInMatrix = () => {
    
    const histogram = deepCopy(matrix) as string[][];
    let maxArea = 0
    for(let i = 1; i < m; i++){
        for(let j = 0; j < n; j++){
            if (histogram[i][j] === '1'){
                histogram[i][j] =  String(Number(histogram[i-1][j]) + 1)
            }
        };
        const maxHGArea = new Histogram(histogram[i].map(Number)).claculateMaxArea()

        if (maxArea < maxHGArea) {
            maxArea = maxHGArea
        }
    };

    return maxArea
};



console.log(maxRectangleInMatrix())
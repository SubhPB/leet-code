/**
 * 
Given a 2D matrix matrix, handle multiple queries of the following type:

Calculate the sum of the elements of matrix inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).
Implement the NumMatrix class:

NumMatrix(int[][] matrix) Initializes the object with the integer matrix matrix.
int sumRegion(int row1, int col1, int row2, int col2) Returns the sum of the elements of matrix inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).
You must design an algorithm where sumRegion works on O(1) time complexity.
Example 1:

Input
["NumMatrix", "sumRegion", "sumRegion", "sumRegion"]
[[[[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]], [2, 1, 4, 3], [1, 1, 2, 2], [1, 2, 2, 4]]
Output
[null, 8, 11, 12]

CMD npx ts-node ./src/app/2025/Jan/304.ts
 */

class Solve304{
    public matrix: number[][]; public rows: number; public cols: number; public sumMatrix: number[][];
    constructor(matrix:number[][]){
        this.matrix = matrix;
        this.rows = matrix.length, this.cols = matrix[0].length;
        this.sumMatrix = this.calcSumMatrix()
    };
    slotExist(r:number,c:number){
        return r>=0 && r<this.rows && c>=0 && c<this.cols
    };
    private calcSumMatrix(){
        const sumMatrix:number[][] = [];
        const sumMatrixSlotVal = (r:number,c:number,defVal=0) => this.slotExist(r,c) ? sumMatrix[r][c] : defVal;
        for(let r=0; r<this.rows; r++){
            sumMatrix.push([])
            for(let c=0; c<this.cols; c++){
                const subMatrixSum = sumMatrixSlotVal(r-1,c-1) + (
                   sumMatrixSlotVal(r-1, c) - sumMatrixSlotVal(r-1,c-1)
                ) + (
                    sumMatrixSlotVal(r, c-1) - sumMatrixSlotVal(r-1,c-1)
                ) + this.matrix[r][c];
                sumMatrix[r].push(subMatrixSum)
            }
        };
        return sumMatrix
    };
    sumRegion(r1:number,c1:number,rn:number,cn:number){
        if (r1<=rn && c1<=cn && [[r1,c1], [rn,cn]].every(([r1,c])=> this.slotExist(r1,c))){
            const sumMatrixSlotVal = (r:number,c:number,defVal=0) => this.slotExist(r,c) ? this.sumMatrix[r][c] : defVal; 
            return (
                sumMatrixSlotVal(rn,cn) 
                    - sumMatrixSlotVal(r1-1,cn)
                    - sumMatrixSlotVal(rn,c1-1)
                    + sumMatrixSlotVal(r1-1,c1-1)
            )
        };
        throw new Error(`Invalid region uppermost-left -> [${r1},${c1}] lowermost-right -> [${rn},${cn}] Matrix-size -> [${this.rows},${this.cols}]`)
    };
};

(()=>{
    const ARGS = [
        [[[[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]], [2, 1, 4, 3], [1, 1, 2, 2], [1, 2, 2, 4]]
    ] as const;
    ARGS.forEach(
        ([
            [matrix],...regions
        ]) => {
            //@ts-ignore
            const solve304 = new Solve304(matrix)
            console.log(`\r\n `);
            for(let [r1,c1,rn,cn] of regions){
                console.log(`region=${[r1,c1,rn,cn]} where sumRegions->${solve304.sumRegion(r1,c1,rn,cn)}`);
            }
        }
    )
})()
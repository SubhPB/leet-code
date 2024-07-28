// Byimaan

/**
 * Given an m x n integers matrix, return the length of the longest increasing path in matrix.

From each cell, you can either move in four directions: left, right, up, or down. You may not move diagonally or move outside the boundary (i.e., wrap-around is not allowed).

Example 1:

Input: matrix = [
    [9,9,4],
    [6,6,8],
    [2,1,1]
]
Output: 4
Explanation: The longest increasing path is [1, 2, 6, 9]


CMD :- npx ts-node ./src/app/7-24/longest-path-in-matrix.ts
 */

const Matrix = [
    [3, 4, 5],
    [4, 7, 6],
    [5 ,6, 10]
]

function findLongestpathInMatrix(matrix=Matrix){
    
    const directions = [
        [-1, 0], // up
        [0, 1], // right
        [1, 0], // down
        [0, -1], // left
    ];

    let longestPath: number[] = [];

    const isValid = (i:number, j:number, currVal: number) => {
        return (
            i >= 0 && i < matrix.length && j >=0 && j < matrix[0].length && currVal < matrix[i][j]
        )
    };
    
    const recursion = (i: number, j: number, path: number[]) => {
        
        const validDirections = directions.filter(dir => isValid(dir[0] + i, dir[1] + j,  matrix[i][j]));

        if (validDirections.length === 0 ){
            if (path.length + 1 > longestPath.length){
                longestPath = [...path, matrix[i][j]]
            };
        } else {
            for(let dir of validDirections){
                recursion(
                    dir[0]+i, dir[1]+j, [...path, matrix[i][j]]
                )
            }
        }
    };

    for (let i = 0;  i < matrix.length; i++){
        for(let j=0; j< matrix[0].length; j++) {
            recursion(i, j, [])
        }
    }

    return longestPath

};

console.log(findLongestpathInMatrix())
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
 */

const Matrix = [
    [9,9,4],
    [6,6,8],
    [2,1,1]
]

function findLongestpathInMatrix(matrix=Matrix){
    
    const directions = [
        [-1, 0], // up
        [0, 1], // right
        [1, 0], // down
        [0, -1], // left
    ];


    const longestPath = [];

    const solve = (i: number, j: number) => {
        const queue = [matrix[i][j]]
        
        while (queue.length !== 0){

            for(let dir of directions){

            }
        }
    }

};

console.log(findLongestpathInMatrix())
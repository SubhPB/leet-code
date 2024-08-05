/**
 * Byimaan
 * You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

Example 1:
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[7,4,1],[8,5,2],[9,6,3]]
Example 2:

Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]

CMD :-  npx ts-node ./src/app/8-24/rotate-image-48.ts
 */

const matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]];

type MatrixElemType = (typeof matrix[number][number])

function rotateImage(image=matrix){
    const rotatedImage = Array.from({length: image[0].length}, () => (
        Array.from({length: image.length}, () : null | MatrixElemType => null)
    ));

    for(let i = 0; i < image.length; i++){
        for (let j = 0; j < image[0].length; j++){
            rotatedImage[j][image.length - 1 - i] = matrix[i][j]
        }
    };
    return rotatedImage
};

for(let row of rotateImage()){
    console.log(JSON.stringify(row))
}
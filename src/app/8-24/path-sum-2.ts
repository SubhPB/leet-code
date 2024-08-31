/**
 * Byimaan
 * 
 * Path Sum II
Given the root of a binary tree and an integer targetSum, return all root-to-leaf paths where the sum of the node values in the path equals targetSum. Each path should be returned as a list of the node values, not node references.

A root-to-leaf path is a path starting from the root and ending at any leaf node. A leaf is a node with no children.

 

Example 1:


Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
Output: [[5,4,11,2],[5,8,4,5]]
Explanation: There are two paths whose sum equals targetSum:
5 + 4 + 11 + 2 = 22
5 + 8 + 4 + 5 = 22
Example 2:


Input: root = [1,2,3], targetSum = 5
Output: []
Example 3:

Input: root = [1,2], targetSum = 0
Output: []

CMD - npx ts-node ./src/app/8-24/path-sum-2.ts
 */

function pathSum(root =[5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22){

    const paths:number[][] = [];

    const isLeaf = (i:number) => i >= root.length || root[i] === null

    const BT = (index: number, sum: number, path: NonNullable<typeof root[number]>[]) => {

        if (index < 0){
            return
        }

        if (isLeaf(index) && sum === targetSum){
            paths.push([...path]);
            return
        }
        
        const currNode = root?.[index], leftInd = (2*index) + 1, rightInd = 2*(index+1);

        if(typeof currNode === 'number'){
            let newPath = [...path, currNode];
            // leftIndex
            BT(leftInd, sum + currNode, [...newPath]);
            BT(rightInd, sum + currNode, [...newPath])
        }
    };

    BT(0, 0, [])

    return paths
};

console.log(pathSum())
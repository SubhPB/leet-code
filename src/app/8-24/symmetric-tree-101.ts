/**
 * Byimaan
 * 
 * 101. Symmetric Tree
    Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).
    Example 1:

    Input: root = [1,2,2,3,4,4,3]
    Output: true

    CMD :- npx ts-node ./src/app/8-24/symmetric-tree-101.ts
 */

import { BSTTree, BSTNodeError } from "../../dsa/BST";

const isPalindrome = (arr: (string|number)[]) => {
    if (arr.length <= 2){
        return true
    }
    const _arr = Array.from(String(arr.join('')));
    const breaker = Math.ceil(arr.length / 2);
    return _arr.slice(0, breaker).join('') === _arr.slice(breaker).reverse().join('')
}

function isSymmetric(arr =[1,2,2,3,4,4,3]){

    try {
        const root = new BSTTree(arr);

        /** So our task is to check whether it is symmetric or not. Does the left side of the root is mirror reflection of the right. */
        /**
         * If we check very preciously then we will notice that in a symmetric tree every layer forms a palindrome.
         * So if all layers of the tree depth forms a palindrome then the tree is symmetric else it is non-symmetric
         * 
         * Q1 what wil be the depth of the tree if we are given with arr.length
         */
        const depth = Math.floor(arr.length / 2);
        const layers:number[][] = []

        for(let layerInd = 0; layerInd < depth; layerInd ++){
            /** Q2 if we know the at which tree level(level can be considered as layerInd) we are then how many woud exist in that layer   */
            const noOfNodesInThislayer = 2**layerInd;
            const layer = arr.slice(noOfNodesInThislayer - 1, 2*noOfNodesInThislayer - 1);
            layers.push(layer)
        };

        for(let layer of layers){
            console.log(layer)
        }
        return layers.every(layer => {return isPalindrome(layer)})

        
    } catch (error) {
        if (error instanceof BSTNodeError){
            console.log("The given array does not represents a valid BST tree");
            console.log(error.message)
            return false
        } else {
            throw error
        }
    }
}


console.log(isSymmetric())
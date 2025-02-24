/**
 * 889. Construct Binary Tree from Preorder and Postorder Traversal

Given two integer arrays, preorder and postorder where preorder is the preorder traversal
 of a binary tree of distinct values and postorder is the postorder traversal of the same tree,
  reconstruct and return the binary tree.

If there exist multiple answers, you can return any of them.

Example 1:

Input: preorder = [1,2,4,5,3,6,7], postorder = [4,5,2,6,7,3,1]
Output: [1,2,3,4,5,6,7]
Example 2:

Input: preorder = [1], postorder = [1]
Output: [1]

Constraints:

1 <= preorder.length <= 30
1 <= preorder[i] <= preorder.length
All the values of preorder are unique.
postorder.length == preorder.length
1 <= postorder[i] <= postorder.length
All the values of postorder are unique.
It is guaranteed that preorder and postorder are the preorder traversal and postorder traversal of the same binary tree.

npx ts-node ./src/app/2025/Feb/889.ts
 */

class Solve889WarmUp{
    constructor(public graph:{root: number; tree: { [parent: number]: number[] }} ){
        this.graph = graph 
    };
    preOrder(tree=this.graph.tree){
        const preOrder:number[] = [], n = Object.keys(tree).length, root = this.graph.root;
        if (n>0){
            const fn = (node:number) => { //A DFS approach
                preOrder.push(node);
                for(let child of tree[node]) fn(child);
            };
            fn(root)
        };
        return preOrder
    };
    postOrder(tree=this.graph.tree){
        const n = Object.keys(tree).length, postOrder:number[] = [], root = this.graph.root;
        if (n>0){
            const fn = (node:number) => { //A DFS approach
                for(let child of tree[node]) fn(child);
                postOrder.push(node);
            };
            fn(root)
        }
        return postOrder
    }
};

const _trees: { root: number; tree: { [parent: number]: number[] } }[] = [
    // Test Case 1: Simple Binary Tree
    {
      root: 1,
      tree: {
        1: [2, 3],
        2: [4, 5],
        3: [],
        4: [],
        5: [],
      },
    },
  
    // Test Case 2: Skewed Left Tree
    {
      root: 10,
      tree: {
        10: [20],
        20: [30],
        30: [40],
        40: [],
      },
    },
  
    // Test Case 3: Skewed Right Tree
    {
      root: 50,
      tree: {
        50: [60],
        60: [70],
        70: [80],
        80: [],
      },
    },
  
    // Test Case 4: More Complex Tree
    {
      root: 100,
      tree: {
        100: [200, 300],
        200: [400],
        400: [],
        300: [500, 600],
        500: [700],
        700: [],
        600: [],
      },
    },
  
    // Test Case 5: Balanced Tree
    {
      root: 1000,
      tree: {
        1000: [500, 1500],
        500: [200, 700],
        1500: [1200, 2000],
        200: [],
        700: [],
        1200: [],
        2000: [],
      },
    },
  
    // Test Case 6: Unbalanced Tree
    {
      root: 9000,
      tree: {
        9000: [8000],
        8000: [8500],
        8500: [8700],
        8700: [8800],
        8800: [8900],
        8900: [],
      },
    },
  ];
  
  // Expected Traversals:
  const _expectedTraversals = [
    { preorder: [1, 2, 4, 5, 3], postorder: [4, 5, 2, 3, 1] },
    { preorder: [10, 20, 30, 40], postorder: [40, 30, 20, 10] },
    { preorder: [50, 60, 70, 80], postorder: [80, 70, 60, 50] },
    { preorder: [100, 200, 400, 300, 500, 700, 600], postorder: [400, 200, 700, 500, 600, 300, 100] },
    { preorder: [1000, 500, 200, 700, 1500, 1200, 2000], postorder: [200, 700, 500, 1200, 2000, 1500, 1000] },
    { preorder: [9000, 8000, 8500, 8700, 8800, 8900], postorder: [8900, 8800, 8700, 8500, 8000, 9000] },
  ];

(
    ()=>{
        const isEqual = (a1:number[], a2:number[]) => {
            if (a1.length!==a2.length) return false;
            for(let i=0; i<a1.length; i++){
                if (a1[i]!==a2[i]) return false
            }
            return true
        }
        _trees.forEach((tree, i)=>{
            const preOrder = new Solve889WarmUp(tree).preOrder(), postOrder = new Solve889WarmUp(tree).postOrder()
            console.log('\n')
            console.log(`Testing Tree-${i+1} root=[${Object.keys(tree)[0]}] preOrder=[${preOrder.join(", ")}] expected=[${_expectedTraversals[i].preorder.join(', ')}]`, isEqual(preOrder, _expectedTraversals[i].preorder) ? " Passed! " : " Failed! ");
            console.log(`Testing Tree-${i+1} root=[${Object.keys(tree)[0]}] postOrder=[${postOrder.join(", ")}] expected=[${_expectedTraversals[i].postorder.join(', ')}]`, isEqual(postOrder, _expectedTraversals[i].postorder) ? " Passed! " : " Failed! ")
        })
    }
)()
  

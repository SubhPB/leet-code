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
            /**
            Recursive approach
                const fn = (node:number) => { //A DFS approach
                    preOrder.push(node);
                    for(let child of tree[node]) fn(child);
                };
                fn(root);
             *  
             */
            const stack = [root];
            while(stack.length){
                const node = stack.pop()!;
                preOrder.push(node);
                const children = node in tree ? tree[node] : []
                for(let i=children.length-1; i>=0; i--) stack.push(children[i])
            }
        };
        return preOrder
    };
    postOrder(tree=this.graph.tree){
        const n = Object.keys(tree).length, postOrder:number[] = [], root = this.graph.root;
        if (n>0){
            /**
             Recursive Approach
                const fn = (node:number) => { //A DFS approach
                    for(let child of tree[node]) fn(child);
                    postOrder.push(node);
                };
                fn(root)
             */

            const stack:number[]=[root];
            while(stack.length){
                const node:number = stack.pop()!;
                const isLeaf = !(node in tree) || tree[node].length===0;
                if (isLeaf) postOrder.push(node);
                else {
                    const possibleParent = postOrder[postOrder.length-1]
                    const childAreTraversed = Number.isInteger(possibleParent) && possibleParent in tree && (
                        tree[possibleParent][tree[possibleParent].length-1/**basically the last child */] === node
                    )
                    if (childAreTraversed){
                        postOrder.push(node)
                    } else {
                        for(let i=tree[node].length-1; i>=0; i--){
                            stack.push(tree[node][i])
                        }
                    }
                }
            };
        }
        return postOrder
    };
};

class Solve889{
  constructor(public preOrder:number[],public postOrder:number[]){
    this.preOrder=preOrder; this.postOrder=postOrder;
  };
  solution(preOrder=this.preOrder, postOrder=this.postOrder){
    const nodesCount = preOrder.length;
    const [preOrderIndex, postOrderIndex] = [Array(nodesCount).fill(-1), Array(nodesCount).fill(-1)];
    for(let i=0; i<nodesCount; i++){
      preOrderIndex[preOrder[i]] = i;
      postOrderIndex[postOrder[i]] = i;
    };
    const tree:(number|null)[] = [];
    const queue: ([[number,number]/**Indices indicating subPreOrder*/, [number,number] /**Indices indicating subPostOrder*/]|[])[] = [];
    while(queue.length){
      const indices = queue.pop()!;
      if (!indices.length){
        if (queue.every(indices => !indices.length)) break; //End of the tree traversal
        /**If zero length, indicates at some part our tree had only single child on either side & it's parent does not exist*/
        tree.push(null);
        for(let i=0; i<2; i++) queue.push([]); //It's child should also be null
      } else {
        const [[preStart,preEnd], [postStart, postEnd]] = indices;

        const subNodesCount = preEnd - preStart;
        if (subNodesCount!==postEnd-postStart) throw new Error(`Invalid indices, expected subArrays of same size but found of length ${subNodesCount} and ${postEnd-postStart}`);

        const currRoot = preOrder[preStart]; //or postOrder[postEnd-1]
        if (currRoot!==postOrder[postEnd-1]) throw new Error(`Invalid currRoot, ${currRoot} and ${postOrder[postEnd-1]} are different values`)
        tree.push(currRoot);
  
        //now time to traverse left and right side.
        /**
         * Challenge: Identify whether this currRoot has single child subtree or does it have both?
         * PreOrder works this way, ( Top -> Left -> Right ) & PostOrder works as ( Left -> Right -> Top )
         * Next to the currRoot means preOrder[preStart+1] can be either be at left side or right side.
         * If preOrder[preStart+1] === postOrder[postEnd-2] It means currRoot has only one child-subtree,
         *  because this condition shows that same node is both at left as well as right side, which contradicts out ordering mechanism,
         * else : preOrder[preStart+1] has been proved to be as left node of the currRoot
         */
        if (subNodesCount>0){
          if (preOrder[preStart+1]===postOrder[postEnd-2]){
            //Only one left-subtree. Now in next subproblem we will remove the currRoot from the indices
            const leftSubTreeIndices: typeof queue[number] = [
              [preStart+1, preEnd], // {PreOrder} Incrementing preStart because of (Top, left, right) remove top and move to the left as nextRoot
              [postStart, postEnd-1], // {PostOrder} decrementing postEnd because (Left, right, top) remove top and move to right as nextRoot
            ]
            queue.push(leftSubTreeIndices);
            queue.push([]); //Right subtree not exist so fill it with null
          } else {
            //There are both right and left-subtree
            /**
             *Let's first resolve left subtree, leftNode is preOrder[preStart+1] is for sure. How many children does in involves in its subtree?
             */            
            const leftSubTreeIndices: typeof queue[number] = [
              [preStart+1, preOrderIndex[postOrder[postEnd-1]]], //preOrder subpart
              [postStart, postOrderIndex[preOrder[preStart+1]]+1] //postOrder subPart
            ];
            queue.push(leftSubTreeIndices);

            const rightSubTreeIndices: typeof queue[number] = [
              [preOrderIndex[postOrder[postEnd-1]], preEnd], //preOrder subPart
              [postOrderIndex[preOrder[preStart+1]]+1, postEnd-1] //postOrder subPart
            ];
            queue.push(rightSubTreeIndices);
          }
        }
      }

    };
    return tree
  }
}

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
        // _trees.forEach((tree, i)=>{
        //     const preOrder = new Solve889WarmUp(tree).preOrder(), postOrder = new Solve889WarmUp(tree).postOrder()
        //     console.log('\n')
        //     console.log(`Testing Tree-${i+1} root=[${Object.keys(tree)[0]}] preOrder=[${preOrder.join(", ")}] expected=[${_expectedTraversals[i].preorder.join(', ')}]`, isEqual(preOrder, _expectedTraversals[i].preorder) ? " Passed! " : " Failed! ");
        //     console.log(`Testing Tree-${i+1} root=[${Object.keys(tree)[0]}] postOrder=[${postOrder.join(", ")}] expected=[${_expectedTraversals[i].postorder.join(', ')}]`, isEqual(postOrder, _expectedTraversals[i].postorder) ? " Passed! " : " Failed! ")
        // })
    }
)()
  

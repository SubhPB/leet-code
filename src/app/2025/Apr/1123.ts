/**
 * 1123. Lowest Common Ancestor of Deepest Leaves

    Given the root of a binary tree, return the lowest common ancestor of its deepest leaves.

    Recall that:

    The node of a binary tree is a leaf if and only if it has no children
    The depth of the root of the tree is 0. if the depth of a node is d, the depth of each of its children is d + 1.
    The lowest common ancestor of a set S of nodes, is the node A with the largest depth such that every node in S is in the subtree with root A.  

    Example 1:

    Input: root = [3,5,1,6,2,0,8,null,null,7,4]
    Output: [2,7,4]
    Explanation: We return the node with value 2, colored in yellow in the diagram.
    The nodes coloured in blue are the deepest leaf-nodes of the tree.
    Note that nodes 6, 0, and 8 are also leaf nodes, but the depth of them is 2, but the depth of nodes 7 and 4 is 3.
    Example 2:

    Input: root = [1]
    Output: [1]
    Explanation: The root is the deepest node in the tree, and it's the lca of itself.
    Example 3:

    Input: root = [0,1,3,null,2]
    Output: [2]
    Explanation: The deepest leaf node in the tree is 2, the lca of one node is itself.

    npx ts-node ./src/app/2025/Apr/1123.ts
 */

class Solve1123{
    constructor(public root:(number|null)[]){
        this.root=root;
    };
    solution(root=this.root,n=root.length){
        const leftChild = (i:number) => (2*i+1)<n ? 2*i+1 : null;
        const rightChild = (i:number) => (2*i+2)<n ? 2*i+2 : null;
        const isLeaf =(i:number) => i<n && root[i]!==null && [leftChild,rightChild].every(fn=>fn(i)===null) 

        const dfs =(node:number|null, depth:number): [number|null, number] => {
            // console.log({node, nodeVal: node!==null ? root[node]: null, depth})
            if (node===null || isLeaf(node)) return [node, depth];
            const [lc,ld] = dfs(leftChild(node), depth+1), [rc,rd] = dfs(rightChild(node),depth+1);
            console.log({nodeI:node, nodeVal: node!==null ? root[node] : null, depth, left: lc!==null ? root[lc]: null,lc,ld, right: rc!==null ? root[rc] : null, rc,rd})
            if (ld>rd) return [lc, ld];
            else if (ld<rd) return [rc, rd];
            return [node, ld];
        };
        return dfs(0, 0)
    }
};

(
    ()=>{
        const Roots = [
            [3,5,1,6,2,0,8,null,null,7,4],
            // [0,1,3,null,2],
            // [1]
        ];
        Roots.forEach(
            root => console.log(`Root=[${root.join(', ')}] Sol=[${new Solve1123(root).solution().join(', ')}]`)
        )
    }
)()
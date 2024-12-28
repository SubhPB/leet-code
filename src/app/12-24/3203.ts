/**
 * 
There exist two undirected trees with n and m nodes, numbered from 0 to n - 1 and from 0 to m - 1, respectively. You are given two 2D integer arrays edges1 and edges2 of lengths n - 1 and m - 1, respectively, where edges1[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the first tree and edges2[i] = [ui, vi] indicates that there is an edge between nodes ui and vi in the second tree.

You must connect one node from the first tree with another node from the second tree with an edge.

Return the minimum possible diameter of the resulting tree.

The diameter of a tree is the length of the longest path between any two nodes in the tree.

 

Example 1:

Input: edges1 = [[0,1],[0,2],[0,3]], edges2 = [[0,1]]

Output: 3

Explanation:

We can obtain a tree of diameter 3 by connecting node 0 from the first tree with any node from the second tree.

Example 2:


Input: edges1 = [[0,1],[0,2],[0,3],[2,4],[2,5],[3,6],[2,7]], edges2 = [[0,1],[0,2],[0,3],[2,4],[2,5],[3,6],[2,7]]

Output: 5

Explanation:

We can obtain a tree of diameter 5 by connecting node 0 from the first tree with node 0 from the second tree.

CMD npx ts-node ./src/app/12-24/3203.ts
 */

function solve3203(edges1:[number, number][], edges2: [number, number][]){
    const constructTree = (edges: typeof edges1) => {
        const tree: {[k:string]:number[]} = {};
        edges.forEach(([parent, child]) => {
            if(!(parent in tree)) tree[parent] = [];
            tree[parent].push(child)
        });
        return tree
    };

    const reverseStr = (str:string) => Array.from(str).reverse().join('')
    const tree1 = constructTree(edges1), tree2 = constructTree(edges2);

    const longestPath = (tree:ReturnType<typeof constructTree>, parent=0) => {
        let longestPath = '';

        const dfs = (node:number, path:string) => {
            const children = node in tree ? tree[node] : [], newpath = path + node;
            if (!children.length && newpath.length > longestPath.length) longestPath = newpath;
            for(let child of children) dfs(child, newpath)
        };
        dfs(parent, '')
        return longestPath
    };

    //Our next task is to find the diameter since we now have longest paths of both trees 
    const [longestPathOfTree1, longestPathOfTree2] = [tree1, tree2].map(tree => longestPath(tree));
    if (longestPathOfTree1[0]!==longestPathOfTree2[0]) return longestPathOfTree1.length > longestPathOfTree2.length ? longestPathOfTree1 : longestPathOfTree2;
    //Joining the parent of both trees, will make sure we do not count parent twice in diameter 
    const diameterOfTree = reverseStr(longestPathOfTree1) + longestPathOfTree2.substring(1);
    return diameterOfTree
}

const EDGES = [
    [
        [[0,1],[0,2],[0,3],[2,4],[2,5],[3,6],[2,7]],
        [[0,1],[0,2],[0,3],[2,4],[2,5],[3,6],[2,7]]
    ],
    [
        [[0,1],[0,2],[0,3]],
        [[0,1]]
    ]
];

EDGES.forEach(([e1, e2]) => console.log(solve3203(e1 as any, e2 as any)))
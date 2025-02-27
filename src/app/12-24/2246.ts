/**
 *  BYIMAAN
 * 
 * 2246. Longest Path With Different Adjacent Characters
You are given a tree (i.e. a connected, undirected graph that has no cycles) rooted at node 0 consisting of n nodes numbered from 0 to n - 1. The tree is represented by a 0-indexed array parent of size n, where parent[i] is the parent of node i. Since node 0 is the root, parent[0] == -1.

You are also given a string s of length n, where s[i] is the character assigned to node i.

Return the length of the longest path in the tree such that no pair of adjacent nodes on the path have the same character assigned to them.


Example 1:

Input: parent = [-1,0,0,1,1,2], s = "abacbe"
Output: 3
Explanation: The longest path where each two adjacent nodes have different characters in the tree is the path: 0 -> 1 -> 3. The length of this path is 3, so 3 is returned.
It can be proven that there is no longer path that satisfies the conditions. 
Example 2:


Input: parent = [-1,0,0,0], s = "aabc"
Output: 3
Explanation: The longest path where each two adjacent nodes have different characters is the path: 2 -> 0 -> 3. The length of this path is 3, so 3 is returned.
 

Constraints:

n == parent.length == s.length
1 <= n <= 105
0 <= parent[i] <= n - 1 for all i >= 1
parent[0] == -1
parent represents a valid tree.
s consists of only lowercase English letters.

CMD npx ts-node ./src/app/12-24/2246.ts
 */

function solve2246(parent:number[], s:string){
    if (parent.length !== s.length) throw new Error(`Invalid value of arguments.`);

    const trackChildren : { [parent:number]: ([number,  string])[] } = {};
    const getChildren = (i:number) => {
        if (i in trackChildren) return trackChildren[i];
        const children: ([number, string])[] = []
        parent.forEach(
            (val, ind) => {
                if (val===i){
                    children.push([ind, s[ind]])
                }
            }
        )
        trackChildren[i] = children;
        return children
    };

    let longestPath = '';

    const solve = (i:number) => {
        const paths :string[] = []

        const traverse = (node:number, nodeName:string, path:string) => {
            const children = getChildren(node);
            if (!children.length || children.every(([childInd, childName]) => nodeName === childName)){
                const newPath = path + nodeName;
                paths.push(newPath)
            };
            
            for(let [childInd, childName] of children){
                if (childName === nodeName){
                    solve(childInd)
                } else {
                    traverse(childInd, childName, path + nodeName)
                }
            }
        };

        traverse(i, s[i], '')
        
        //We need at most 2 longest paths exist from a node;
        const atMost2LongestPaths = paths.sort((a, b) => b.length - a.length).slice(0,2); 
        let localLongestPath = '';
        if (atMost2LongestPaths.length === 1){
            localLongestPath = atMost2LongestPaths[0]
        } else {
            atMost2LongestPaths[0] = Array.from(atMost2LongestPaths[0]).reverse().join('');
            localLongestPath = atMost2LongestPaths.join('').replace(`${s[i]}${s[i]}`, s[i])
        };

        if (localLongestPath.length > longestPath.length) longestPath = localLongestPath
    };

    solve(0)
    return longestPath
}

function anotherApproach2246(parent:number[], s:string){
    let longest = '';

    const graph: {[key:number]:number[]} = {};
    const reverseString = (str:string) => Array.from(str).reverse().join('')
    parent.forEach( (parent, node) => parent in graph ? graph[parent].push(node) : graph[parent] = [node]);
    
    const solve = (node:number) => {
        const children = node in graph ? graph[node] : [];
        const longestPaths:string[] = ['', ''];
        for(let child of children){
            longestPaths.push(
                dfs(child)
            )
        };
        longestPaths.sort((a,b) => b.length - a.length);
        console.log({node, longestPaths})
        const jointPath = reverseString(longestPaths[0]) + s[node] + longestPaths[1];
        if (jointPath.length > longest.length) longest = jointPath;
    }
    const dfs = (node:number) => {
        let longestPathFromThisNode = '';
        
        const rec = (i:number, traversedPath:string) => {
            const children = i in graph ? graph[i] : [];
            const nodeName = s[i];
            
            let baseCase = 0;
            for(let child of children){
                const childName = s[child];
                if (childName === nodeName){
                    solve(child)
                    baseCase++
                } else {
                    rec(child, traversedPath + childName)
                }
            };
            if (baseCase === children.length && traversedPath.length > longestPathFromThisNode.length){
                longestPathFromThisNode = traversedPath
            }
        };
        rec(node, s[node])
        return longestPathFromThisNode
    };

    solve(0)
    return longest
}

[ 
    [[-1,0,0,1,1,2], "abacbe"],
    [[-1,0,0,0], "aabc"]
].forEach(
    ([parent, s]) => {
        console.log(anotherApproach2246(parent as number[], s as string))
    }
)

/**
 * 684. Redundant Connection

In this problem, a tree is an undirected graph that is connected and has no cycles.

You are given a graph that started as a tree with n nodes labeled from 1 to n, with one additional edge added. The added edge has two different vertices chosen from 1 to n, and was not an edge that already existed. The graph is represented as an array edges of length n where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the graph.

Return an edge that can be removed so that the resulting graph is a tree of n nodes. If there are multiple answers, return the answer that occurs last in the input.

Example 1:

Input: edges = [[1,2],[1,3],[2,3]]
Output: [2,3]
Example 2:

Input: edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]
Output: [1,4]

npx ts-node ./src/app/2025/Feb/684.ts
 */

class Solve684{
    constructor(public Edges:[number,number][]){ this.Edges=Edges; };
    solution1(edges=this.Edges){
        /**According to problem statement, we can assume that initial graph was a tree,
         * But then after making an additional edge b/w two nodes, it is no longer a tree.
         * Our task is to find that edge/(any edge whose deletion would result back into tree) and simply return it
         */
        const parentMap:{[node:string]:number/**nodeParent*/} = {}
        for(let [parent,newNode] of edges){
            if (newNode in parentMap && parentMap[newNode] !== parent) return [parent,newNode];
            parentMap[newNode] = parent;
        };
        return -1;
    };
    solution2(edges=this.Edges){
        /**Solution based on union sets approach*/
        const parent = Array.from({length:edges.length+1}, (_,i)=>i);
        const rank = Array.from(parent, ()=>1);

        const find = (n:number) => { 
            /**Not only find the rootParent of the component but also update the rootParent*/
            if (parent[n]!==n) parent[n] = find(parent[n]);
            return parent[n]
        };

        const union = (n1:number,n2:number) => {
            const [p1, p2] = [n1,n2].map(find);
            if (p1===p2) return false;
            if (rank[p1]>rank[p2]){
                parent[p2] = p1;
                rank[p2] += rank[p2];
            } else {
                parent[p1] = p2;
                rank[p1] += rank[p1];
            };
            return true;
        }
        
        for(let i=0;i<edges.length; i++){
            if (!(union(...edges[i]))){
                console.log({parent})
                return edges[i]
            }
        }
        return -1
    };
    solution3(edges=this.Edges){
        /**This is also based on union find approach, but will try to reduce the space-complexity to O(n)*/
        const parent = Array.from({length:edges.length+1}, ()=>-1); //if -ve means it's a root and number represents the size of this union-set
        const findParent = (n:number) => {
            if (parent[n]<0){/**Is it a root?*/
                return n
            } else {
                parent[n] = findParent(parent[n])
                return parent[n]
            }
        };
        const setSize = (n:number) => {
            if (parent[n]>0) throw new Error(`Root of a component is expected to be in -ve value but found ${parent[n]}`);
            return -parent[n]
        };
        const union = (n1:number, n2:number) => {
            const [p1,p2] = [n1,n2].map(findParent);
            if (p1===p2) return false;
            if (setSize(p1)>setSize(p2)){
                parent[p2] = p1;
                parent[p1] -= setSize(parent[p2]) //Size of p2 is been merged into p1
            } else {
                parent[p1] = p2;
                parent[p2] -= setSize(parent[p1])
            };
            return true
        };
        for(let edge of edges){
            if (!(union(...edge))) return edge
        };
        return -1
    }
};

(
    ()=>{
        const ARGS: ([number,number][])[] = [
            [[1,2],[1,3],[2,3]],
            [[1,2],[2,3],[3,4],[1,4],[1,5]]
        ];
        ARGS.forEach(edges => console.log(`Edges=[${edges.map(e=>e.join('->')).join(', ')}] solution = {${ new Solve684(edges).solution3() }}`))
    }
)()


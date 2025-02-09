/**
 * 1514. Path with Maximum Probability
You are given an undirected weighted graph of n nodes (0-indexed), represented by an edge list where edges[i] = [a, b] is an undirected edge connecting the nodes a and b with a probability of success of traversing that edge succProb[i].

Given two nodes start and end, find the path with the maximum probability of success to go from start to end and return its success probability.

If there is no path from start to end, return 0. Your answer will be accepted if it differs from the correct answer by at most 1e-5.

Example 1:

Input: n = 3, edges = [[0,1],[1,2],[0,2]], succProb = [0.5,0.5,0.2], start = 0, end = 2
Output: 0.25000
Explanation: There are two paths from start to end, one having a probability of success = 0.2 and the other has 0.5 * 0.5 = 0.25.
Example 2:



Input: n = 3, edges = [[0,1],[1,2],[0,2]], succProb = [0.5,0.5,0.3], start = 0, end = 2
Output: 0.30000
Example 3:



Input: n = 3, edges = [[0,1]], succProb = [0.5], start = 0, end = 2
Output: 0.00000
Explanation: There is no path between 0 and 2.

CMD npx ts-node ./src/app/2025/Jan/1514.ts
 
 */

class MaxHeap1514<NodeVal=null>{
    private heapArr :([number, NodeVal])[] = [];
    constructor(arr:number[]|[number,NodeVal][]=[]){
        arr.forEach(v=>Array.isArray(v)?this.insert(v[0], v[1]):this.insert(v,null as NodeVal))
    };
    size(){
        return this.heapArr.length
    };
    parentIndex = {
        of:(childIndex:number)=>{
            if(childIndex<=0) return null;
            if(childIndex>=this.size()) throw new Error(`Child index does not exist expected [0, ${this.size()}) but found ${childIndex}`)
            return Math.floor( (childIndex-1)/2 )
        }
    };
    childIndex = {
        of: (parentIndex:number) => {
            if (parentIndex<0) throw new Error(`Invalid parent index expected to be at least 0 but found ${parentIndex}`)
            return {
                left: (2*parentIndex+1) >= this.size() ? null : 2*parentIndex+1,
                right: (2*parentIndex+2) >= this.size() ? null : 2*parentIndex+2 
            }
        }
    };
    insert(node:number,val:NodeVal){
        this.heapArr.push([node,val]);
        let  nodeIndex = this.size() - 1, nodeParentIndex = this.parentIndex.of(nodeIndex);
        while(
            nodeParentIndex!==null
                &&this.heapArr[nodeIndex][0]>this.heapArr[nodeParentIndex][0]
        ){
            [
                this.heapArr[nodeParentIndex], this.heapArr[nodeIndex]
            ] = [
                this.heapArr[nodeIndex], this.heapArr[nodeParentIndex]
            ];
            nodeIndex = nodeParentIndex;
            nodeParentIndex = this.parentIndex.of(nodeIndex);
        };
    };
    delete(node:number){
        let nodeIndex:number|null = null
        for(let i=0; i<this.size(); i++) if (this.heapArr[i][0]===node){
            nodeIndex=i; break;
        };
        if (nodeIndex!==null){
            if (this.size()===1) this.heapArr = [];
            else {
                this.heapArr[nodeIndex] = this.heapArr[this.size()-1];
                this.heapArr.pop();
                let newParentIndex = nodeIndex, childIndexes = () => this.childIndex.of(newParentIndex);
                while(
                    Object.values(childIndexes()).some(
                        childIndex=> childIndex!==null&&this.heapArr[childIndex][0]>this.heapArr[newParentIndex][0]
                    )
                ){
                    const {left:leftChildIndex, right:rightChildIndex} = childIndexes();
                    let swapIndex:number|null = null;
                    if(leftChildIndex!==null&&this.heapArr[leftChildIndex][0]>this.heapArr[newParentIndex][0]) swapIndex = leftChildIndex;
                    else if (rightChildIndex!==null&&this.heapArr[rightChildIndex][0]>this.heapArr[newParentIndex][0]) swapIndex = rightChildIndex;
                    if (swapIndex===null) throw new Error(`Programmer logic error there should be no chance of swapIndex to be null`);
                    [
                        this.heapArr[swapIndex], this.heapArr[newParentIndex]
                    ] = [
                        this.heapArr[newParentIndex],
                        this.heapArr[swapIndex]
                    ];
                    newParentIndex = swapIndex;
                }
            }
        };
    };
    root(){
        return this.size()>0 ? this.heapArr[0] : null
    };
    unshift(){
        const root = this.root();
        this.delete(0);
        return root
    }
}

class Solve1514{
    constructor(public n:number, public edges: [number, number][], public succProb:number[], public start:number, public end:number){
        this.n=n; this.edges=edges; this.succProb=succProb; this.start=start; this.end=end
    };
    solution1(){
        const Map: {[k:number]:[number /**NodeNext */, number /**succProb */][]} = {};
        for(let i=0; i<this.edges.length; i++){
            const [node, nodeNext] = this.edges[i];
            if (!(node in Map)) Map[node] = [];
            Map[node].push([nodeNext, this.succProb[i]])
        };
    }
};

(
    ()=>{
        const ARGS: ConstructorParameters<typeof Solve1514>[] = [
            [ 3, [[0,1],[1,2],[0,2]], [0.5,0.5,0.2], 0, 2],
            [3, [[0,1]], [0.5], 0, 2]
        ];
        ARGS.forEach(
            arg => console.log(`sol -> ${new Solve1514(...arg).solution1()}`)
        )
    }
)();
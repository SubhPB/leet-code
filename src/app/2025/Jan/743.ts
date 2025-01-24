/**
 * 743. Network Delay Time

You are given a network of n nodes, labeled from 1 to n. You are also given times,
a list of travel times as directed edges times[i] = (ui, vi, wi), where ui is the source node,
vi is the target node, and wi is the time it takes for a signal to travel from source to target.

We will send a signal from a given node k. Return the minimum time it takes for all the n nodes to receive the signal.
If it is impossible for all the n nodes to receive the signal, return -1.

Example 1:
Input: times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
Output: 2
Example 2:

Input: times = [[1,2,1]], n = 2, k = 1
Output: 1
Example 3:

Input: times = [[1,2,1]], n = 2, k = 2
Output: -1
 */

class Solve743{
    constructor(public times:[number,number,number][], public n:number, public k:number){
        this.times=times; this.n=n; this.k=k;
    };
    createNetwork(){
        const n:{[k:number]:[
            number, //neighbor
            number //neighbor-distance
        ][]}={}
        for(let [from, to, dist] of this.times){
            if(!(from in n)) n[from] = [];
            n[from].push([to, dist])
        };
        return n
    };
    solution1(){
        const network = this.createNetwork();
        const traversing = [this.k], kMap = {[this.k]:0 /** k -to-> k should be zero */};
        const traversed: number[] = [];

        let minimumDelay = -1;
        
        while(!!traversing.length){
            const node = traversing.pop() as number;
            for(let [neighbor, neighborDist] of (node in network ? network[node] : [])){
                if (
                    (kMap[node]+neighborDist)<(neighbor in kMap ? kMap[neighbor] : Infinity)
                ) kMap[neighbor] = kMap[node]+neighborDist;
                if (kMap[neighbor]>minimumDelay) minimumDelay = kMap[neighbor]
            };
            traversed.push(node);
            //Need to select next node
            const nextNode = parseInt(Object.keys(kMap).filter(
                k=>!traversed.includes(parseInt(k))
            ).sort((a,b)=>parseInt(a)-parseInt(b))[0]);
            if (Number.isInteger(nextNode)) traversing.push(nextNode)
        };
        return minimumDelay
    }
    
}
(
    ()=>{
        const ARGS = [
            [[[2,1,1],[2,3,1],[3,4,1]], 4, 2],
            [[[1,2,1]], 2, 1],
            [[[1,2,1]], 2, 2]
        ] as ([[number, number, number][], number, number])[]
        ARGS.forEach(([times, n, k])=>{
            console.log(`Times ${JSON.stringify(times)} n=${n} k=${k} Sol-> ${new Solve743(times, n, k).solution1()}`)
        })
    }
)()
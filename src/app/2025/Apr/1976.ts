/**
 * 1976. Number of Ways to Arrive at Destination
You are in a city that consists of n intersections numbered from 0 to n - 1 with bi-directional roads between some intersections. The inputs are generated such that you can reach any intersection from any other intersection and that there is at most one road between any two intersections.
You are given an integer n and a 2D integer array roads where roads[i] = [ui, vi, timei] means that there is a road between intersections ui and vi that takes timei minutes to travel. You want to know in how many ways you can travel from intersection 0 to intersection n - 1 in the shortest amount of time.
Return the number of ways you can arrive at your destination in the shortest amount of time. Since the answer may be large, return it modulo 109 + 7.

Example 1:

Input: n = 7, roads = [[0,6,7],[0,1,2],[1,2,3],[1,3,3],[6,3,3],[3,5,1],[6,5,1],[2,5,1],[0,4,5],[4,6,2]]
Output: 4
Explanation: The shortest amount of time it takes to go from intersection 0 to intersection 6 is 7 minutes.
The four ways to get there in 7 minutes are:
- 0 ➝ 6
- 0 ➝ 4 ➝ 6
- 0 ➝ 1 ➝ 2 ➝ 5 ➝ 6
- 0 ➝ 1 ➝ 3 ➝ 5 ➝ 6
Example 2:

Input: n = 2, roads = [[1,0,10]]
Output: 1
Explanation: There is only one way to go from intersection 0 to intersection 1, and it takes 10 minutes.

npx ts-node ./src/app/2025/Apr/1976.ts
 */

class Solve1976{
    constructor(public n:number,public roads:number[][]){
        this.n=n; this.roads=roads;
    };
    solution(n=this.n,roads=this.roads){
        let count = 0, minTime = Infinity;
        const graph:{[k:string]:[number,number][]} = {};
        for(let [u,v,t] of roads) {
            [u,v].forEach(c=>{
                if (!(c in graph)) graph[c] = [];
            });
            graph[u].push([v,t]);
            graph[v].push([u,t]);
        };
        const queue: [number,number,number][] = [[1,0,0]];
        while(queue.length){
            const [mask, currCity, currTime] = queue.pop()!;
            if (currTime<=minTime){
                if (currCity===n-1){ //Destination found
                    if (minTime>currTime){
                        minTime = currTime;
                        count=0
                    };
                    count++;
                } else { //Keep traversing 
                    for(let [nextCity, nextTime] of graph[currCity]){
                        if (mask & 1<<nextCity) continue;
                        const newMask = mask | (1 << currCity), newTime = currTime + nextTime;
                        queue.push([newMask, nextCity, newTime])
                    };
                }
            };
        };
        return count;
    };
    solution2(n=this.n, roads=this.roads){
        let minTime = Infinity, count = 0;
        const traversed = Array(n).fill(false);
        const cost = Array.from({length:n}, (_,i)=> i!==0 ? Infinity : 0);

        class PQ {
            public arr:number[];
            constructor(arr:number[]){this.arr=arr}
            push(val:number){
                this.arr.push(val);
                this.arr.sort( (cityA,cityB) => cost[cityB] - cost[cityA] );
            };
            get len() {
                return this.arr.length
            };
            pop(){
                return this.arr.pop();
            };
        };

        const graph:{[k:string]:[number,number][]} = {};
        for(let [u,v,t] of roads) {
            [u,v].forEach(c=>{
                if (!(c in graph)) graph[c] = [];
            });
            graph[u].push([v,t]);
            graph[v].push([u,t]);
        };

        const pq = new PQ([0]);
        // console.log('Graph = %O', graph)
        while(pq.len){
            // console.log('Before %O', {traversed, cost, pq: pq.arr, count, minTime})
            const city = pq.pop()!, cityCost = cost[city];
            if (city===(n-1)){
                if (cityCost<=minTime){
                    if (minTime>cityCost){
                        minTime = cityCost;
                        count=0
                    };
                    count++;
                }
            };

            if (traversed[city]) continue;

            if (city in graph){
                for(let [nextCity, nextTime] of graph[city]){
                    if ( cost[nextCity] > (cityCost + nextTime) ){
                        cost[nextCity] = cityCost + nextTime
                    };
                    if (cost[nextCity]<=minTime && !traversed[nextCity]) pq.push(nextCity);
                }
            };
            traversed[city]=true;
        };
        return count
    }
};

(
    ()=>{
        const ARGS: [number,number[][]][] = [
            [7, [[0,6,7],[0,1,2],[1,2,3],[1,3,3],[6,3,3],[3,5,1],[6,5,1],[2,5,1],[0,4,5],[4,6,2]]],
            // [2, [[1,0,10]]]
        ];
        ARGS.forEach(([n,roads]) => {
            const sol = new Solve1976(n,roads)
            console.log(`N=${n}, sol1=${sol.solution()}, sol2=${sol.solution2()}`)
        })
    }
)()

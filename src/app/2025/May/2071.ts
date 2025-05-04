/**
 * 2071. Maximum Number of Tasks You Can Assign
You have n tasks and m workers. Each task has a strength requirement stored in a 0-indexed integer array tasks, with the ith task requiring tasks[i] strength to complete. The strength of each worker is stored in a 0-indexed integer array workers, with the jth worker having workers[j] strength. Each worker can only be assigned to a single task and must have a strength greater than or equal to the task's strength requirement (i.e., workers[j] >= tasks[i]).

Additionally, you have pills magical pills that will increase a worker's strength by strength. You can decide which workers receive the magical pills, however, you may only give each worker at most one magical pill.

Given the 0-indexed integer arrays tasks and workers and the integers pills and strength, return the maximum number of tasks that can be completed.

Example 1:

Input: tasks = [3,2,1], workers = [0,3,3], pills = 1, strength = 1
Output: 3
Explanation:
We can assign the magical pill and tasks as follows:
- Give the magical pill to worker 0.
- Assign worker 0 to task 2 (0 + 1 >= 1)
- Assign worker 1 to task 1 (3 >= 2)
- Assign worker 2 to task 0 (3 >= 3)
Example 2:

Input: tasks = [5,4], workers = [0,0,0], pills = 1, strength = 5
Output: 1
Explanation:
We can assign the magical pill and tasks as follows:
- Give the magical pill to worker 0.
- Assign worker 0 to task 0 (0 + 5 >= 5)
Example 3:

Input: tasks = [10,15,30], workers = [0,10,10,10,10], pills = 3, strength = 10
Output: 2
Explanation:
We can assign the magical pills and tasks as follows:
- Give the magical pill to worker 0 and worker 1.
- Assign worker 0 to task 0 (0 + 10 >= 10)
- Assign worker 1 to task 1 (10 + 10 >= 15)
The last pill is not given because it will not make any worker strong enough for the last task.

Constraints:

n == tasks.length
m == workers.length
1 <= n, m <= 5 * 104
0 <= pills <= m
0 <= tasks[i], workers[j], strength <= 109

npx ts-node ./src/app/2025/May/2071.ts
 */

class Solve2071{
    constructor(
        public tasks:number[], public workers:number[], public pills:number, public strength:number
    ){
        this.tasks = tasks; this.workers = workers;
        this.pills = pills; this.strength = strength
    };
    solution(
        tasks=this.tasks, workers=this.workers, pills=this.pills, strength=this.strength
    ){
        const n = tasks.length, m = workers.length;

        const sortedTasks = tasks.sort((a,b)=>a-b);
        const sortedWorkers = workers.sort((a,b)=>b-a);
        let needToSortWorkers = false;

        const canAssign = (cnt:number) => {
            if ([m,n].every(l=>cnt>=0&&cnt<=l)){
                /**
                 * Process:-
                 * 1) Assign strongest worker the hardest task (within cnt range)
                 * 2) If pill needed, elect optimal worker to use pill wisely.
                 * 3) If can't do any task in within range then return false immediately 
                 */
                if (needToSortWorkers) sortedWorkers.sort((a,b) => b-a)
                let pillsCnt = pills;
                for(let i=0; i<cnt; i++){
                    const suppl = strength * Math.min(1, pillsCnt);
                    const task = sortedTasks[cnt-i-1];

                    if (sortedWorkers[i] + suppl >= task){

                        if (sortedWorkers[i] < task){ //Does pill needed?
                            //Need to elect most optimal worker
                            let l = i, r = cnt-1;
                            while(l<r){
                                let candid = Math.ceil( (l+r)/2 );
                                if (
                                    sortedWorkers[candid] + suppl >= task
                                ){ //A weak worker is found, capable to complete this task
                                    l=candid;
                                } else {
                                    r=candid-1;
                                }
                            };
                            //So now sortedWorker['l'] is most optimal candidate to elect
                            if (i!==l){
                                needToSortWorkers = true;
                                while(i!==l){
                                    [sortedWorkers[l-1], sortedWorkers[l]] = [sortedWorkers[l], sortedWorkers[l-1]];
                                    l-=1
                                }
                            };
                            pillsCnt -= 1; //pillUsed
                        };

                    } else {
                        return false
                    }
                };
                return true
            }
            return false
        }

        let l=0, r=n;
        while(l<r){
            const cnt = Math.ceil(
                (l+r)/2 //Not using floor because [cnt=0] is always a 'true' answer
            );
            if (canAssign(cnt)){
                l=cnt;
            } else {
                r=cnt-1;
            }
        }
        return l
    }
};

(
    ()=>{
        const ARGS: [number[],number[],number,number][] = [
            [[3,2,1], [0,3,3], 1, 1],
            [[5,4], [0,0,0], 1, 5],
            [[5,9,8,5,9], [1,6,4,2,6], 1, 5]
        ];

        ARGS.forEach(
            ([tasks,workers,pills,strength]) => {
                const sol = new Solve2071(tasks,workers,pills,strength);
                const toStr = (arr:number[]) => `[${arr.join(',')}]`
                console.log(
                    `Tasks = ${toStr(tasks)} \n`
                    + `Workers = ${toStr(workers)} \n`
                    + `Pills = ${pills} \n`
                    + `Strength = ${strength} \n`
                    + `Max-Tasks(1) = ${sol.solution()} \n`
                )
            }
        )
    }
)()
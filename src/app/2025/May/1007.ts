/**
 * 1007. Minimum Domino Rotations For Equal Row

In a row of dominoes, tops[i] and bottoms[i] represent the top and bottom halves of the ith domino. (A domino is a tile with two numbers from 1 to 6 - one on each half of the tile.)

We may rotate the ith domino, so that tops[i] and bottoms[i] swap values.

Return the minimum number of rotations so that all the values in tops are the same, or all the values in bottoms are the same.

If it cannot be done, return -1.

Example 1:

Input: tops = [2,1,2,4,2,2], bottoms = [5,2,6,2,3,2]
Output: 2
Explanation: 
The first figure represents the dominoes as given by tops and bottoms: before we do any rotations.
If we rotate the second and fourth dominoes, we can make every value in the top row equal to 2, as indicated by the second figure.
Example 2:

Input: tops = [3,5,1,2,3], bottoms = [3,6,3,3,4]
Output: -1
Explanation: 
In this case, it is not possible to rotate the dominoes to make one row of values equal.
 
npx ts-node ./src/app/2025/May/1007.ts
 */

class Solve1007{
    constructor(public tops:number[], public bottoms:number[]){
        this.tops=tops; this.bottoms=bottoms
    };
    solution(tops=this.tops, bottoms=this.bottoms){
    
        const fn = (tops:number[], bottoms:number[]) => {
            const get = (i:number) => [tops[i], bottoms[i]];
            const [top, btm] = get(0);
            let topCnt = 0, nonTopCnt = 0;
            if (top!==btm) topCnt+=1;
            for(let i=1; i<tops.length; i++){
                const temp = get(i);
                if (temp.includes(top)){
                    if (temp[0]!==temp[1]){
                        top === temp[0] ? topCnt+=1 : nonTopCnt += 1
                    }
                } else {
                    return Infinity;
                }
            };
            return Math.min(topCnt, nonTopCnt)
        };
        const mins = [fn(tops, bottoms), fn(bottoms, tops)].filter(min => min!==Infinity);
        console.log({min1: fn(tops, bottoms), min2: fn(bottoms, tops)})
        return mins.length ? Math.min(...mins) : -1
    };
};

(
    ()=>{
        const ARGS = [
            [[2,1,2,4,2,2], [5,2,6,2,3,2]],
            [[3,5,1,2,3], [3,6,3,3,4]],
            [[2,1,1,3,2,1,2,2,1], [3,2,3,1,3,2,3,3,2]]
        ];
        ARGS.forEach(
            ([tops, bottoms]) => {
                const sol = new Solve1007(tops,bottoms);
                console.log(
                    `Tops=[${tops.join(',')}] \n`
                    + `Bottoms=[${bottoms.join(',')}] \n`
                    + `RotateCnt = ${sol.solution()}`
                )
            }
        )
    }
)()
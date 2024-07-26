/**
 * Byimaan
 * You are given an array of non-negative integers representing an elevation map where the width of each bar is 1 unit. You need to compute how much water it can trap after raining.
 * 
 * CMD :- npx ts-node ./src/app/7-24/water-trap.ts
 */

const Height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1];

function countWaterTrap(heights= Height){

    const nearestGreatestToRight = (index: number) => {
        let heightest = heights[index];

        for(let i = index+1; i < heights.length; i++){
            if (heights[i] >= heightest){
                return i
            }
        }
        return null
    };
    
    
    const greatestToRight = (index: number) => {
        let max = 0
        for(let i = index+1; i < heights.length; i++){
            if (heights[i] >= heights[max]){
                max = i
            }
        };
        return max
    };


    const calc = (i: number, j: number) => {
        let height = Math.min(heights[i], heights[j]);
        let width = j - (i-1);
        let substract = heights.slice(i, j+1).reduce(
            (acc, val) => val > height ? acc+height : acc+val, 0
        );
        const res =  height*width - substract;
        return res > 0 ? res : 0
    }

    let count = 0;


    let i = 0

    while (i < heights.length-1){
        const NGR = nearestGreatestToRight(i);
        if (NGR !== null && NGR !== i){
            count += calc(i, NGR)
            console.log("calc = ",calc(i, NGR))
            i = NGR;
        } else {
            const GTR = greatestToRight(i);
            count += calc(i, GTR)
            i = GTR
        };
    };

    console.log(count)
    return count
};

countWaterTrap();



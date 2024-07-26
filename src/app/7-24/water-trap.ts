/**
 * Byimaan
 * You are given an array of non-negative integers representing an elevation map where the width of each bar is 1 unit. You need to compute how much water it can trap after raining.
 * 
 * CMD :- npx ts-node ./src/app/7-24/water-trap.ts
 */

const Height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1];

// function countWaterTrap(heights= Height){

//     const nearestGreatestToRight = (index: number) => {
//         let heightest = heights[index];

//         for(let i = index+1; i < heights.length; i++){
//             if (heights[i] >= heightest){
//                 return i
//             }
//         }
//         return null
//     };
    
    
//     const greatestToRight = (index: number) => {
//         let max = 0
//         for(let i = index+1; i < heights.length; i++){
//             if (heights[i] >= heights[max]){
//                 max = i
//             }
//         };
//         return max
//     };


//     const calc = (i: number, j: number) => {
//         let height = Math.min(heights[i], heights[j]);
//         let width = j - (i-1);
//         let substract = heights.slice(i, j+1).reduce(
//             (acc, val) => val > height ? acc+height : acc+val, 0
//         );
//         const res =  height*width - substract;
//         return res > 0 ? res : 0
//     }

//     let count = 0;


//     let i = 0

//     while (i < heights.length-1){
//         const NGR = nearestGreatestToRight(i);
//         if (NGR !== null && NGR !== i){
//             count += calc(i, NGR)
//             console.log("calc = ",calc(i, NGR))
//             i = NGR;
//         } else {
//             const GTR = greatestToRight(i);
//             count += calc(i, GTR)
//             i = GTR
//         };
//     };

//     console.log(count)
//     return count
// };


function countWater(heights=Height){
    
    // this will return the index of nearest greatest height else null
    const nearestGreatestToRight = (index: number, height=Height) =>{
        for(let i = index+1; i < height.length; i++){
            if (height[i] >= height[index]){
                return i
            }
        }
        return null
    };

    let count = 0;


    const solve = (heightArray: number[]) => {
        const stack = [0];
        while (stack.length !== 0){
            const index = stack.pop() as number;
            const ngr = nearestGreatestToRight(index, heightArray);
            if (ngr){
                stack.push(ngr);
                const calc = {
                    height: Math.min(heightArray[index], heightArray[ngr]),
                    width: ngr - (index - 1)
                }
                const area = (calc.height * calc.width) - heightArray.slice(index, ngr+1).reduce(
                    (acc, val) => val <= calc.height ? val+acc : acc+calc.height,0
                );
                count += (area > 0 ? area : 0)
            } else {
                return index
            }
        }
    };

    const index = solve(Height);
    console.log("The value of count & index after one call ", count, index)
    if (index){
        const leftToRightHeight = Height.slice(index).reverse()
        solve(leftToRightHeight)
    };
    return count
}

console.log(countWater())

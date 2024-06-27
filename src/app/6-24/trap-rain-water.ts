// Byimaan

/**
 * Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.

 * CMD npx ts-node ./src/app/6-24/trap-rain-water.ts
 */

const height = [0,1,0,2,1,0,1,3,2,1,2,1];

const trapWater = () => {

    const heightestFromLeft = (index: number) => {
        return height.slice(0, index).reduce((acc, val) => acc > val ? acc : val, 0) || 0;
    };

    
    const heightestFromRight = (index: number) => {
        return height.slice(index+1).reduce((acc, val) => acc > val ? acc : val, 0) || 0;
    };

    const recordWater = Array(height.length).fill(null)

    for(let i=0; i< height.length; i++){
        const smallestBar = Math.min(heightestFromLeft(i), heightestFromRight(i));
        const waterTrappedOnTop = smallestBar - height[i] 
        recordWater[i] = waterTrappedOnTop > 0 ? waterTrappedOnTop : 0
    };
    return recordWater.reduce((acc,val) => acc+val,0)
};

console.log(trapWater())
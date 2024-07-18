// BYIMAAN

/**
 * CMD npx ts-node ./src/app/7-24/mcm.ts
 */

const MCM = (array=[40, 20, 30, 10, 30]) => {

    let minMul = Infinity;

    const rec = (arr: number[]): number => {
        if (arr.length === 3){
            const val =  arr[0] * arr[1] * arr[2]
            console.log(val)
            if (val < minMul){
                minMul = val
            }
            return val
        } else {
            for(let i = 1; i < arr.length - 1; i ++){
    
                return arr[i-1]*arr[i]*arr[i+1] + rec(arr.slice(0, i).concat(arr.slice(i+1)))
            }
        };
        return minMul
    };


    return rec(array)

};

console.log(MCM())
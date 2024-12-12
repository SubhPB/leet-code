/**
 * Byimaan
 * 
 * CMD npx ts-node ./src/app/12-24/tower-of-honoi.ts
 */

const towerOfHanoi = (discs:number) => {
    const pr = (start:number, end:number) => console.log(` ${start} --> ${end}`);
    
    const hanoi = (n:number, start:number, end:number) => {
        if (n===1){
            pr(start, end)
        } else {
            const other = 6 - (start+end);
            hanoi(n-1, start, other)
            pr(start, end)
            hanoi(n-1, other, end)
        }
    };
    hanoi(discs, 0, 3)
}

console.log(towerOfHanoi(3))
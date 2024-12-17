/**
 * Byimaan
 * 
 * CMD npx ts-node ./src/app/12-24/tower-of-honoi.ts
 */
const pr = (start:number, end:number) => console.log(` ${start} --> ${end}`);

const towerOfHanoi = (discs:number, start=1, end=3) => {
    if ([start, end].some(a => a > 3 || a <= 0) || discs < 1) return;
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
    hanoi(discs, start, end)
}

/**
 * Problem variation:-
 * Find the shortest sequence of moves that transfers a tower of n disks
 from the left peg A to the right peg B, if direct moves between A and B
 are disallowed. (Each move must be to or from the middle peg. As usual,
 a larger disk must never appear above a smaller one.) 
 */
const towerOfHanoi2 = (discs:number) => {
    const hanoi = (n:number, start:number, end:number) => {
        const other = 6 - (start+end);
        if (n===1){
            pr(start, other);
            pr(other, end)
        } else {
            hanoi(n-1, start, end);
            pr(start, other);
            towerOfHanoi(n-1, end, other);
            pr(other, end);
            towerOfHanoi(n-1, start, end)
        }
    };
    hanoi(discs, 1, 3)
}

console.log(towerOfHanoi(3))
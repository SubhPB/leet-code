/**Byimaan
 * 
 * CMD npx ts-node ./src/app/12-24/josephus.ts
 */

// Most simplest solution to be done by pure mathematics
const Josephus = (n:number) :number => {
    if ([1, 2].includes(n)) return 1;
    if (n<=0) return 0;
    /**
     * Mathematical recurrence relation
    *       When `n` is even --> J(2n) = 2*J(n) - 1
    *       When `n` is odd --> J(2n+1) = 2*J(n) + 1
     */
    return Josephus(Math.floor(n/2)) + (-1)**(n+1)
};

// Solution with O(1) complexity
const JosephusO1 = (n:number, startingPos=1) => {
    /** n = 2**M + L;
     * J(n) = 2*L + 1
     * We saw a binary pattern in our problem, According to that we need to follow these steps:-
     *      1) Delete the most significant, by which you will get the leftover.
     *      2) Now doubles the leftover
     *      3) Add one to this result by which we will get the final answer
     * All these are super easy to perform in binary
     */
    if (n <= 0) return 0;
    if (startingPos > n || startingPos <= 0){
        throw new Error(`Invalid starting position expected [1, ${n}] but found ${startingPos}`)
    };
    
    const binary = String(n.toString(2)),
        leftover = binary.substring(1);
    const winningPosition = parseInt(leftover + '1', 2);

    const rotation = 1 - startingPos; // [-(n-1), 0] 
    const winnerAfterRotation = (winningPosition - rotation) % n
    return winnerAfterRotation === 0 ? n  : winnerAfterRotation
}

Array.from({length:20}, (_, i) => i + 1).forEach(
    n => console.log(`When n = ${n} then J(n) = ${Josephus(n)}`)
)
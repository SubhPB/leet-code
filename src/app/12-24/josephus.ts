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
}

Array.from({length:20}, (_, i) => i + 1).forEach(
    n => console.log(`When n = ${n} then J(n) = ${Josephus(n)}`)
)
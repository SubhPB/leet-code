/**
 * Leetcode 1653
 * You have a bomb to defuse, and your time is running out! Your informer will provide you with a circular array code of length of n and a key k.

To decrypt the code, you must replace every number. All the numbers are replaced simultaneously.

If k > 0, replace the ith number with the sum of the next k numbers.
If k < 0, replace the ith number with the sum of the previous k numbers.
If k == 0, replace the ith number with 0.
As code is circular, the next element of code[n-1] is code[0], and the previous element of code[0] is code[n-1].

Given the circular array code and an integer key k, return the decrypted code to defuse the bomb!

 

Example 1:

Input: code = [5,7,1,4], k = 3
Output: [12,10,16,13]
Explanation: Each number is replaced by the sum of the next 3 numbers. The decrypted code is [7+1+4, 1+4+5, 4+5+7, 5+7+1]. Notice that the numbers wrap around.
Example 2:

Input: code = [1,2,3,4], k = 0
Output: [0,0,0,0]
Explanation: When k is zero, the numbers are replaced by 0. 
Example 3:

Input: code = [2,4,9,3], k = -2
Output: [12,5,6,13]
Explanation: The decrypted code is [3+9, 2+3, 4+2, 9+4]. Notice that the numbers wrap around again. If k is negative, the sum is of the previous numbers.

CMD :- npx ts-node ./src/app/11-24/dtb-1652.ts
*/

//To go back and forth
const move = {
    next: (i:number, n:number) => (i+1)%n,
    prev:(i:number, n:number) => (n+i-1)%n
};

const mod = (a:number) => a >= 0 ? a : -a;

const calcSum = (currIndex: number, k: number, code: number[]) => {
    if (k===0) return 0;
    const moveIndex = k > 0 ? move.next : move.prev;

    const solve = (index:number, iteration:number/** iteration should always positive */): number => {
        if (iteration === 0) return 0;
        const nextIndex = moveIndex(index, code.length);

        //because we do not want sum the currentIndex, then
        if (index === currIndex) return solve(nextIndex, iteration);
        
        return code[index] + solve(nextIndex, iteration - 1)
    }
    return solve(currIndex, mod(k))
};

const defuseTheBomb = (code:number[], k:number) => {
    if (k===0 || code.length <= 1) return Array.from({length:code.length}, () => 0);
    const decryptedCode:number[] = []
    const n = code.length
    
    const calcIndexOfLastElem = (currIndex:number, pad:number) => {
        if (currIndex < 0 || currIndex >= n) throw Error(`Invalid currIndex expected to be in range [0, ${n}) but found ${currIndex}`)
        const overlap = Math.floor(pad / n);

        if (pad > 0){
            return (currIndex + (pad%n + overlap)) % n
        } else {
            return (n + currIndex - (pad%n - overlap)) % n
        }
    };

    for(let i = 0; i < code.length; i++){
        const decryptSum = calcSum(i, k, code)
        decryptedCode.push(
            decryptSum
        )
    }
    
    return decryptedCode
}

const optimizeDefuseTheBomb = (code:number[], k: number) => {
    const n = code.length;
    if ([n, k].some(e => e===0)) return Array.from({length:n}, () => 0);

    const overlap = Math.floor(k/n)
    const circularIndex = (i:number) => i % n;
    const decryptedCode:number[] = [];
    const arrSum = (arr:number[]) => arr.reduce((acc, val) => acc+val, 0)
    for(let i = 0; i < code.length; i++){
        let decryptedInt :number 
        if (i===0){
           const encryptedCodeSum = arrSum(code)
           decryptedInt = overlap*(encryptedCodeSum - code[0]) + arrSum(code.slice(1, 1+k))
        } else {
            decryptedInt = decryptedCode[i-1] + code[circularIndex(i + k + overlap)] - code[i]
        }
        decryptedCode.push(decryptedInt)
    };

    return decryptedCode
}

type ARG = [number[], number]

const ARGS: ARG[] = [
    [ [5, 7, 1, 4], 3 ],
    [ [1, 2, 3, 4], 0 ],
    [ [2, 4, 9, 3], -2 ]
]

console.log("-------- RESULT ---------")

ARGS.forEach( arg => console.log(`\r\n ARG = ${arg.join(" & ")} OLD-RESULT = ${defuseTheBomb(...arg)}`) )

console.log('\r\n')

ARGS.forEach( arg => console.log(`\r\n ARG = ${arg.join(" & ")} OPTIMIZED-RESULT = ${optimizeDefuseTheBomb(...arg)}`) )

/**
 * 838. Push Dominoes

There are n dominoes in a line, and we place each domino vertically upright. In the beginning, we simultaneously push some of the dominoes either to the left or to the right.
After each second, each domino that is falling to the left pushes the adjacent domino on the left. Similarly, the dominoes falling to the right push their adjacent dominoes standing on the right.
When a vertical domino has dominoes falling on it from both sides, it stays still due to the balance of the forces.
For the purposes of this question, we will consider that a falling domino expends no additional force to a falling or already fallen domino.
You are given a string dominoes representing the initial state where:

dominoes[i] = 'L', if the ith domino has been pushed to the left,
dominoes[i] = 'R', if the ith domino has been pushed to the right, and
dominoes[i] = '.', if the ith domino has not been pushed.
Return a string representing the final state.

Example 1:

Input: dominoes = "RR.L"
Output: "RR.L"
Explanation: The first domino expends no additional force on the second domino.
Example 2:

Input: dominoes = ".L.R...LR..L.."
Output: "LL.RR.LLRRLL.."
 
Constraints:

n == dominoes.length
1 <= n <= 105
dominoes[i] is either 'L', 'R', or '.'.

 * npx ts-node ./src/app/2025/May/838.ts
 */

class Solve838{
    constructor(public dominoes:string){
        this.dominoes=dominoes
    };
    solution1(dominoes=this.dominoes){
        const n = dominoes.length;
        const res = Array(n).fill('.');

        let l=-1, r=0;

        //Handling L.H.S edge case
        for(r; r<n&&dominoes[r]!=='R'; r++) {
            if (dominoes[r]==='L') l=r;
        };
        for(let i=0; i<=l; i++) res[i] = 'L';

        let i=r;
        while(i<n){ //If 'R' was found!   
            const char = dominoes[i];
            if (char!=='.'){
                const prevChar = dominoes[Math.max(l,r)];

                if (prevChar===char){
                    for(let j=Math.max(l,r); j<=i; j++) res[j] = char;
                } else if (prevChar==='R'&&char==='L'){ //Collision has to happen
                    const len = i-r+1;
                    for(let j=0; j<Math.floor(len/2); j++){
                        res[r+j] = 'R';
                        res[i-j] = 'L'
                    };
                };
                char==='L' ? l=i : r=i;
            };
            i++;
        };
        
        //Handling R.H.S edge-case
        for(let j=r; j<n&&j>l; j++) res[j] = 'R';

        return res.join('')

    }
};

(
    ()=>{
        const ARGS = [
            "RR.L",
            "LL.RR.LLRRLL.."
        ];
        ARGS.forEach(dominoes => {
            const sol = new Solve838(dominoes);
            console.log(`Dominoes="${dominoes}" Output="${sol.solution1()}"`)
        })
    }
)()
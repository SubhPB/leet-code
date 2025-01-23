/**
 * Input: arr[] = {2, 1, 3, 4}
Output: 20
Explanation: There are 3 matrices of dimensions 2×1, 1×3, and 3×4, 
Let the input 3 matrices be M1, M2, and M3. There are two ways to multiply ((M1 x M2) x M3) and (M1 x (M2 x M3)), 
Please note that the result of M1 x M2 is a 2 x 3 matrix and result of (M2 x M3) is a 1 x 4 matrix.
((M1 x M2) x M3)  requires (2 x 1 x 3)  + (0) +  (2 x 3 x 4) = 30 
(M1 x (M2 x M3))  requires (0)  + (1 x 3 x 4) +  (2 x 1 x 4) = 20 
The minimum of these two is 20.

CMD npx ts-node ./src/app/2025/Jan/mcm.ts
 */

class SolveMCM{
    constructor(public arr:number[], public n=arr.length){
        this.arr = arr; this.n = n;
    };
    solution1(){
        const M:number[][] = [];
        for(let i=0; i<this.n-1; i++) M.push([this.arr[i], this.arr[i+1]]);
        
        //     if (start>=end-1) return 0;
        //     let minCost = Infinity;
        //     for(let i=start+1; i<end; i++){
        //         const leftCost = fn(start, i);
        //         const rightCost = fn(i, end);
                
        //         const tempCost = leftCost + rightCost + M[i-1][0]*M[i-1][1]*M[i][1];
        //         if (tempCost < minCost) minCost = tempCost
        //     };

        //     return minCost
        // };
        const fn = (start:number, end:number):[number, number[]] => {
            if (end-start===1) return [
                0, M[start]
            ];
            let minCost = Infinity, matrix:number[] = []
            for(let i=start+1; i<end; i++){
                const [leftCost, leftM] = fn(start,i);
                const [rightCost, rightM] = fn(i, end);
                const tempCost = leftCost + rightCost + leftM[0]*leftM[1]*rightM[1];
                if (tempCost<minCost){
                    minCost = tempCost, 
                    matrix = [leftM[0], rightM[1]]
                }
            };
            return [minCost, matrix]
        }
        return fn(0,M.length)

    };
    solution2(){
        // if i as pointer = 1, it represents a matrix as M[i-1=0][i] so i>0;
        const record: {[k:string]:number} = {}
        const fn = (start:number, end:number) => {
            const key = `${start}-${end}`;
            if (key in record) record[key]++;
            else record[key] = 1;

            if (start>=end) return 0;
            let minCost = Infinity
            for(let k=start; k<end; k++){
                const cost = fn(start, k) + fn(k+1, end) + this.arr[start-1]*this.arr[k]*this.arr[end];
                if (cost<minCost) minCost = cost;
            };
            return minCost
        };
        const res = fn(1, this.n-1);
        console.log('How much times values were recomputed -> %o', record)
        return res
    };
    solution3(){
        //Now we will solve using DP
        if (this.n<=2) return 0;
        const M = Array.from(
            {length:this.n},
             (_,i) => Array.from(
                {length:this.n},
                (_,j) => i>=j ? 0 : Infinity
            )
        );
        
        const kTable = Array.from(M, (r) => [...r]);

        for(let i=this.n-2; i>=1; i--){
            for(let j=i+1; j<this.n; j++){

                for(let k=i; k<j; k++){
                    const slotVal = M[i][k] + M[k+1][j] + this.arr[i-1]*this.arr[k]*this.arr[j];
                    if (slotVal<M[i][j]){
                        M[i][j] = slotVal
                        kTable[i][j] = k;
                    };
                }
            }
        };
        //We can also use kTable to know the place of parenthesis
        const parenthesis = (i:number,j:number): string => {
            if (i===j) return `M${i}`;
            const k = kTable[i][j];
            return `( ${parenthesis(i,k)} x ${parenthesis(k+1, j)} )`
        };
        
        console.log(parenthesis(1, this.n-1))
        return M[1][this.n-1]
    }
    solve = this.solution3
};

(
    ()=> {
        const ARGS = [
            [2,1,3,4],
            [40,20,30,10,30],
            [29,30]
        ];
        ARGS.forEach(
            arr => console.log(`MCM, arr = ${arr}, minCost = ${new SolveMCM(arr).solve()}`)
        )
    }
)()
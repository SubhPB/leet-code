/**
 * 3394. Check if Grid can be Cut into Sections

You are given an integer n representing the dimensions of an n x n grid, with the origin at the bottom-left corner of the grid. You are also given a 2D array of coordinates rectangles, where rectangles[i] is in the form [startx, starty, endx, endy], representing a rectangle on the grid. Each rectangle is defined as follows:

(startx, starty): The bottom-left corner of the rectangle.
(endx, endy): The top-right corner of the rectangle.
Note that the rectangles do not overlap. Your task is to determine if it is possible to make either two horizontal or two vertical cuts on the grid such that:

Each of the three resulting sections formed by the cuts contains at least one rectangle.
Every rectangle belongs to exactly one section.
Return true if such cuts can be made; otherwise, return false.

Example 1:

Input: n = 5, rectangles = [[1,0,5,2],[0,2,2,4],[3,2,5,3],[0,4,4,5]]

Output: true

Explanation:

The grid is shown in the diagram. We can make horizontal cuts at y = 2 and y = 4. Hence, output is true.

Example 2:

Input: n = 4, rectangles = [[0,0,1,1],[2,0,3,4],[0,2,2,3],[3,0,4,3]]

Output: true

Explanation:
We can make vertical cuts at x = 2 and x = 3. Hence, output is true.

Example 3:

Input: n = 4, rectangles = [[0,2,2,4],[1,0,3,2],[2,2,3,4],[3,0,4,2],[3,2,4,4]]

Output: false
Explanation:
We cannot make two horizontal or two vertical cuts that satisfy the conditions. Hence, output is false.

Constraints:
3 <= n <= 109
3 <= rectangles.length <= 105
0 <= rectangles[i][0] < rectangles[i][2] <= n
0 <= rectangles[i][1] < rectangles[i][3] <= n
No two rectangles overlap.

npx ts-node ./src/app/2025/Mar/3394.ts
 */

class Solve3394{
    constructor(public recs:number[][], public n:number){
        this.recs=recs; this.n=n;
    };
    solution(recs=this.recs,n=this.n){
        const vc = Array.from({length:n+1}, (_,i) => i>0&&i<n ? true : false);
        const hc = Array.from({length:n+1}, (_,i) => i>0&&i<n ? true : false);
        let vCount = n-1, hCount = n-1;
        const check = () => [vCount,hCount].some(c=>c>1);
        for(let r=0; r<recs.length&&check(); r++){
            const [si,sj,ei,ej] = recs[r];

            for(let i=si+1; i<ei&&vCount>1; i++){
                if (vc[i]){
                    vc[i] = false
                    vCount--;
                }
            };
            for(let i=sj+1; i<ej&&hCount>1; i++){
                if (hc[i]){
                    hc[i] = false;
                    hCount--;
                }
            }
        };
        return check()
    };
    solution2(recs=this.recs,n=this.n){
        const Sn = (n:number) => 2**n - 1;
        /**will use yMask to mark horizontal cuts, xMask for vertical cuts */
        let yMask = Sn(n)-1, xMask = Sn(n)-1; //e.g nth and 0th can never be a valid cut at both axises
        for(let i=0; i<recs.length; i++){
            const [sx,sy,ex,ey] = recs[i];
            //horizontal-cuts
            if ((ey-sy)>1) {
                const currYMask = Sn(n+1) - ( Sn(ey-1) - Sn(sy+1) );
                yMask &= currYMask;
            };
            //vertical-cuts
            if ((ex-sx)>1){
                const currXMask = Sn(n+1) - ( Sn(ex-1) - Sn(sx+1) );
                xMask &= currXMask
            }
        };
        return [yMask,xMask].some(mask => mask>0&&((mask&(mask-1))!==0))//There are at-least 2 cuts available.
    }
};

(
    ()=>{
        const ARGS: [number,number[][]][] = [
            [5, [[1,0,5,2],[0,2,2,4],[3,2,5,3],[0,4,4,5]]],
            [4, [[0,0,1,1],[2,0,3,4],[0,2,2,3],[3,0,4,3]]],
            [4, [[0,2,2,4],[1,0,3,2],[2,2,3,4],[3,0,4,2],[3,2,4,4]]]
        ];
        ARGS.forEach(([n,recs]) => console.log(`Recs=${JSON.stringify(recs)} n=${n} solution=${new Solve3394(recs,n).solution()}`))
    }
)()
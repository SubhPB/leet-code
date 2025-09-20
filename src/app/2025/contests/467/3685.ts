/**
 * See ./3685.py for problem statement!
 */

(
    ()=>{
        function subsequenceSumAfterCapping(nums: number[], k: number): boolean[] {
            nums.sort((a,b)=>a-b);
            const n = nums.length, ans = Array(n).fill(false);

            const init = ():boolean[] => Array.from({length:k+1}, (_,i)=> !i);
            const dp:Record<string|number,boolean[]> = {
                0: init()
            };

            const br = (x:number) => {
                let l=0, r=n;
                while (l<r){
                    const m = Math.floor((l+r)/2);
                    if (nums[m]>x){
                        r=m;
                    } else {
                        l=m+1;
                    };
                }
                return l;
            };


            let state = init();
            for(const num of nums){
                for(let j=k; j>=num; j--){
                    state[j] ||= state[j-num]
                };
                if(num<=n) dp[num] = [...state];
            };

            const keys = Object.keys(dp).map(x=>parseInt(x,10));
            keys.sort((a,b)=>a-b);
            const bl = (x:number) => {
                let l = 0, r = keys.length-1;
                while (l<r){
                    const m = Math.ceil((l+r)/2);
                    if (keys[m]<=x){
                        l=m
                    } else {
                        r=m-1
                    };
                };
                return l
            };

            for(let x=1; x<=n; x++){
                const inc = br(x), exc = n-inc;
                let ne=0;
                while (!ans[x-1] && ne<=exc && k>=ne*x){
                    const key = keys[bl(x)];
                    if (dp[key][k-ne*x]){
                        ans[x-1]=true
                    };
                    ne++;
                }
            };
            return ans
        };
    }
)()
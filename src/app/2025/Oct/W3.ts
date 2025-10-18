
(
    function main(){

        function hasIncreasingSubarrays(nums: number[], k: number): boolean {
            /**
            3349. Adjacent Increasing Subarrays Detection I
            
            Given an array nums of n integers and an integer k, determine whether there exist two adjacent subarrays of length k such that both subarrays are strictly increasing. Specifically, check if there are two subarrays starting at indices a and b (a < b), where:
            
            Both subarrays nums[a..a + k - 1] and nums[b..b + k - 1] are strictly increasing.
            The subarrays must be adjacent, meaning b = a + k.
            Return true if it is possible to find two such subarrays, and false otherwise.
            
            Example 1:
            Input: nums = [2,5,7,8,9,2,3,4,3,1], k = 3
            Output: true
            
            Explanation:
            The subarray starting at index 2 is [7, 8, 9], which is strictly increasing.
            The subarray starting at index 5 is [2, 3, 4], which is also strictly increasing.
            These two subarrays are adjacent, so the result is true.
            
            Example 2:
            Input: nums = [1,2,3,4,4,4,4,5,6,7], k = 5
            Output: false
            
            Constraints:
            
            2 <= nums.length <= 100
            1 < 2 * k <= nums.length
            -1000 <= nums[i] <= 1000
            */
            let prev=-1000, i=0; const sms = [0,0];
            for(let num of nums){
                if (num>prev){
                    sms[i]+=1;
                } else {
                    if (i>0){
                        i-=1;
                        sms[0]=1;sms[1]=0
                    } else {
                        if (sms[0]>=k){
                            sms[1]=1;i+=1;
                        } else {
                            sms[0]=1;sms[1]=0;
                        };
                    }
                };
                if (
                    Math.floor(sms[i]/k)>=2
                    || sms.every(sm=>sm>=k)
                ) return true;
                prev=num;
            };
            return false;
        };

        function maxIncreasingSubarrays(nums: number[]): number {
            /**
             * 3350. Adjacent Increasing Subarrays Detection II
                Given an array nums of n integers, your task is to find the maximum value of k for which there exist two adjacent subarrays of length k each, such that both subarrays are strictly increasing. Specifically, check if there are two subarrays of length k starting at indices a and b (a < b), where:
    
                Both subarrays nums[a..a + k - 1] and nums[b..b + k - 1] are strictly increasing.
                The subarrays must be adjacent, meaning b = a + k.
                Return the maximum possible value of k.
    
                A subarray is a contiguous non-empty sequence of elements within an array.
                Example 1:
                Input: nums = [2,5,7,8,9,2,3,4,3,1]
                Output: 3
    
                Explanation:
                The subarray starting at index 2 is [7, 8, 9], which is strictly increasing.
                The subarray starting at index 5 is [2, 3, 4], which is also strictly increasing.
                These two subarrays are adjacent, and 3 is the maximum possible value of k for which two such adjacent strictly increasing subarrays exist.
            
                Constraints:
                2 <= nums.length <= 2 * 10^5
                -10^9 <= nums[i] <= 10^9
            */
            const n=nums.length;
            const rtl=Array(n).fill(1), ltr=Array(n).fill(1);
            for(let i=1;i<n;i++){
                if (nums[i-1]<nums[i]) rtl[i]+=rtl[i-1]
            };
            for (let i=n-2;i>=0;i--){
                if (nums[i]<nums[i+1]) ltr[i]+=ltr[i+1]
            };
            let res=1;
            for(let i=1;i<n;i++){
                res=Math.max(
                    res,
                    Math.min(
                        rtl[i-1],ltr[i]
                    )
                );
            }
            return res;
        };

        function findSmallestInteger(nums: number[], value: number): number {
            /**
            2598. Smallest Missing Non-negative Integer After Operations

            You are given a 0-indexed integer array nums and an integer value.
            In one operation, you can add or subtract value from any element of nums.
            For example, if nums = [1,2,3] and value = 2, you can choose to subtract value from nums[0] to make nums = [-1,2,3].
            The MEX (minimum excluded) of an array is the smallest missing non-negative integer in it.
            For example, the MEX of [-1,2,3] is 0 while the MEX of [1,0,3] is 2.
            Return the maximum MEX of nums after applying the mentioned operation any number of times.

            Example 1:

            Input: nums = [1,-10,7,13,6,8], value = 5
            Output: 4
            Explanation: One can achieve this result by applying the following operations:
            - Add value to nums[1] twice to make nums = [1,0,7,13,6,8]
            - Subtract value from nums[2] once to make nums = [1,0,2,13,6,8]
            - Subtract value from nums[3] twice to make nums = [1,0,2,3,6,8]
            The MEX of nums is 4. It can be shown that 4 is the maximum MEX we can achieve.

            Constraints:
            1 <= nums.length, value <= 10^5
            -10^9 <= nums[i] <= 10^9
             */
            const n=nums.length, freq:{[k:number]:number}={};
            for(let i=0;i<n;i++){
                if (nums[i]<0) nums[i]=value-(value-nums[i])%value;
                nums[i]%=value;
                freq[nums[i]] = 1+(freq[nums[i]]??0)
            };
            for(let x=0;x<n;x++){
                const q = Math.floor(x/value);
                if (q>=(freq[x%value]??0)) return x;
            };
            return n
        };

        function maxDistinctElements(nums: number[], k: number): number {
            /**
             * 3397. Maximum Number of Distinct Elements After Operations

            You are given an integer array nums and an integer k.
            You are allowed to perform the following operation on each element of the array at most once:
            Add an integer in the range [-k, k] to the element.
            Return the maximum possible number of distinct elements in nums after performing the operations.

            Example 1:
            Input: nums = [1,2,2,3,3,4], k = 2
            Output: 6
            Explanation:
            nums changes to [-1, 0, 1, 2, 3, 4] after performing operations on the first four elements.

            1 <= nums.length <= 10^5
            1 <= nums[i] <= 10^9
            0 <= k <= 10^9
             */
            nums.sort((a,b)=>a-b)
            let n = nums.length, idx=-1e9;
            for(let num of nums){
                const ndx=Math.max(idx+1,num-k);
                if (ndx>num+k) n-=1;
                else idx=ndx; // idx assigned!
            };
            return n;
        };
    }
)()

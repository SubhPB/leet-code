
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

        function findLexSmallestString(s: string, a: number, b: number): string {
            /**
            1625. Lexicographically Smallest String After Applying Operations

            You are given a string s of even length consisting of digits from 0 to 9, and two integers a and b.
            You can apply either of the following two operations any number of times and in any order on s:
            Add a to all odd indices of s (0-indexed). Digits post 9 are cycled back to 0. For example, if s = "3456" and a = 5, s becomes "3951".
            Rotate s to the right by b positions. For example, if s = "3456" and b = 1, s becomes "6345".
            Return the lexicographically smallest string you can obtain by applying the above operations any number of times on s.

            A string a is lexicographically smaller than a string b (of the same length) if in the first position where a and b differ, string a has a letter that appears earlier in the alphabet than the corresponding letter in b. For example, "0158" is lexicographically smaller than "0190" because the first position they differ is at the third letter, and '5' comes before '9'.

            Example 1:

            Input: s = "5525", a = 9, b = 2
            Output: "2050"
            Explanation: We can apply the following operations:
            Start:  "5525"
            Rotate: "2555"
            Add:    "2454"
            Add:    "2353"
            Rotate: "5323"
            Add:    "5222"
            Add:    "5121"
            Rotate: "2151"
            Add:    "2050"​​​​​
            There is no way to obtain a string that is lexicographically smaller than "2050".

            Constraints:

            2 <= s.length <= 100
            s.length is even.
            s consists of digits from 0 to 9 only.
            1 <= a <= 9
            1 <= b <= s.length - 1
             */
            let nums:number[]=[]; const n=s.length;
            for(let i=0; i<n; i++){
                const num=parseInt(s[i]); let least=num;
                const x = i+b*(Math.floor((n-i-1)/b))
                if (i%2 || x%2 || ((x+b)%n)%2){
                    for(let j=1; j<10; j++) least=Math.min(least, (num+a*j)%10)
                };
                nums.push(least)
            };
            let res=nums.join('');
            for(let i=0; i<n; i++){
                nums=[...nums.slice(n-b,n),...nums.slice(0,n-b)];
                if (parseInt(nums.join('')) < parseInt(res)){
                    res=nums.join('')
                }
            };
            return res;
        };
    }
)()

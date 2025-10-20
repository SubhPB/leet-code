(
    function main(){ //Contest-470
        function longestSubsequence(nums: number[]): number {
            /**
             * 3702. Longest Subsequence With Non-Zero Bitwise XOR
                You are given an integer array nums.
                Return the length of the longest subsequence in nums whose bitwise XOR is non-zero. If no such subsequence exists, return 0.
    
                Example 1:
                Input: nums = [1,2,3]
                Output: 2
                Explanation:
                One longest subsequence is [2, 3]. The bitwise XOR is computed as 2 XOR 3 = 1, which is non-zero.
    
                Constraints:
                1 <= nums.length <= 10^5
                0 <= nums[i] <= 10^9
             */
            const n=nums.length; let xor=0;
            for(let i=0;i<n;i++){
                xor^=nums[i];
                nums[i]=Math.max(nums[i],nums[Math.max(0,i-1)])
            };
            if (!nums[n-1]) return 0;
            return xor ? n : n-1
        };
    }
)()
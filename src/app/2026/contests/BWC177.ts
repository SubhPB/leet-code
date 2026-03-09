
class BiweeklyContest177 {
    /**
     * 3853. Merge Close Characters
    You are given a string s consisting of lowercase English letters and an integer k.
    Two equal characters in the current string s are considered close if the distance between their indices is at most k.
    When two characters are close, the right one merges into the left. Merges happen one at a time, and after each merge, the string updates until no more merges are possible.
    Return the resulting string after performing all possible merges.
    Note: If multiple merges are possible, always merge the pair with the smallest left index. If multiple pairs share the smallest left index, choose the pair with the smallest right index.
    
    Example 1:
    Input: s = "abca", k = 3
    Output: "abc"
    Explanation:
    ​​​​​​​Characters 'a' at indices i = 0 and i = 3 are close as 3 - 0 = 3 <= k.
    Merge them into the left 'a' and s = "abc".
    No other equal characters are close, so no further merges occur.
    
    Constraints:
    1 <= s.length <= 100
    1 <= k <= s.length
    s consists of lowercase English letters.
    */
    mergeCharacters(s: string, k: number): string {
        const res:string[]=[s[0]], prev={[s[0]]:0};
        const n=s.length, g=Array.from({length:n},()=>0);
        for(let i=1; i<n; i++){
            g[i]=g[i-1]
            if (s[i] in prev){
                const t=i-prev[s[i]]-(g[i]-g[prev[s[i]]]);
                if (t<=k) g[i]+=1; 
                else delete prev[s[i]];
            };
            if (!(s[i] in prev)){
                res.push(s[i]);
                prev[s[i]]=i;
            };
        };
        return res.join('');
    };
    /**
     * 3854. Minimum Operations to Make Array Parity Alternating

    You are given an integer array nums.
    An array is called parity alternating if for every index i where 0 <= i < n - 1, nums[i] and nums[i + 1] have different parity (one is even and the other is odd).
    In one operation, you may choose any index i and either increase nums[i] by 1 or decrease nums[i] by 1.
    Return an integer array answer of length 2 where:
    answer[0] is the minimum number of operations required to make the array parity alternating.
    answer[1] is the minimum possible value of max(nums) - min(nums) taken over all arrays that are parity alternating and can be obtained by performing exactly answer[0] operations.
    An array of length 1 is considered parity alternating.
    
    Example 1:
    Input: nums = [-2,-3,1,4]
    Output: [2,6]
    Explanation:
    Applying the following operations:
    Increase nums[2] by 1, resulting in nums = [-2, -3, 2, 4].
    Decrease nums[3] by 1, resulting in nums = [-2, -3, 2, 3].
    The resulting array is parity alternating, and the value of max(nums) - min(nums) = 3 - (-3) = 6 is the minimum possible among all parity alternating arrays obtainable using exactly 2 operations.

    Constraints:
    1 <= nums.length <= 10^5
    -10^9 <= nums[i] <= 10^9
    */
    makeParityAlternating(nums: number[]): number[] {
        const inf=10**9+1, n=nums.length;
        if (n<=1) return [0,0];
        let ε=0, θ=0;
        for(let i=0; i<n; i++){
            if (nums[i]%2){
                ε+=(i+1)%2; θ+=i%2;
            } else {
                θ+=(i+1)%2; ε+=i%2
            };
        };
        const λ = (i:number) => (x:number) => {
            if (nums[i]%2) return x ? i%2 : (i+1)%2;
            return x ? (i+1)%2 : i%2
        };
        const idxs = Array.from({length:n},(_,i)=>i);
        idxs.sort((a,b)=>nums[a]-nums[b]);
        if (ε<θ){
            return [
                ε,
                Math.max(nums[idxs[n-1]]-λ(idxs[n-1])(0), nums[idxs[n-2]])
                - Math.min(nums[idxs[0]]+λ(idxs[0])(0), nums[idxs[1]])
            ] 
        } else if (ε>θ){
            return [
                θ,
                Math.max(nums[idxs[n-1]]-λ(idxs[n-1])(1), nums[idxs[n-2]])
                - Math.min(nums[idxs[0]]+λ(idxs[0])(1), nums[idxs[1]])
            ] 
        };
        return [
            ε,
            Math.min(
                Math.max(nums[idxs[n-1]]-λ(idxs[n-1])(0), nums[idxs[n-2]]-λ(idxs[n-2])(0))
                - Math.min(nums[idxs[0]]+λ(idxs[0])(0), nums[idxs[1]]+λ(idxs[1])(0)),
                Math.max(nums[idxs[n-1]]-λ(idxs[n-1])(1), nums[idxs[n-2]]-λ(idxs[n-2])(1))
                - Math.min(nums[idxs[0]]+λ(idxs[0])(1), nums[idxs[1]]+λ(idxs[1])(1))            
            )
        ] 
    };
    /**
     * 3855. Sum of K-Digit Numbers in a Range
        You are given three integers l, r, and k.
        Consider all possible integers consisting of exactly k digits, where each digit is chosen independently from the integer range [l, r] (inclusive). If 0 is included in the range, leading zeros are allowed.
        Return an integer representing the sum of all such numbers.​​​​​​​ Since the answer may be very large, return it modulo 109 + 7.

        Example 1:
        Input: l = 1, r = 2, k = 2
        Output: 66

        Explanation:
        All numbers formed using k = 2 digits in the range [1, 2] are 11, 12, 21, 22.
        The total sum is 11 + 12 + 21 + 22 = 66.

        Example 2:
        Input: l = 0, r = 1, k = 3
        Output: 444
        Explanation:
        All numbers formed using k = 3 digits in the range [0, 1] are 000, 001, 010, 011, 100, 101, 110, 111​​​​​​​.
        These numbers without leading zeros are 0, 1, 10, 11, 100, 101, 110, 111.
        The total sum is 444.

        Constraints:

        0 <= l <= r <= 9
        1 <= k <= 10^9
     */
    sumOfNumbers(l: number, r: number, k: number): number {
        return -1;
    };
}
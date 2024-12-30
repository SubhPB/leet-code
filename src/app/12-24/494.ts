/**
 * You are given an integer array nums and an integer target.

You want to build an expression out of nums by adding one of the symbols '+' and '-' before each integer in nums and then concatenate all the integers.

For example, if nums = [2, 1], you can add a '+' before 2 and a '-' before 1 and concatenate them to build the expression "+2-1".
Return the number of different expressions that you can build, which evaluates to target.

Example 1:

Input: nums = [1,1,1,1,1], target = 3
Output: 5
Explanation: There are 5 ways to assign symbols to make the sum of nums be target 3.
-1 + 1 + 1 + 1 + 1 = 3
+1 - 1 + 1 + 1 + 1 = 3
+1 + 1 - 1 + 1 + 1 = 3
+1 + 1 + 1 - 1 + 1 = 3
+1 + 1 + 1 + 1 - 1 = 3
Example 2:

Input: nums = [1], target = 1
Output: 1

CMD: npx ts-node ./src/app/12-24/494.ts 
 */

const arithmeticOperations = ["+", "-"] as const

const solve494 = (nums:number[], target:number, arithmeticOps=arithmeticOperations) => {
    const n = nums.length;
    if(!n) return [''];

    //If there are n operations then we need to find number of ways to arrange them (#-of-arrangements = (#-of-ops)^(#-of-slots))
    const arithmeticPerms = () => {
        const perms:string[] = [];
        if (Array.from(new Set(arithmeticOps)).length === 1) return Array.from({length:nums.length}, () => arithmeticOps[0])
        const fn = (perm:string, l:number) => {
            if (l===n) {
                perms.push(perm)
            } else arithmeticOps.forEach(op => fn(perm+op, l+1))
        };
        fn('', 0)
        return perms
    };

    const sum = (arr:number[]|string[]) => arr.reduce<number>( (acc, val) => acc + Number(val), 0);

    const noOfWays:string[] = [], ops = arithmeticPerms();
    ops.forEach(op => {
        const way = nums.map((num, i) => op[i] + num);
        if (sum(way) === target) noOfWays.push(way.join(''))
    });
    return noOfWays
};

const another494Solution = (nums:number[], target:number, arithmeticOps=arithmeticOperations) => {
    const n = nums.length;
    if(!n) return [''];

    const noOfWays:string[] = [] 
    const solve = (way:string, l:number) => {
        console.log({way, l})
        if(l===n){
            if (eval(way) === target) noOfWays.push(way)
        } else {
            for(let op of arithmeticOps){
                const updatedWay = way + op + nums[l];
                solve(updatedWay, l+1)
            }
        };
    };
    solve('', 0)
    return noOfWays
}

console.log(solve494([1,1,1,1,1], 3));
console.log('\r\n')
console.log(another494Solution([1,1,1,1,1], 3))

const data = [
    { Name: "Alice", Age: 25, Role: "Developer" },
    { Name: "Bob", Age: 30, Role: "Designer" },
    { Name: "Charlie", Age: 35, Role: "Manager" }
  ];
  
  console.table(data);
  
/**
 * Byimaan
 * 
 * 282. Expression Add Operators
Given a string num that contains only digits and an integer target, return all possibilities to insert the binary operators '+', '-', and/or '*' between the digits of num so that the resultant expression evaluates to the target value.

Note that operands in the returned expressions should not contain leading zeros.

 

Example 1:

Input: num = "123", target = 6
Output: ["1*2*3","1+2+3"]
Explanation: Both "1*2*3" and "1+2+3" evaluate to 6.
Example 2:

Input: num = "232", target = 8
Output: ["2*3+2","2+3*2"]
Explanation: Both "2*3+2" and "2+3*2" evaluate to 8.
Example 3:

Input: num = "3456237490", target = 9191
Output: []
Explanation: There are no expressions that can be created from "3456237490" to evaluate to 9191.


CMD :- CMD = npx ts-node ./src/app/8-24/exp-add-op-284.ts
 */

const operands = [
    {
        'symbol': '+',
        invoke(a:number, b:number){
            return a+b;
        }
    },
    {
        'symbol': '-',
        invoke(a:number, b:number){
            return a-b
        }
    },
    {
        'symbol': '*',
        invoke(a:number, b:number){
            return a*b
        }
    }
] as const;

function addOperators(num="232", target=8){
    const ans: string[] = [];
    let calls = 0;
    function rec(n:string, str:string, value: number){
        if (str === '1+2*3'){
            console.log("debug n = " +  n + " & value = " + value)
        }
        if (value === target && !n){
            ans.push(str);
            return
        };
        
        if (n.length === 0){
            return
        }
        
        calls++
        for(let operand of operands){
            let newValue = operand.invoke(value, Number(n[0]))
            let newStr = str + ( (str ? operand.symbol : '') + n[0]);
            rec(n.slice(1), newStr, newValue)
        };
    };
    rec(num, '', 0)
    console.log("calls = ", calls)
    return ans
};

function anotherSolution(nums="232", target=8){

    const result : string[] = []
    
    function BT(expr: string, index: number, value: number, prev: number){

        if (index === nums.length){
            if (value === target){
                result.push(expr)
            }
            return;
        };

        for(let i = index; i < nums.length; i++){

            if (i !== index && nums[index] === '0'){
                break;
            };

            const current = parseInt(nums.substring(index, i+1));

            if (index === 0){
                BT(expr+current, i+1, current, current);
            } else {
                // addition
                BT(expr + '+' + current, i + 1, value + current, current);
                //subtraction
                BT(expr + "-" + current, i + 1, value - current, -current);
                // multipication
                BT(expr + "*" + current, i + 1, value - prev + prev * current, prev * current)

            }

        }
    };
    BT('', 0, 0, 0);
    return result
}

console.log(anotherSolution())


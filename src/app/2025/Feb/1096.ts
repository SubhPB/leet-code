/**
 * 1096. Brace Expansion II

Under the grammar given below, strings can represent a set of lowercase words.
 Let R(expr) denote the set of words the expression represents.

The grammar can best be understood through simple examples:

Single letters represent a singleton set containing that word.
R("a") = {"a"}
R("w") = {"w"}
When we take a comma-delimited list of two or more expressions, we take the union of possibilities.
R("{a,b,c}") = {"a","b","c"}
R("{{a,b},{b,c}}") = {"a","b","c"} (notice the final set only contains each word at most once)
When we concatenate two expressions, we take the set of possible concatenations between two words where the first word comes from the first expression and the second word comes from the second expression.
R("{a,b}{c,d}") = {"ac","ad","bc","bd"}
R("a{b,c}{d,e}f{g,h}") = {"abdfg", "abdfh", "abefg", "abefh", "acdfg", "acdfh", "acefg", "acefh"}
Formally, the three rules for our grammar:

For every lowercase letter x, we have R(x) = {x}.
For expressions e1, e2, ... , ek with k >= 2, we have R({e1, e2, ...}) = R(e1) ∪ R(e2) ∪ ...
For expressions e1 and e2, we have R(e1 + e2) = {a + b for (a, b) in R(e1) × R(e2)}, where + denotes concatenation, and × denotes the cartesian product.
Given an expression representing a set of words under the given grammar, return the sorted list of words that the expression represents.

Example 1:

Input: expression = "{a,b}{c,{d,e}}"
Output: ["ac","ad","ae","bc","bd","be"]
Example 2:

Input: expression = "{{a,z},a{b,c},{ab,z}}"
Output: ["a","ab","ac","z"]
Explanation: Each distinct word is written only once in the final answer.
 

Constraints:

1 <= expression.length <= 60
expression[i] consists of '{', '}', ','or lowercase English letters.
The given expression represents a set of words based on the grammar given in the description.

 npx ts-node ./src/app/2025/Feb/1096.ts
 */

class Solve1096{
    constructor(public expression:string){
        this.expression=expression
    };
    solution(expression=this.expression){
        class Dict{
            constructor(public expr:string){
                this.expr = expr
            };
            flat(){
                if (this.expr.length<=1) return `{${this.expr}}`;

                const tempStartStack = [0];
                const startAt:number[] = [], endsAt:number[] = [];

                for(let i=1; i<this.expr.length; i++){
                    if (this.expr[i]==='{'){
                        tempStartStack.push(i)
                    } else if (this.expr==='}'){
                        startAt.push(tempStartStack.pop()!);
                        endsAt.push(i);
                    } else {
                        //If char is not been surrounded by any bracket e.g. `f` in here: {a{b,c}f{d}}
                        startAt.push(i); endsAt.push(i); //A special way to represent this,
                    }
                };

                let flattenExpr = '{';
                let i = 1;
                while(i<startAt.length){
                    if (startAt[i]===endsAt[i]) flattenExpr += `{${this.expr[i]}}`;
                    else {
                        const subExpr = this.expr.substring(startAt[i], endsAt[i]+1);
                        const isDeeplyNested = (currI:number) => currI+1<startAt.length && endsAt[currI]>startAt[currI+1];
                        if (isDeeplyNested(i)){
                            flattenExpr += new Dict(subExpr).flat();
                            while (isDeeplyNested(i)) i++
                        }
                    };
                    i++
                }
                flattenExpr += '}'
                return flattenExpr 
                
            };
            // parse(){
            //     const flattenExpr = this.flat(); //Here we sure that expression is flatten and not deeply nested
            //     const stack: string[][] = [];
            //     for(let i=1; i<flattenExpr.length-1; i++){
            //         if (flattenExpr[i]==='{'){

            //         }
            //     }
            // }
            
        };
        return new Dict(expression)
    }
};

(
    ()=>{
        const Expressions = [
            "{a,b}{c,{d,e}}",
            "{{a,z},a{b,c},{ab,z}}",
            "a{b,c}{d,e}f{g,h}",
            "{a,b}{c,d}",
        ];
        Expressions.forEach(exp => console.log(`expression=(${exp}) testExpression: ${new Solve1096(exp).solution().flat()}`))
    }
)()
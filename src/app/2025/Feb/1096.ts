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

        const init = () => {
            const  expr = this.expression, n = expr.length;
            const indices: [number/**startIndex of a set */, number /**endIndex of a set*/][] = [];
            const temp:number[] = [];
            const ops : {[indicesIndex:string]:'*'|'+'} = {};
            
            for(let i=0; i<n; i++){
                const char = expr[i]
                const l = indices.length;
                if (char===' ') continue;
                else if (char===','){//An 'additive' operation b/w two sets
                    ops[indices[l-1][0]]='+';//We apply operation from left->right
                } else if (char==='{'){
                    indices.push([i, -1]);
                    temp.push(l);//this will help to determine lastIndex which is currently set to -1
                    /**Another thing to identify is to to determine whether is getting multiplied with other set.
                     * Is there any Set that exist left to it & do any operation with this current index?,
                     *  if that Set exist and does not point to any operation, then it means this is the multiplication
                     */
                    if (i>0&&l>0){ //As 'l' still points to prev length, hence indices[l] points to the current indice, to track left indice we need indices[l-1] or indices[indices.length-2]
                        const leftSetStartingIndex = indices[l-1][0];
                        if (!(leftSetStartingIndex in ops)&&expr[leftSetStartingIndex]!=='{') ops[leftSetStartingIndex] = '*'
                    }
                } else if (char==='}'){
                    indices[temp.pop()!][1] = i; //The unknown lastIndex (where set ends!) is now been found!
                } else { //means this is a letter or continuos seq. of letters, e.g. 'a', 'abc', 'de'
                    indices.push([i, -1]); //A letter or seq of letters can itself be a Set, now we know its starting index but not end of it.
                    //Be prepared in advance following line can cause an expected bug related to 'newspace' in future, during special/intentional inputs whose output would technically correct but awkward for human reading
                    while(i+1<n&&['{','}',',',' '].every(sym=>sym!==expr[i+1])) i++; //To handle letter sequence
                    indices[l][1] = i;//if starting and end index is of same value we can consider this as singleton set
                }
            };
            return {indices,ops}
        };

        const {indices,ops} = init();
        console.log('\n %O',{indices,ops})
        class Tree {
            public children: Tree[] = [];
            public expr : string;
            constructor(public indice:[number,number]){
                this.indice=indice; this.expr = expression.substring(indice[0], indice[1]+1)
            };
            width(){
                return this.children.length
            };
            parse():string[]{
                if (!this.width()) return [this.expr];
                let parsed:string[] = this.children[0].parse();
                for(let i=1; i<this.width(); i++){
                    const nextParsed = this.children[i].parse();
                    const op = ops[this.children[i].indice[0]];
                    if (op==='+'||[parsed,nextParsed].some(p=>!p.length)) parsed = Array.from(new Set([...parsed, ...nextParsed]));
                    else {
                        const newParsed:string[] = []
                        for(let a of parsed){
                            for(let b of nextParsed){
                                newParsed.push(a+b)
                            }
                        };
                        parsed = newParsed
                    }
                }
                return parsed
            }
        };

        if (!indices.length||indices[0][1]!==expression.length-1){
            indices.unshift([0,expression.length-1])
        };

        const parent = [new Tree(indices[0])];

        for(let i=1; i<indices.length;i++){
            const lastIndex = () => parent.length-1;
            let [startFrom,endAt] = indices[i], [parentStartFrom, parentEndAt] = parent[lastIndex()].indice;
            const currTree = new Tree(indices[i]);

            while(startFrom>parentStartFrom&&endAt>parentEndAt){
                const subParent = parent.pop()!;
                const grandParent = parent[lastIndex()]
                grandParent.children.push(subParent);
                [parentStartFrom, parentEndAt] = indices[lastIndex()]
            };

            parent.push(currTree);
        };

        while (parent.length!==1){
            parent[0].children.push(parent.pop()!);
        };

        console.log('%O',{parent: parent[0], children:parent[0].children})

        return parent[0].parse()
    }
};

(
    ()=>{
        const Expressions = [
            "{{a,z},a{b,c},{ab,z}}",
            // "{a,b}{c,{d,e}}",
            // "a{b,c}{d,e}f{g,h}",
            // "{a,b}{c,d}",
        ];
        Expressions.forEach(exp => console.log(`expression=(${exp}) testExpression: %O`, new Solve1096(exp).solution()))
    }
)()
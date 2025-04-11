/**
 * 2140. Solving Questions With Brainpower
You are given a 0-indexed 2D integer array questions where questions[i] = [pointsi, brainpoweri].

The array describes the questions of an exam, where you have to process the questions in order (i.e., starting from question 0) and make a decision whether to solve or skip each question. Solving question i will earn you pointsi points but you will be unable to solve each of the next brainpoweri questions. If you skip question i, you get to make the decision on the next question.

For example, given questions = [[3, 2], [4, 3], [4, 4], [2, 5]]:
If question 0 is solved, you will earn 3 points but you will be unable to solve questions 1 and 2.
If instead, question 0 is skipped and question 1 is solved, you will earn 4 points but you will be unable to solve questions 2 and 3.
Return the maximum points you can earn for the exam.

Example 1:

Input: questions = [[3,2],[4,3],[4,4],[2,5]]
Output: 5
Explanation: The maximum points can be earned by solving questions 0 and 3.
- Solve question 0: Earn 3 points, will be unable to solve the next 2 questions
- Unable to solve questions 1 and 2
- Solve question 3: Earn 2 points
Total points earned: 3 + 2 = 5. There is no other way to earn 5 or more points.
Example 2:

Input: questions = [[1,1],[2,2],[3,3],[4,4],[5,5]]
Output: 7
Explanation: The maximum points can be earned by solving questions 1 and 4.
- Skip question 0
- Solve question 1: Earn 2 points, will be unable to solve the next 2 questions
- Unable to solve questions 2 and 3
- Solve question 4: Earn 5 points
Total points earned: 2 + 5 = 7. There is no other way to earn 7 or more points.
 
Constraints:

1 <= questions.length <= 105
questions[i].length == 2
1 <= pointsi, brainpoweri <= 105

npx ts-node ./src/app/2025/Apr/2140.ts
 */

class Solve2140{
    constructor(public questions:number[][]){
        this.questions=questions
    };
    bfSolution(ques=this.questions, n=ques.length){
        const bforce = (q:number):number => {
            if (q>n) return 0;
            else if (q===n) return ques[q-1][0];
            else return Math.max(
                bforce(q+1), //Not selected
                ques[q-1][0] + bforce(q+ques[q-1][1]+1) //Selected
            );
        };
        return bforce(1)
    };
    solution(ques=this.questions, n=ques.length){
        const dp = Array.from({length:n}, (_,i) => ques[i][0]);
        let mx = 0;
        for(let i=n-1; i>=0; i--){
            const [pts,bp] = ques[i]
            dp[i] = Math.max(
                dp[i], 
                i+bp+1 < n ? (pts + dp[i+bp+1]) : 0
            );
            mx = Math.max(mx, dp[i])
        };
        return mx
    }
};

(
    ()=>{
        const ARGS = [
            [[3, 2], [4, 3], [4, 4], [2, 5]],
            [[1,1],[2,2],[3,3],[4,4],[5,5]],
        ];
        ARGS.forEach(ques => console.log(`Questions=[${JSON.stringify(ques)}] \n bforce=${new Solve2140(ques).bfSolution()} \n dpSol=${new Solve2140(ques).solution()}`))
    }
)()
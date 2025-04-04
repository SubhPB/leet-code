/**
 * 2551. Put Marbles in Bags

You have k bags. You are given a 0-indexed integer array weights where weights[i] is the weight of the ith marble. You are also given the integer k.

Divide the marbles into the k bags according to the following rules:

    No bag is empty.
    If the ith marble and jth marble are in a bag, then all marbles with an index between the ith and jth indices should also be in that same bag.
    If a bag consists of all the marbles with an index from i to j inclusively, then the cost of the bag is weights[i] + weights[j].
    The score after distributing the marbles is the sum of the costs of all the k bags.

    Return the difference between the maximum and minimum scores among marble distributions.

    

    Example 1:

    Input: weights = [1,3,5,1], k = 2
    Output: 4
    Explanation: 
    The distribution [1],[3,5,1] results in the minimal score of (1+1) + (3+1) = 6. 
    The distribution [1,3],[5,1], results in the maximal score of (1+3) + (5+1) = 10. 
    Thus, we return their difference 10 - 6 = 4.
    Example 2:

    Input: weights = [1, 3], k = 2
    Output: 0
    Explanation: The only distribution possible is [1],[3]. 
    Since both the maximal and minimal score are the same, we return 0.

    
npx ts-node ./src/app/2025/Apr/2551.ts
 */

class Solve2551{
    constructor(public weights:number[],public k:number){
        this.weights=weights; this.k=k
    };
    solution(weights=this.weights,k=this.k){
        const n = weights.length;

        const pairSums = Array.from({length:n-1}, (_,i)=> weights[i]+weights[i+1]);
        pairSums.sort((a,b)=>a-b); //decreasing order
        let [minScore,maxScore]:number[] = Array(2).fill(weights[0]+weights[weights.length-1]);
        for(let i=0; i<k-1; i++){ // If need to make k partitions then will need 'k-1' cuts in btw weights.
            minScore += pairSums[i];
            maxScore += pairSums[n-i-2]
        };
        return maxScore - minScore
    }
};

(
    ()=>{
        const ARGS: [number[], number][] = [
            [[1,3,5,1], 2],
            [[1, 3], 2]
        ];
        ARGS.forEach(([weights,bags]) => console.log(`Weights=[${weights.join(',')}] k=${bags} Solution=${new Solve2551(weights,bags).solution()}`))
    }
)()
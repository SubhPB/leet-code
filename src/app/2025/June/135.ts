/**
 * 135. Candy
    There are n children standing in a line. Each child is assigned a rating value given in the integer array ratings.

    You are giving candies to these children subjected to the following requirements:

    Each child must have at least one candy.
    Children with a higher rating get more candies than their neighbors.
    Return the minimum number of candies you need to have to distribute the candies to the children.

    

    Example 1:

    Input: ratings = [1,0,2]
    Output: 5
    Explanation: You can allocate to the first, second and third child with 2, 1, 2 candies respectively.
    Example 2:

    Input: ratings = [1,2,2]
    Output: 4
    Explanation: You can allocate to the first, second and third child with 1, 2, 1 candies respectively.
    The third child gets 1 candy because it satisfies the above two conditions.
    

    Constraints:

    n == ratings.length
    1 <= n <= 2 * 104
    0 <= ratings[i] <= 2 * 104

    npx ts-node ./src/app/2025/June/135.ts
 */

class Solve135{
    constructor(public ratings:number[]){
        this.ratings=ratings;
    };
    solution1(R: number[]): number { //self-thought algorithm, fully working and correct
        const n = R.length;
    
        const intervals = [0];
        for(let i=1; i<n-1; i++){
            const interval = intervals[intervals.length-1];
            if ( //Only strict intervals should be considered.
                [R[interval], R[i+1]].every(r => r===R[i])
                || R[interval]<R[i]&&R[i]<R[i+1]
                || R[interval]>R[i]&&R[i]>R[i+1]
            ) continue;
            intervals.push(i);
        };
        if (
            intervals[intervals.length-1]!==n-1
        ) intervals.push(n-1);
    
        const fn = (x:number) => x*(x+1)/2;
        let prev = 1, res = 1;
        for(let i=1; i<intervals.length; i++){
            const a = intervals[i-1], b = intervals[i];
            if (R[a]<R[b]){
                //When slope is increasing, acc. to problem its will would always be equal to 1.
                res += fn(b-a+1)-1;//avoiding overcount of head
                prev = b-a+1;//tail value
            } else if (R[a]>R[b]){
                //When slope is decreasing, its head should always be atleast 2 or more. if not we manually need to correct it.
                const head = b-a+1
                res += fn(head-1);
                if (prev<head) res += head-prev; //avoiding overcount
                prev = 1//tail value
            } else {
                //Upon constant slope, heads should always be atleast 1 which it is everytime!
                res += b-a
                prev=1//tail value
            }
        }
        return res;
    }
}


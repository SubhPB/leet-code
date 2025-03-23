/**
 * 1011. Capacity To Ship Packages Within D Days

A conveyor belt has packages that must be shipped from one port to another within days days.
The ith package on the conveyor belt has a weight of weights[i]. Each day, we load the ship with packages on the conveyor belt (in the order given by weights). We may not load more weight than the maximum weight capacity of the ship.
Return the least weight capacity of the ship that will result in all the packages on the conveyor belt being shipped within days days.

Example 1:

Input: weights = [1,2,3,4,5,6,7,8,9,10], days = 5
Output: 15
Explanation: A ship capacity of 15 is the minimum to ship all the packages in 5 days like this:
1st day: 1, 2, 3, 4, 5
2nd day: 6, 7
3rd day: 8
4th day: 9
5th day: 10

Note that the cargo must be shipped in the order given, so using a ship of capacity 14 and splitting the packages into parts like (2, 3, 4, 5), (1, 6, 7), (8), (9), (10) is not allowed.
Example 2:

Input: weights = [3,2,2,4,1,4], days = 3
Output: 6
Explanation: A ship capacity of 6 is the minimum to ship all the packages in 3 days like this:
1st day: 3, 2
2nd day: 2, 4
3rd day: 1, 4
Example 3:

Input: weights = [1,2,3,1,1], days = 4
Output: 3
Explanation:
1st day: 1
2nd day: 2
3rd day: 3
4th day: 1, 1

npx ts-node ./src/app/2025/Mar/1011.ts
 */

class Solve1011{
    constructor(public weights:number[], public days:number){
        this.weights=weights; this.days = days;
    };
    solution(weights=this.weights, days=this.days){
        /**
         * 1 <= days <= weights.length <= 5 * 104 
         * 1 <= weights[i] <= 500
         */
        /**
         * left means minimum possible weightCapacity will surely needed. (this value can be valid/invalid);
         * right means max capacity possible of ship to make this ship happen even in 1 day. (This always true)
         */
        let left = 0, right = 0; 
        weights.forEach(w => {
            left = Math.max(left, w)
            right+=w
        }); 
        const canShip = (shipCapacity:number) => {
            let daysCount = 1, belt = 0; /**Belt weight on start of first day */
            for(let i=0; i<weights.length&&daysCount<=days; i++){
                if ((belt+weights[i])>shipCapacity){
                    belt = 0;
                    daysCount++; //Will ship remaining weight on next day
                };
                belt += weights[i]
            }
            return daysCount <= days
        };
        while(left<right){
            const mid = Math.floor((left+right)/2);
            if (canShip(mid)){
                right = mid;
            } else {
                left = mid + 1
            }
        };
        return left;
    }
};

(
    ()=>{
        const ARGS : [number[], number][] = [
            [[1,2,3,4,5,6,7,8,9,10], 5],
            [[3,2,2,4,1,4], 3],
            [ [1,2,3,1,1], 4]
        ];
        ARGS.forEach(([weights, days]) => console.log(`Weights=[${weights.join(', ')}] Days=${days} Min-capacity=${new Solve1011(weights,days).solution()}`))
    }
)()

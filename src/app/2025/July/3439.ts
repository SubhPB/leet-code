/**
 * 3439. Reschedule Meetings for Maximum Free Time I
    You are given an integer eventTime denoting the duration of an event, where the event occurs from time t = 0 to time t = eventTime.
    You are also given two integer arrays startTime and endTime, each of length n. These represent the start and end time of n non-overlapping meetings, where the ith meeting occurs during the time [startTime[i], endTime[i]].
    You can reschedule at most k meetings by moving their start time while maintaining the same duration, to maximize the longest continuous period of free time during the event.
    The relative order of all the meetings should stay the same and they should remain non-overlapping.
    Return the maximum amount of free time possible after rearranging the meetings.
    Note that the meetings can not be rescheduled to a time outside the event.


    Example 1:

    Input: eventTime = 5, k = 1, startTime = [1,3], endTime = [2,5]

    Output: 2

    Explanation:

    Reschedule the meeting at [1, 2] to [2, 3], leaving no meetings during the time [0, 2].

    Example 2:

    Input: eventTime = 10, k = 1, startTime = [0,2,9], endTime = [1,4,10]

    Output: 6

    Explanation:

    Reschedule the meeting at [2, 4] to [1, 3], leaving no meetings during the time [3, 9].

    Example 3:

    Input: eventTime = 5, k = 2, startTime = [0,1,2,3,4], endTime = [1,2,3,4,5]

    Output: 0

    Explanation:

    There is no time during the event not occupied by meetings.

    

    Constraints:

    1 <= eventTime <= 10^9
    n == startTime.length == endTime.length
    2 <= n <= 10^5
    1 <= k <= n
    0 <= startTime[i] < endTime[i] <= eventTime
    endTime[i] <= startTime[i + 1] where i lies in the range [0, n - 2].

    CMD npx ts-node ./src/app/2025/July/3439.ts
 */

class Solve3439{
    constructor(public eventTime:number, public k:number, public startTime:number[],public endTime:number[]){
        this.eventTime=eventTime; this.startTime=startTime; this.endTime=endTime; this.k=k;
    };
    solution(eventTime=this.eventTime,k=this.k, startTime=this.startTime, endTime=this.endTime){
        const freeTime = [startTime[0]], n = startTime.length;
        for(let i=1; i<n; i++){
            freeTime.push(startTime[i]-endTime[i-1])
        };
        freeTime.push(eventTime-endTime[n-1]);

        let max = 0, sum = 0;
        for(let i=0; i<=k; i++) sum += freeTime[i];
        max = sum;

        for(let i=1; i<freeTime.length-k; i++){
            
            sum -= freeTime[i-1] 
            sum += freeTime[k+i]

            max = Math.max(max, sum)
        }
        return max;
    }
};

(
    ()=>{
        const testcases:[number,number,number[],number[]][] = [
            // [10, 1,  [0,2,9], [1,4,10]],
            [55, 2, [48,49,52,53], [49,52,53,54]]
        ];
        for(let [e,k,st,et] of testcases){
            const sol = new Solve3439(e,k,st,et)
            console.log(`eventTimes=${e} k=${k} startTime=[${st.join(',')}] endTime=[${et.join(',')}] solution=${sol.solution()}`)
        }
    }
)()
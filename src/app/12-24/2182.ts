/**
 * BYIMAAN
 * Input: s = "cczazcc", repeatLimit = 3
    Output: "zzcccac"
    Explanation: We use all of the characters from s to construct the repeatLimitedString "zzcccac".
    The letter 'a' appears at most 1 time in a row.
    The letter 'c' appears at most 3 times in a row.
    The letter 'z' appears at most 2 times in a row.
    Hence, no letter appears more than repeatLimit times in a row and the string is a valid repeatLimitedString.
    The string is the lexicographically largest repeatLimitedString possible so we return "zzcccac".
    Note that the string "zzcccca" is lexicographically larger but the letter 'c' appears more than 3 times in a row, so it is not a valid repeatLimitedString.

    CMD npx ts-node ./src/app/12-24/2182.ts
 */

const fn2182 = (s:string, repeatingLimit=3) => {
    
    let count = (str:string, c:string) => str.split(c).length - 1;
    // counter arrange in anti-alphabetic order
    const counter = Array.from(new Set(s)).map(
        c => ([c, count(s, c)] as [string, number])
    ).sort( (a, b) => b[0].charCodeAt(0) - a[0].charCodeAt(0));

    let repeatingStr = '';

    while (counter.length && repeatingLimit >= 0){
        const [char, count] = counter[0];

        if (count === 0){
            counter.shift()
            continue
        };
        if (repeatingStr.endsWith(char)){
            if (counter.length === 1) break; // Can't repeat the character even have more of them
            [counter[0], counter[1]]= [counter[1], counter[0]];
            continue;
        };
        const noOfChars = Math.min(repeatingLimit, count);
        repeatingStr += Array.from({length:noOfChars}, () => char).join('');
        counter[0] = [char, count - noOfChars];
    }

    return repeatingStr

};

console.log(fn2182("cczazcc", 3))
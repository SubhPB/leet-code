/**
 * An approach to quick-sort algorithm,
 * 
 * CMD npx ts-node ./src/app/12-24/quick-sort.ts
 */

const quickSort = (arr:number[]) => {
    const swap = (i:number, j:number) => [arr[i], arr[j]] = [arr[j], arr[i]];
    
    const fn = (start:number, end:number) => {
        if (end-start <= 1 || start>=end) return; // subArr = arr[start:end]
        let pivot = arr[start], a = start+1, b = end-1;
        while(a<b){
            if (arr[a]>=arr[b]) swap(a, b);
            while(a<end && arr[a]<=pivot) a++;
            while(b>=a && arr[b]>=pivot) b--;
        };
        swap(b, start);
        // arr[b] is been sorted, and at the correct spot
        fn(start, b);
        fn(b+1, end)

    };
    fn(0, arr.length)
    return arr
};

const TESTARRS = [
    [35, 50, 15, 25, 80, 0, 90, 45],
    [35, 4,3, 4, 3, 2, 1]
]

console.log(`@quick-sort`)
TESTARRS.forEach( arr => console.log(`Quick-Sort Algorithm \r\n ${arr} -> ${quickSort(arr)}`) )
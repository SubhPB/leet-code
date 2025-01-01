/**
 * An approach to quick-sort algorithm,
 * 
 * CMD npx ts-node ./src/app/12-24/quick-sort.ts
 */

const quickSort = (arr:number[]) => {
    const swap = (i:number, j:number) => [arr[i], arr[j]] = [arr[j], arr[i]]
    const n = arr.length
    const pivotSort = (ascI:number=1, descI:number=arr.length-1) => {
        if (descI <= ascI) return;
        const pivot = 0;
        while(descI > ascI){
            while(arr[descI]>arr[pivot]) descI--;
            while(arr[ascI]<arr[pivot] && ascI<n) ascI++;
            if (arr[ascI]>arr[descI]) swap(ascI, descI);
        };
        const newPivot = descI;
        swap(pivot, newPivot);
        pivotSort(1, newPivot-1);
        pivotSort(newPivot+1, n-1)
    }
    pivotSort()
    return arr
};

const arr = [35, 50, 15, 25, 80, 0, 90, 45]

console.log(`@quick-sort`)
console.log(`Quick-Sort Algorithm \r\n ${arr} -> ${quickSort(arr)}`)
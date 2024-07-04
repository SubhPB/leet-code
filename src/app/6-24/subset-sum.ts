// Byimaan

// find the subset whose sum is 11

const array = [2, 3, 7, 8, 10], targetSum = 11;

//utils
const arraySum = (arr: number[]) => arr.reduce((acc, val) => acc+val,0)

const solve = () => {

    const subsets = [];

    const recursion = (i: number, subset: number[]) => {
        const subsetSum = arraySum(subset);
        // base case
        if (subsetSum === targetSum){
            subsets.push(subset);
            return
        };

        if (array[i] <= targetSum - subsetSum){
            recursion(i+1, [...subset, array[i]])
        }
    };

}


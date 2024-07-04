// Byimaan

/**
*   Given a positive integer n, generate an n x n matrix filled with elements from 1 to n2 in spiral ord
*   Input: n = 3
    Output: [[1,2,3],[8,9,4],[7,6,5]]
    CMD: npx ts-node ./src/app/6-24/spiral59.ts
 */

const generateSpiralMatrix = (n: number) => {
    
    // boundries
    let [right, bottom, left, top] = [n-1, n-1, 0, 1];

    const compass = {
        'R': [0, 1],
        'B': [1, 0],
        'L': [0, -1],
        'T': [-1, 0]
    };

    const indicator = (currentPosition: keyof (typeof compass),a: number, b: number) => {
        // this behave according to the upcoming state of a & b
        
        // first check from right diretion
        // if now is right there only outputs can be producd either keep going right else bottom if boundary reached;
        
        let outcome = {
            'array': compass[currentPosition],
            'shrinkBoundary': () => {},
            'direction': currentPosition,
        };
        const update = (arr: number[], func: Function, direction: keyof(typeof compass)) => {
            outcome.array = arr;
            outcome.direction= direction
            func();
        }

        if (currentPosition === 'R' && b === right) {
            update(compass.B, () => right--, 'B')
        };

        // same with bottom if all okay then keep going bottom else left
        if (currentPosition === 'B' && a === bottom) {
            update(compass.L, () => bottom--, 'L')
        };

        if (currentPosition === 'L' && b === left) {
            update(compass.T, () => left++, 'T')
        };

        if (currentPosition === 'T' && a === top){
            update(compass.R, () => top++, 'R')

        };

        return outcome;
    };

    let [i, j, counter] = [0, 0, 1];

    const matrix: (null|number)[][] = Array.from({length: n}, () => Array(n).fill(null))

    let direction: keyof(typeof compass) = 'R'
    while (counter <= n**2){
        matrix[i][j] = counter;
        const result = indicator(direction, i, j);
        direction = result.direction;
        const [a, b] = result.array;
        i = i+a;
        j = j+b;
        counter++;
    };
    for(let A of matrix){
        console.log(A)
    };
};

const solution = (n : number) => {

    // const 

}
generateSpiralMatrix(4)
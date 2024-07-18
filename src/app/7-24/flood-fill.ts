// Byimaan

// CMD :- npx ts-node ./src/app/7-24/flood-fill.ts



function floodFill(image: number[][], sr: number, sc: number, newColor: number): number[][] {
    // Your implementation here;

    const m = image.length, n = image[0].length

    const directions = [
        [-1, 0], [0, 1],[1, 0],[0, -1]
    ];
    const _matrix: number[][] = JSON.parse(JSON.stringify(image))

    const isValid = (i: number, j:number) => {
        if (i >=0 && i < m && j >= 0 && j < n && (_matrix[i][j] === image[sr][sc])){
            return true
        }
        return false
    };

    
    
    const firstAppproach = () => {
        const queue = [
            [sr, sc]
        ];

        while (queue.length !== 0){
            const [i, j] = queue.pop() as number[];
            _matrix[i][j] = newColor
            for(let dir of directions){
                let _i = dir[0] + i, _j = dir[1] + j
                if (isValid(_i, _j)){
                    queue.push([_i, _j])
                }
            }
        };
        return _matrix;
    };

    firstAppproach();
    for(let r of _matrix){
        console.log(JSON.stringify(r))
    }

    return image
}

// Example
const image = [
    [1, 1, 1, 1, 1, 1, 1],
    [1, 1, 0, 0, 0, 1, 1],
    [1, 0, 1, 1, 0, 0, 1],
    [1, 0, 0, 1, 1, 0, 1],
    [1, 1, 0, 0, 0, 1, 1],
    [1, 1, 1, 1, 1, 1, 1]
];
const sr = 2;
const sc = 3;
const newColor = 2;

console.log(floodFill(image, sr, sc, newColor));

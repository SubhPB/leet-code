/**
 * Byimaan
 * 
 * Given an m x n board of characters and a list of strings words, return all words on the board.

Each word must be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

 Example 1:

Input: board = [
    ["o","a","a","n"],
    ["e","t","a","e"],
    ["i","h","k","r"],
    ["i","f","l","v"]
], 
words = ["oath","pea","eat","rain"]
Output: ["eat","oath"]
 * 
 * CMD :- npx ts-node ./src/app/8-24/find-word-path.ts
 */

const M = [
    [ 'o', 'a', 'a', 'n' ],
    [ 'e', 't', 'a', 'e' ],
    [ 'i', 'h', 'k', 'r' ],
    [ 'i', 'f', 'l', 'v' ],
]

const dictWords = ['oath', 'pea', 'eat', 'rain', 'oak'];

function findWords(matrix=M, words=dictWords){

    
    const directions = [
        [0, 1], //right
        [1, 0], // bottom
        [0, -1], // left
        [-1, 0], // top
    ];

    const isValid = (i: number /** nextI */, j: number /** nextJ */, nextChar: string) => (
        (i < matrix.length && i >= 0) && (
            j < matrix[0].length && j >= 0
        ) && (
            matrix[i][j] === nextChar
        )
    )
    
    const solve = (targetWord: string, i: number, j: number): boolean => {

        targetWord = targetWord.slice(1);

        if (targetWord.length === 0){
            return true
        };

        for (let direction of directions){
            let newI = i + direction[0], newJ = j + direction[1];
            if (isValid(newI, newJ, targetWord[0])){
                if (solve(targetWord, newI, newJ)){
                    return true
                }
            }
        }

        return false
    };
    
    const outputWords: string[] = []
    const options = (char :string) => words.filter(word => word.startsWith(char) && !outputWords.includes(word));

    for(let i = 0; i < matrix.length; i++){
        for(let j = 0; j < matrix[0].length; j++){

            const possibleTargets = options(matrix[i][j]);            
            for (let target of possibleTargets){
                if (solve(target, i, j)){
                    outputWords.push(target)
                }
            };
        };
    };

    return outputWords
};

console.log(findWords())



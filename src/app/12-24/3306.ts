/**
 * 3306. Count of Substrings Containing Every Vowel and K Consonants II
You are given a string word and a non-negative integer k.

Return the total number of 
substrings
 of word that contain every vowel ('a', 'e', 'i', 'o', and 'u') at least once and exactly k consonants.

Example 1:

Input: word = "aeioqq", k = 1

Output: 0

Explanation:

There is no substring with every vowel.

Example 2:

Input: word = "aeiou", k = 0

Output: 1

Explanation:

The only substring with every vowel and zero consonants is word[0..4], which is "aeiou".

Example 3:

Input: word = "ieaouqqieaouqq", k = 1

Output: 3

Explanation:

The substrings with every vowel and one consonant are:

word[0..5], which is "ieaouq".
word[6..11], which is "qieaou".
word[7..12], which is "ieaouq".

CMD npx ts-node ./src/app/12-24/3306.ts
 */
const vowels = ['a', 'e', 'i', 'o', 'u'];
const isVowel = (c:string) => vowels.includes(c);

function solve3306(s:string, k:number){
    const n = vowels.length + k;
    if (k < 0 || n > s.length) return 0;

    let count = 0

    const record: {[k:string]: number} = {'k':0};
    vowels.forEach(vowel => record[vowel] = 0);

    const recordKey = (char:string) => isVowel(char) ? char : 'k'

    for(let i=0; i <(s.length-(n-1)); i++){
        if(i===0){
            for(let j=0; j < i+n; j++) record[recordKey(s[j])]++;
        } else {
            const lastChar = s[i-1], newChar = s[i+n-1];
            record[recordKey(lastChar)]--;
            record[recordKey(newChar)]++;
        };
        if (record['k'] === k && vowels.every(vowel => record[vowel] === 1)) count++;
    };

    return count
};

const args = [
    ["aeioqq", 1],
    ['aeiou', 0],
    ["ieaouqqieaouqq", 1]
];

args.forEach(
    ([s, k]) => {
        console.log(`\r\n s=${s} k=${k} --> ${solve3306(s as string, k as number)}`)
    }
)
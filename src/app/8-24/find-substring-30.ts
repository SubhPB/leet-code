/**
 * BYIMAAN
 * 
 * 30. Substring with Concatenation of All Words

You are given a string s and an array of strings words. All the strings of words are of the same length.

A concatenated string is a string that exactly contains all the strings of any permutation of words concatenated.

For example, if words = ["ab","cd","ef"], then "abcdef", "abefcd", "cdabef", "cdefab", "efabcd", and "efcdab" are all concatenated strings. "acdbef" is not a concatenated string because it is not the concatenation of any permutation of words.
Return an array of the starting indices of all the concatenated substrings in s. You can return the answer in any order.

 

Example 1:

Input: s = "barfoothefoobarman", words = ["foo","bar"]

Output: [0,9]

Explanation:

The substring starting at 0 is "barfoo". It is the concatenation of ["bar","foo"] which is a permutation of words.
The substring starting at 9 is "foobar". It is the concatenation of ["foo","bar"] which is a permutation of words.

Example 3:

Input: s = "barfoofoobarthefoobarman", words = ["bar","foo","the"]

Output: [6,9,12]

Explanation:

The substring starting at 6 is "foobarthe". It is the concatenation of ["foo","bar","the"].
The substring starting at 9 is "barthefoo". It is the concatenation of ["bar","the","foo"].
The substring starting at 12 is "thefoobar". It is the concatenation of ["the","foo","bar"].

CMD :- npx ts-node ./src/app/8-24/find-substring-30.ts

 */


class FindSubString {
    constructor(public s: string, public words: string[]){
        this.s = s;
        this.words = words
    };

    public permutation = {
        dp: (words : string | string[] =this.words) => {

            if (typeof words === 'string'){
                words = words.split('')
            }

            const layers = [
                [words]
            ];

            for(let layer = 0; layer < words.length; layer ++){

                const prevLayer = layers.pop() as string[][]
                
                const newLayer = [];

                for(let perms of prevLayer){
                    for(let i = layer; i < perms.length; i++){

                        const copy = [...perms];
                        [copy[layer], copy[i]] = [copy[i], copy[layer]];
                        newLayer.push(copy)
                    }
                };

                layers.push(newLayer)
            }

            return layers[layers.length - 1].map(l => l.join(''));

        },

        recursion: (words: string | string[]=this.words) => {
            words = typeof words === 'string' ? words.split('') : words
            const perms: string[] = []; // ["abcdef", "abefcd", "cdabef", "cdefab", "efabcd", and "efcdab"]

            const rec = (index: number, w: string[] /**["ab","cd","ef"] */) => {
                if (index === words.length){
                    perms.push(w.join(''))
                    return
                };

                for(let i = index; i < words.length; i++){
                    [w[index], w[i]]  = [w[i], w[index]]
                    rec(index+1, [...w]);
                }
            };

            rec(0, words)
            return perms
        }
    }

    solve(s=this.s, words=this.words){
        const indexes: number[] = [];

        /**
         * So our first task is to find the permutation of the words
         */

        for (let perm of this.permutation.dp()){
            const index = s.indexOf(perm);
            if (index !== -1) indexes.push(index)
        }
        return indexes;
    };

    
};

const s = "barfoothefoobarman", words = ["bar", "foo"];

console.log(new FindSubString(s, words).solve())
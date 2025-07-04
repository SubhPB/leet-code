'''

    ======================================= 3304. Find the K-th Character in String Game I =======================================

    Alice and Bob are playing a game. Initially, Alice has a string word = "a".

    You are given a positive integer k.

    Now Bob will ask Alice to perform the following operation forever:

    Generate a new string by changing each character in word to its next character in the English alphabet, and append it to the original word.
    For example, performing the operation on "c" generates "cd" and performing the operation on "zb" generates "zbac".

    Return the value of the kth character in word, after enough operations have been done for word to have at least k characters.

    Note that the character 'z' can be changed to 'a' in the operation.


    ======================================= 3307. Find the K-th Character in String Game II =======================================

    Alice and Bob are playing a game. Initially, Alice has a string word = "a".

    You are given a positive integer k. You are also given an integer array operations, where operations[i] represents the type of the ith operation.

    Now Bob will ask Alice to perform all operations in sequence:

    If operations[i] == 0, append a copy of word to itself.
    If operations[i] == 1, generate a new string by changing each character in word to its next character in the English alphabet, and append it to the original word. For example, performing the operation on "c" generates "cd" and performing the operation on "zb" generates "zbac".
    Return the value of the kth character in word after performing all the operations.

    Note that the character 'z' can be changed to 'a' in the second type of operation.

    

    Example 1:

    Input: k = 5, operations = [0,0,0]

    Output: "a"

    Explanation:

    Initially, word == "a". Alice performs the three operations as follows:

    Appends "a" to "a", word becomes "aa".
    Appends "aa" to "aa", word becomes "aaaa".
    Appends "aaaa" to "aaaa", word becomes "aaaaaaaa".


'''   

   
class Solution:
    def kthCharacterI(self, k: int) -> str:
        l = 0
        while k>1:
            d = (k-1).bit_length()-1
            k = k-(1<<d)
            l+=1
        l %= 26
        return chr(ord('a')+l)
    def kthCharacterII(self, k: int, operations: list[int]) -> str:
        l = 0
        while k>1:
            b = (k-1).bit_length()-1
            k -= (1<<b)
            l += (operations[b]-1)
            l+=1
        l%=26
        return chr(ord('a')+l)
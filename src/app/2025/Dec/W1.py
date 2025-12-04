from typing import List
class Solution:
    '''
        3756. Concatenate Non-Zero Digits and Multiply by Sum II

        You are given a string s of length m consisting of digits. You are also given a 2D integer array queries, where queries[i] = [li, ri].
        For each queries[i], extract the substring s[li..ri]. Then, perform the following:
        Form a new integer x by concatenating all the non-zero digits from the substring in their original order. If there are no non-zero digits, x = 0.
        Let sum be the sum of digits in x. The answer is x * sum.
        Return an array of integers answer where answer[i] is the answer to the ith query.

        Since the answers may be very large, return them modulo 109 + 7.
        Example 1:
        Input: s = "10203004", queries = [[0,7],[1,3],[4,6]]
        Output: [12340, 4, 9]
        Explanation:
        s[0..7] = "10203004"
        x = 1234
        sum = 1 + 2 + 3 + 4 = 10
        Therefore, answer is 1234 * 10 = 12340.
        s[1..3] = "020"
        x = 2
        sum = 2
        Therefore, the answer is 2 * 2 = 4.
        s[4..6] = "300"
        x = 3
        sum = 3
        Therefore, the answer is 3 * 3 = 9.

        Constraints:

        1 <= m == s.length <= 10^5
        s consists of digits only.
        1 <= queries.length <= 10^5
        queries[i] = [li, ri]
        0 <= li <= ri < m
    '''
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        n=len(s);sums=[0]*(n+1);concs=[0]*(n+1);M=10**9+7
        ADD=lambda x,y:(x%M+y%M)%M;MUL=lambda x,y:(x%M * y%M)%M
        for i,num in enumerate(s):
            sums[i]=ADD(sums[i-1],int(num)); concs[i]=concs[i-1]
            if int(num): concs[i]=MUL(concs[i],10)
            concs[i]=ADD(concs[i],int(num))

        for i,[l,r] in enumerate(queries):
            [n1,n2]=[len(str(concs[j])) for j in (l-1,r)]
            queries[i]=ADD(concs[r],-MUL(concs[l-1],10**(n2-n1)))
            queries[i]=MUL(queries[i],sums[r]-sums[l-1])
        return queries

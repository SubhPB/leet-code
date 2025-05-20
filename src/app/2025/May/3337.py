'''
3337. Total Characters in String After Transformations II

You are given a string s consisting of lowercase English letters, an integer t representing the number of transformations to perform, and an array nums of size 26. In one transformation, every character in s is replaced according to the following rules:

Replace s[i] with the next nums[s[i] - 'a'] consecutive characters in the alphabet. For example, if s[i] = 'a' and nums[0] = 3, the character 'a' transforms into the next 3 consecutive characters ahead of it, which results in "bcd".
The transformation wraps around the alphabet if it exceeds 'z'. For example, if s[i] = 'y' and nums[24] = 3, the character 'y' transforms into the next 3 consecutive characters ahead of it, which results in "zab".
Return the length of the resulting string after exactly t transformations.

Since the answer may be very large, return it modulo 109 + 7.

 

Example 1:

Input: s = "abcyy", t = 2, nums = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2]

Output: 7

Explanation:

First Transformation (t = 1):

'a' becomes 'b' as nums[0] == 1
'b' becomes 'c' as nums[1] == 1
'c' becomes 'd' as nums[2] == 1
'y' becomes 'z' as nums[24] == 1
'y' becomes 'z' as nums[24] == 1
String after the first transformation: "bcdzz"
Second Transformation (t = 2):

'b' becomes 'c' as nums[1] == 1
'c' becomes 'd' as nums[2] == 1
'd' becomes 'e' as nums[3] == 1
'z' becomes 'ab' as nums[25] == 2
'z' becomes 'ab' as nums[25] == 2
String after the second transformation: "cdeabab"
Final Length of the string: The string is "cdeabab", which has 7 characters.

Example 2:

Input: s = "azbk", t = 1, nums = [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2]

Output: 8

Explanation:

First Transformation (t = 1):

'a' becomes 'bc' as nums[0] == 2
'z' becomes 'ab' as nums[25] == 2
'b' becomes 'cd' as nums[1] == 2
'k' becomes 'lm' as nums[10] == 2
String after the first transformation: "bcabcdlm"
Final Length of the string: The string is "bcabcdlm", which has 8 characters.

 

Constraints:

1 <= s.length <= 105
s consists only of lowercase English letters.
1 <= t <= 109
nums.length == 26
1 <= nums[i] <= 25

python ./src/app/2025/May/3337.py
'''


class SolvePY3337:
    M = 10**9 + 7
    def MATRIX(self,m:int,n:int,inp:int|function)->list[list[int]]:
        return [
            [
                inp if isinstance(inp,int) else inp(mi,ni) for ni in range(n)
            ] for mi in range(m)
        ]
    def mod_mul(self, a:int, b:int):
        return (
            (a%self.M) * (b%self.M)
        )%self.M
    def mod_add(self, a:int, b:int):
        return (
            (a%self.M) + (b%self.M)
        )%self.M
    def matrix_mul(self, M1:list[list[int]], M2:list[list[int]]):
        a, b, c, d, = len(M1), len(M1[0]), len(M2), len(M2[0])
        if (b != c): raise ValueError(f"Found {b}!={c}, M1[{a},{b}] * M2[{c}{d}] is not possible!")
        def fill_slot(mi:int, ni:int):
            sum=0
            for i in range(b):
                sum = self.mod_add(
                    sum,
                    self.mod_mul(
                        M1[mi][i], M2[i][ni]
                    )
                )
            return sum
        return self.MATRIX(
            a,
            d,
            fill_slot
        )
    def matrix_exp(self, M:list[list[int]], pow:int):
        def identity_slot(mi:int, ni:int):
            return 1 if mi==ni else 0
        otp = self.MATRIX(
            len(M),
            len(M[0]), 
            identity_slot
        )
        while(pow>0):
            if pow%2!=0: otp = self.matrix_mul(otp, M)
            M = self.matrix_mul(M,M)
            pow >>= 1
        return otp
    def lengthAfterTransformations(self, s: str, t: int, nums: list[int]) -> int:
        n = len(s)

        freq = [0]*26
        for char in s: freq[ord(char)-97]+=1

        trans_matrix = self.MATRIX(26,26,0)
        for mi in range(26):
            for i in range(1, nums[mi]+1):
                trans_matrix[mi][(mi+i)%26] = 1

        trans_matrix = self.matrix_exp(
            trans_matrix,
            t
        )

        otp = self.matrix_mul(
            [freq],
            trans_matrix
        )

        cnt=0
        for otp_freq in range(26): cnt = self.mod_add(
            cnt, otp[0][otp_freq]
        )
        return cnt
        

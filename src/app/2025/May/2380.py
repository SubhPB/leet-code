'''
2380. Time Needed to Rearrange a Binary String
Solved
Medium
Topics
Companies
Hint
You are given a binary string s. In one second, all occurrences of "01" are simultaneously replaced with "10". This process repeats until no occurrences of "01" exist.

Return the number of seconds needed to complete this process.

 

Example 1:

Input: s = "0110101"
Output: 4
Explanation: 
After one second, s becomes "1011010".
After another second, s becomes "1101100".
After the third second, s becomes "1110100".
After the fourth second, s becomes "1111000".
No occurrence of "01" exists any longer, and the process needed 4 seconds to complete,
so we return 4.
Example 2:

Input: s = "11100"
Output: 0
Explanation:
No occurrence of "01" exists in s, and the processes needed 0 seconds to complete,
so we return 0.
 

Constraints:

1 <= s.length <= 1000
s[i] is either '0' or '1'.


python ./src/app/2025/May/2380.py
'''

class Solution:
    def secondsToRemoveOccurrences(self, s: str) -> int:
        secs = 0
        ls = s.split("01")
        while len(ls)>1:
            ls = "10".join(ls).split("01")
            secs+=1
        return secs
    

if __name__ == '__main__':
    Testcases = [
        bin(i)[2:] for i in range(1, 100)
    ]

    for case in Testcases:
        trans = Solution().secondsToRemoveOccurrences(case)
        print(f'Case={case} secs={len(trans)-1} trans={trans}')
from typing import List
class Solution:
    '''
    3839. Number of Prefix Connected Groups

    You are given an array of strings words and an integer k.
    Two words a and b at distinct indices are prefix-connected if a[0..k-1] == b[0..k-1].
    A connected group is a set of words such that each pair of words is prefix-connected.
    Return the number of connected groups that contain at least two words, formed from the given words.Note:

    Words with length less than k cannot join any group and are ignored.
    Duplicate strings are treated as separate words.

    Example 1:
    Input: words = ["apple","apply","banana","bandit"], k = 2
    Output: 2
    Explanation:
    Words sharing the same first k = 2 letters are grouped together:
    words[0] = "apple" and words[1] = "apply" share prefix "ap".
    words[2] = "banana" and words[3] = "bandit" share prefix "ba".
    Thus, there are 2 connected groups, each containing at least two words.

    Constraints:
    1 <= words.length <= 5000
    1 <= words[i].length <= 100
    1 <= k <= 100
    All strings in words consist of lowercase English letters.
    '''
    def prefixConnected(self, words: List[str], k: int) -> int:
        dt={};res=0
        for word in words:
            key=word[:k]
            if len(key)>=k: dt[key]=1+dt.get(key,0)
        for key in dt: res+=int(dt[key]>1)
        return res
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    '''
    3997. Count Dominant Nodes in a Binary Tree

    You are given the root of a complete binary tree.
    A node x is called dominant if its value is equal to the maximum value among all nodes in the subtree rooted at x.
    Return the number of dominant nodes in the tree.

    Constraints:
    The number of nodes in the tree is in the range [1, 10**5].
    1 <= Node.val <= 10**9
    The tree is guaranteed to be a complete binary tree.
    '''
    def countDominantNodes(self, root: TreeNode | None) -> int:
        res=0
        def fn(node: TreeNode | None):
            if node is None: return 0
            lval=fn(node.left)
            rval=fn(node.right)
            if node.val>=max(lval,rval):
                nonlocal res    
                res+=1
            return max(node.val,lval,rval)
        fn(root)
        return res
    '''
    3998. Transform Binary String Using Subsequence Sort

    You are given a binary string s.
    You are also given an array of strings strs, where each strs[i] has the same length as s and consists of characters '0', '1', and '?'.
    Each '?' can be replaced by either '0' or '1'.

    You may perform the following operation any number of times (including zero):
    Choose any subsequence sub of s.
    Sort sub in non-decreasing order.
    Replace the chosen subsequence in s with the sorted sub, keeping all other characters unchanged.
    Return a boolean array ans, where ans[i] is true if it's possible to replace all '?' in strs[i] with '0' or '1'
    and transform s into the resulting string using the allowed operation above, otherwise return false.


    Example 1:
    Input: s = "101", strs = ["1?1","0?1","0?0"]
    Output: [true,true,false]

    Explanation:
    i	strs[i]	Replacement	Result strs[i]	Operation(s)	Result
    0	"1?1"	? → 0	"101"	Matches s.	true
    1	"0?1"	? → 1	"011"	Select the subsequence at indices [0..2] of s → "101".
    Sort "101" to get "011" = strs[i].	true
    2	"0?0"	? → 0 or 1	"000" or "010"	Not feasible.	false
    Thus, ans = [true, true, false].

    Constraints:
    1 <= n == s.length <= 2000
    s[i] is either '0' or '1'.
    1 <= strs.length <= 2000
    strs[i].length == n
    strs[i] is either '0', '1', or '?'​​​​​​​.
    '''
    def transformStr(self, s: str, strs: list[str]) -> list[bool]:
        cnt1=s.count('1')
        for i,st in enumerate(strs):
            cnt2=st.count('1')
            if cnt1>=cnt2:
                strs[i]=cnt2+st.count('?')>=cnt1
            else:
                strs[i]=False
        return strs
    '''
    3999. Minimum Number of String Groups Through Transformations

    You are given an array of strings words.
    Define a transformation on a string s as follows:
    Let E be the subsequence of characters at even indices of s.
    Let O be the subsequence of characters at odd indices of s.
    Independently cyclically shift E and O by any number of positions to the right, possibly zero.
    Reconstruct the string by placing the shifted E characters back into even indices and the shifted O characters back into odd indices.
    Two strings are equivalent if one can be transformed into the other by a single transformation.
    Partition words into the minimum number of groups such that:
    Every string belongs to exactly one group.
    Every pair of strings in the same group are equivalent.
    Return an integer denoting the minimum number of groups.

    Example 1:
    Input: words = ["ntgwz","zwntg"]
    Output: 1
    
    Constraints:
    1 <= words.length <= 10**5
    1 <= words[i].length <= 5 * 10**5
    The sum of words[i].length does not exceed 5 * 10**5.
    words[i] consist of lowercase English letters.
    '''
    def minimumGroups(self, words: list[str]) -> int:
        pass
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
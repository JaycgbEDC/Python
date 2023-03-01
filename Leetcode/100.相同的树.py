#
# @lc app=leetcode.cn id=100 lang=python3
#
# [100] 相同的树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        """ others """
        if p and q:
            return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        return p is q  # both NULL or one NULL
    
    def func1(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        """ bymyself: use preorder """
        if (not p and not q):  # both NULL
            return True
        if (p and not q) or (not p and q):  # one NULL
            return False
        if p.val != q.val:  # not equal
            return False
        return (self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right))
    
# @lc code=end


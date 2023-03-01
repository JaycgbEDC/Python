#
# @lc app=leetcode.cn id=94 lang=python3
#
# [94] 二叉树的中序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """ bymyself: iterative """
        res = []
        stack = []
        rtag = 0
        temp = root
        while root or (len(stack) != 0):
            if root:
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                res.append(root.val)
                root = root.right
        return res
    
    def func1(self, root: Optional[TreeNode]) -> List[int]:
        """ bymyself: recurse """
        if not root:
            return []
        return (self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right))

# @lc code=end


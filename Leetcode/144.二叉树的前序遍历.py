#
# @lc app=leetcode.cn id=144 lang=python3
#
# [144] 二叉树的前序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """ recursive """
        def preorder(root, l):
            if root:
                l.append(root.val)
                preorder(root.left, l)
                preorder(root.right, l)
        l = []
        preorder(root, l)
        return l
    
    def func_iterative(self, root: Optional[TreeNode]) -> List[int]:
        ret = []
        stack = [root]
        while root:
            node = stack.pop()
            if node:
                ret.append(node.val)
                stack.append(node.right)
                stack.append(node.left)
        return ret

# @lc code=end


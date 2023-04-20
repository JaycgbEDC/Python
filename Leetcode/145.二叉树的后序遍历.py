#
# @lc app=leetcode.cn id=145 lang=python3
#
# [145] 二叉树的后序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def post_order(root, l):
            if root:
                post_order(root.left, l)
                post_order(root.right, l)
                l.append(root.val)
        l = []
        post_order(root, l)
        return l

# @lc code=end


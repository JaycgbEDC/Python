#
# @lc app=leetcode.cn id=112 lang=python3
#
# [112] 路径总和
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        """ bymyself: recurse-postorder """
        def postorder(root, tsum):
            if root:
                l = postorder(root.left, tsum-root.val)
                r = postorder(root.right, tsum-root.val)
                if l == True or r == True or (not root.left) and (not root.right) and (tsum == root.val):
                    return True
        
        return postorder(root, targetSum) == True

# @lc code=end


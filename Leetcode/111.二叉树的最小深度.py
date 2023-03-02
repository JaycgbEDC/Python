#
# @lc app=leetcode.cn id=111 lang=python3
#
# [111] 二叉树的最小深度
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        """ others: level-travesal """
        if not root:
            return 0
        from collections import deque
        q = deque([(root, 1)])
        while q:
            node, levels = q.popleft()
            if node:
                if not node.left and not node.right:  # children all None
                    return levels
                q.append((node.left, levels+1))
                q.append((node.right, levels+1))
    
    def func1(self, root: Optional[TreeNode]) -> int:
        """ bymyself: recurse """
        if not root:
            return 0
        h_l = self.minDepth(root.left)
        h_r = self.minDepth(root.right)
        if h_l == 0 or h_r == 0:
            return max(h_l, h_r) + 1
        return min(h_l, h_r) + 1

# @lc code=end


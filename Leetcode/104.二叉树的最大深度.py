#
# @lc app=leetcode.cn id=104 lang=python3
#
# [104] 二叉树的最大深度
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        """ others:  level-traversal"""
        from collections import deque
        if not root:
            return 0
        q = deque([root])
        cur_level_nodenum = 1
        levels = 0
        while q:
            node = q.popleft()
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
            cur_level_nodenum -= 1
            if cur_level_nodenum == 0:
                levels += 1
                cur_level_nodenum = len(q)
        return levels
    
    def func1(self, root: Optional[TreeNode]) -> int:
        """ bymyself: recurse """
        if not root:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
        
# @lc code=end


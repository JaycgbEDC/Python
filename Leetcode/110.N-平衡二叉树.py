#
# @lc app=leetcode.cn id=110 lang=python3
#
# [110] 平衡二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        """ others: iterative """
        stack, ptag, depths = [], None, {}
        while root or stack:
            if root:
                stack.append(root)
                root = root.left
            else:
                root = stack[-1]
                if root.right and root.right != ptag:
                    root = root.right
                else:
                    root = stack.pop()
                    h_l, h_r = depths.get(root.left, 0), depths.get(root.right, 0)
                    if abs(h_l - h_r) > 1:
                        return False
                    depths[root] = max(h_l, h_r) + 1
                    ptag = root
                    root = None
        return True
    
    def func1(self, root: Optional[TreeNode]) -> bool:
        """ others: recurse """
        def check(root):
            if not root:
                return 0
            h_l = check(root.left)
            h_r = check(root.right)
            if h_r == -1 or h_l == -1 or abs(h_l - h_r) > 1:
                return -1
            return max(h_l, h_r) + 1
        
        return check(root) != -1

# @lc code=end


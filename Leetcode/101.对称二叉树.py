#
# @lc app=leetcode.cn id=101 lang=python3
#
# [101] 对称二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        """ bymyself: iterative """
        stack1 = []
        stack2 = []
        p1, p2 = root.left, root.right
        while (p1 and p2) or len(stack1) != 0:
            if p1 and p2:
                if p1.val != p2.val:
                    return False
                else:
                    stack1.append(p1)
                    stack2.append(p2)
                    p1 = p1.left
                    p2 = p2.right
            elif (p1 and not p2) or (not p1 and p2):
                return False
            else:
                p1 = stack1.pop()
                p2 = stack2.pop()
                p1 = p1.right
                p2 = p2.left
        return p1 is p2
    
    def func1(self, root: Optional[TreeNode]) -> bool:
        """ bymyself: recurse, familar-100 """
        def judge(root1, root2):
            if root1 and root2:
                return root1.val == root2.val and judge(root1.left, root2.right) and judge(root1.right, root2.left)
            return root1 is root2
        return judge(root.left, root.right)

# @lc code=end


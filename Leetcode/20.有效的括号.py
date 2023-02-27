#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号: valid('{[]}') invalid('([)}')
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        """ others: use dict and stack """
        d = {'(': ')', '{': '}', '[': ']'}
        stack = []
        for i in s:
            if i in d:
                stack.append(i)
            elif len(stack) == 0 or d[stack.pop()] != i:
                return False
        return len(stack) == 0
    
    def func1(self, s: str) -> bool:
        """ bymyself: use stack """
        stack = []
        for ch in s:
            if ch in '({[':  # 左进栈
                stack.append(ch)
            elif len(stack) == 0 or ''.join([stack.pop(), ch]) not in ['()', '[]', '{}']:  # 右出判断
                return False
        return len(stack) == 0
            
# @lc code=end


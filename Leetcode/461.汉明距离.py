#
# @lc app=leetcode.cn id=461 lang=python3
#
# [461] 汉明距离
#

# @lc code=start
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        """ others """
        return str(bin(x^y)).count('1')  # 异或运算^
    
    def func1(self, x: int, y: int) -> int:
        """ bymyself """
        count = 0
        x, y = bin(x)[2::], bin(y)[2::]
        if len(x) < len(y):
            for _ in range(len(y) - len(x)):
                x = '0' + x
        elif len(x) > len(y):
            for _ in range(len(x) - len(y)):
                y = '0' + y
        for i, ch in enumerate(x):
            if ch != y[i]:
                count += 1
        return count

# @lc code=end


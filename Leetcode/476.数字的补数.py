#
# @lc app=leetcode.cn id=476 lang=python3
#
# [476] 数字的补数
#

# @lc code=start
class Solution:
    def findComplement(self, num: int) -> int:
        num_b = bin(num)[2:]
        num_r = ''
        for ch in num_b:
            if ch == '0':
                num_r += '1'
            else:
                num_r += '0'
        return int(num_r, 2)

# @lc code=end


#
# @lc app=leetcode.cn id=1323 lang=python3
#
# [1323] 6 和 9 组成的最大数字
#

# @lc code=start
class Solution:
    def maximum69Number (self, num: int) -> int:
        num = str(num)
        res = ''
        for i, ch in enumerate(num):
            if ch == '6':
                res += '9'
                res += num[i + 1::]
                break
            res += ch
        return int(res)
        
# @lc code=end


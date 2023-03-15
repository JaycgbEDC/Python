#
# @lc app=leetcode.cn id=168 lang=python3
#
# [168] Excel表列名称
#

# @lc code=start
class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        res = ''
        while columnNumber:
            columnNumber, rem = divmod(columnNumber-1, 26)  # col要减一
            res = chr(ord('A') + rem) + res
        return res

# @lc code=end


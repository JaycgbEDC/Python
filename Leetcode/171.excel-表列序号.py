#
# @lc app=leetcode.cn id=171 lang=python3
#
# [171] Excel 表列序号
#

# @lc code=start
class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        res = count = 0
        for ch in columnTitle[::-1]:
            res += (ord(ch) - ord('A') + 1)*26**(count)
            count += 1
        return res

# @lc code=end


#
# @lc app=leetcode.cn id=409 lang=python3
#
# [409] 最长回文串
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> int:
        res = 0
        l = list(set(s))
        for ch in l:
            if s.count(ch) % 2 == 0:
                res += s.count(ch)
            elif s.count(ch) > 2:
                res += s.count(ch) - 1
        if len(s) - res != 0:
            return res + 1
        return res

# @lc code=end


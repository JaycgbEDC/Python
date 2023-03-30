#
# @lc app=leetcode.cn id=125 lang=python3
#
# [125] 验证回文串
#

# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        temp = ''
        for i in s:
            if i.isalnum():
                temp += i.lower()
        return temp == temp[::-1]

# @lc code=end


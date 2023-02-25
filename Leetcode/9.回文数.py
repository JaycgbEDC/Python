#
# @lc app=leetcode.cn id=9 lang=python3
#
# [9] 回文数
#

# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        """ first: using str """
        if x < 0:
            return False
        return str(x) == str(x)[::-1]
    
    def func1(self, x: int) -> bool:
        """ second: without using str """
        if x < 0:
            return False
        inputnum = x
        newnum = 0
        while x > 0:
            newnum = newnum * 10 + x % 10
            x //= 10
        return newnum == inputnum

    def func2(self, x: int) -> bool:
        """ third:  without using str and faster, avoid crossing bounds"""
        if x < 0 or (x > 0 and x % 10 == 0):  # 小于0或者大于0时以0结尾不是回文
            return False
        revx = 0
        while x > revx:
            revx = revx * 10 + x % 10
            x //= 10
        return True if (x == revx or x == revx // 10) else False

# @lc code=end


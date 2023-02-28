#
# @lc app=leetcode.cn id=67 lang=python3
#
# [67] 二进制求和
#

# @lc code=start
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        """ others: """
        res = ''
        i, j, carry = len(a) - 1, len(b) - 1, 0
        while i >= 0 or j >= 0:
            sum = carry
            if i >= 0:
                sum += ord(a[i]) - ord('0')
            if j >= 0:
                sum += ord(b[j]) - ord('0')
            carry = 1 if sum > 1 else 0
            res = str(sum % 2) + res
            i , j = i - 1, j - 1
        if carry == 1:
            res = '1' + res
        return res
    
    def func1(self, a: str, b: str) -> str:
        """ bymyself: easy idea(space good) """
        return str(bin(int(a, base=2) + int(b, base=2)))[2:]

# @lc code=end


#
# @lc app=leetcode.cn id=263 lang=python3
#
# [263] 丑数
#

# @lc code=start
class Solution:
    def isUgly(self, n: int) -> bool:
        """ others """
        for p in 2, 3, 5:
            while n % p == 0 < n:
                n //= p
        return n == 1
    
    def func1(self, n: int) -> bool:
        """ bymyself """
        if n <= 0:
            return False
        if n == 1:
            return True
        while n != 2 and n != 3 and n != 5:
            if n % 2 == 0:
                n //= 2
            elif n % 3 == 0:
                n //= 3
            elif n % 5 == 0:
                n //= 5
            else:
                return False
        return True

# @lc code=end


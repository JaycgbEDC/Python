#
# @lc app=leetcode.cn id=69 lang=python3
#
# [69] x 的平方根 
#

# @lc code=start
class Solution:
    def mySqrt(self, x: int) -> int:
        """ others: binary_search, Suda mooc ocurred """
        l, r = 0, x
        while l <= r:
            mid = (l + r) // 2
            if mid * mid <= x < (mid + 1) * (mid + 1):
                return mid
            elif x < mid * mid:
                r = mid -1
            else:
                l = mid + 1
            
    def func1(self, x: int) -> int:
        """ bymyself: bad efficiency """
        if x == 0:
            return 0
        if 1 <= x <= 3:
            return 1
        if x == 4 or x == 5:
            return 2
        for i in range(1, (x // 2) + 1):  # when x > 4
            if i * i > x:
                return (i - 1)

# @lc code=end


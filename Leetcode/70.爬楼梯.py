#
# @lc app=leetcode.cn id=70 lang=python3
#
# [70] 爬楼梯
#

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        """ others: dp-problem. climb = [0, 1, 2, climb(3)=climb(1)+climb(2), ..., climb(n)=climb(n-2)+climb(n-1)] """
        if n == 1:
            return 1
        if n == 2:
            return 2
        dp = [0] * (n+1)
        dp[1] = 1
        dp[2] = 2
        for i in range(3, n+1):
            dp[i] = dp[i-2] + dp[i-1]
        return dp[n]

    def func1(self, n: int) -> int:
        """ bymyself:  recurse"""
        def sol(start):
            if start == n:
                return (1, 0)
            a, b = sol(start+1)
            return (a+b, a)
        return sol(0)[0]

# @lc code=end


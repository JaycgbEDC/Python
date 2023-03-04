#
# @lc app=leetcode.cn id=509 lang=python3
#
# [509] 斐波那契数
#

# @lc code=start
class Solution:
    def fib(self, n: int) -> int:
        """ others: iterative """
        a, b = 0, 1
        for _ in range(n):
            a, b = b, a+b
        return a
    
    def func1(self, n: int) -> int:
        """ bymyself: recurse """
        def sol(n):
            if n <= 1:
                return [n, 0]
            a, b = sol(n-1)
            return [a + b, a]
        return sol(n)[0]

# @lc code=end


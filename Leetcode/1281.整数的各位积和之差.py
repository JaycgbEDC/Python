#
# @lc app=leetcode.cn id=1281 lang=python3
#
# [1281] 整数的各位积和之差
#

# @lc code=start
class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        """ others """
        return eval('*'.join(str(n))) - eval('+'.join(str(n)))

    def func1(self, n: int) -> int:
        """ bymyself """
        mul, sum = 1, 0
        while n != 0:
            n, temp = divmod(n, 10)
            mul *= temp
            sum += temp
        return mul - sum

# @lc code=end


#
# @lc app=leetcode.cn id=121 lang=python3
#
# [121] 买卖股票的最佳时机
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        min_p = prices[0]
        for i in prices:
            if i - min_p > res:
                res = i - min_p
            elif i < min_p:
                min_p = i
        return res

# @lc code=end


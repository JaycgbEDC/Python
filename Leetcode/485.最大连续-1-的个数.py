#
# @lc app=leetcode.cn id=485 lang=python3
#
# [485] 最大连续 1 的个数
#

# @lc code=start
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        temp = res =  0
        for num in nums:
            if num == 1:
                temp += 1
            res = max(res, temp)
            if num == 0:
                temp = 0
        return res

# @lc code=end


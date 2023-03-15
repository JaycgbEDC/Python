#
# @lc app=leetcode.cn id=561 lang=python3
#
# [561] 数组拆分
#

# @lc code=start
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort(reverse = True)
        sum = 0
        for num in nums[1::2]:
            sum += num
        return sum

# @lc code=end


#
# @lc app=leetcode.cn id=628 lang=python3
#
# [628] 三个数的最大乘积
#

# @lc code=start
class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        if len(nums) == 3:
            return nums[0] * nums[1] * nums[2]
        nums.sort()
        count_p = count_n = 0
        for num in nums:
            if num > 0:
                count_p += 1
            if num < 0:
                count_n += 1
        if count_n <= 1 or count_p == 0:
            return nums[-1] * nums[-2] * nums[-3]
        if count_n >= 2:
            if nums[-1] * nums[-2] * nums[-3] >= nums[0] * nums[1] * nums[-1]:
                return nums[-1] * nums[-2] * nums[-3]
            return nums[0] * nums[1] * nums[-1]

# @lc code=end


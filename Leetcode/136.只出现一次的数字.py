#
# @lc app=leetcode.cn id=136 lang=python3
#
# [136] 只出现一次的数字
#

# @lc code=start
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(len(nums))[::2]:
            if i + 1 < len(nums) and nums[i] == nums[i + 1]:
                continue
            elif i == len(nums) - 1 or nums[i] != nums[i + 1]:
                return nums[i]
                
# @lc code=end


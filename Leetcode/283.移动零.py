#
# @lc app=leetcode.cn id=283 lang=python3
#
# [283] 移动零
#

# @lc code=start
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        zero = 0  # record 0 position
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[zero] = nums[zero], nums[i]
                zero += 1

    def func1(self, nums: List[int]) -> None:
        """ bymyself """
        count_zero = 0
        for i, num in enumerate(nums):
            if num == 0:
                count_zero += 1
            else:
                nums[i-count_zero] = num
        for i in range(count_zero):
            nums[-1-i] = 0

# @lc code=end


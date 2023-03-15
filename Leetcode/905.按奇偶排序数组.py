#
# @lc app=leetcode.cn id=905 lang=python3
#
# [905] 按奇偶排序数组
#

# @lc code=start
class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            if nums[i] % 2 != 0:
                for j in range(i+1, len(nums)):
                    if nums[j] % 2 == 0:
                        temp = nums[j]
                        nums[j] = nums[i]
                        nums[i] = temp
                        break
        return nums

# @lc code=end


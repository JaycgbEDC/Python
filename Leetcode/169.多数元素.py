#
# @lc app=leetcode.cn id=169 lang=python3
#
# [169] 多数元素
#

# @lc code=start
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        l = list(set(nums))
        for num in l:
            if nums.count(num) > len(nums) // 2:
                return num

# @lc code=end


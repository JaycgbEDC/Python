#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """ best: use dict """
        d = {}
        for index, num in enumerate(nums):
            temp = target - num
            if temp in d:
                return [d[temp], index]
            d[num] = index
    
    def func2(self, nums: List[int], target: int) -> List[int]:
        """ myself_improved """
        for i in range(0, len(nums)):
            temp = nums.count(target - nums[i])
            if temp and i != nums.index(target - nums[i]):
                return [i, nums.index(target - nums[i])]
    
    def func3(self, nums: List[int], target: int) -> List[int]:
        """ improved by others """
        for index1, num in enumerate(nums):
            temp = target - num
            try:
                index2 = nums.index(temp)
            except ValueError:
                continue
            if index1 !=index2:
                return [index1, index2]
            
# @lc code=end


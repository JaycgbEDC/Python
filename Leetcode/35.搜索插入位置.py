#
# @lc app=leetcode.cn id=35 lang=python3
#
# [35] 搜索插入位置
#

# @lc code=start
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        """ bymyself:  binary search"""
        i, j = 0, len(nums) - 1
        while i <= j:
            mid = (i + j) // 2  # 这里没加括号结果超时
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                i = mid + 1
            else:
                j = mid - 1
        return i
    
    def func1(self, nums: List[int], target: int) -> int:
        pass

# @lc code=end


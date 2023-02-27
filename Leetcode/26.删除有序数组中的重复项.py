#
# @lc app=leetcode.cn id=26 lang=python3
#
# [26] 删除有序数组中的重复项
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """ others: good """
        unique_ind = 1
        for index in range(len(nums) - 1):
            if(nums[index] != nums[index + 1]):
                nums[unique_ind] = nums[index + 1]
                unique_ind += 1
        return unique_ind
    
    def fucn1(self, nums: List[int]) -> int:
        """ bymyself: bad efficiency """
        temp = nums[0]
        for num in nums[1:]:
            if num == temp:
                nums.remove(num)
            else:
                temp = num
        return len(nums)
            
# @lc code=end


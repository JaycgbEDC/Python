#
# @lc app=leetcode.cn id=27 lang=python3
#
# [27] 移除元素
#

# @lc code=start
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        """ others: familar-26, space good """
        i = 0
        for x in nums:
            if x != val:
                nums[i] = x
                i += 1
        return i
    
    def func1(self, nums: List[int], val: int) -> int:
        """ bymyself """
        for i in range((len(nums)))[::-1]:
            if nums[i] == val:
                del nums[i]
        return len(nums)
                
# @lc code=end


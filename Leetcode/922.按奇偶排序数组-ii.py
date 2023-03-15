#
# @lc app=leetcode.cn id=922 lang=python3
#
# [922] 按奇偶排序数组 II
#

# @lc code=start
class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        """ others: double pointer """
        j = 1
        for i in range(len(nums))[::2]:
            if nums[i] % 2 != 0:
                while nums[j] % 2 != 0:
                    j += 2
                temp = nums[j]
                nums[j] = nums[i]
                nums[i] = temp
        return nums
    
    def func1(self, nums: List[int]) -> List[int]:
        """ bymyself """
        odd = []
        even = []
        res = []
        for i in nums:
            if i % 2 == 0:
                even.append(i)
            else:
                odd.append(i)
        for i in range(len(odd)):
            res.append(even[i])
            res.append(odd[i])
        return res

# @lc code=end


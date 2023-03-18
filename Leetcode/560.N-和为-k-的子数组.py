#
# @lc app=leetcode.cn id=560 lang=python3
#
# [560] 和为 K 的子数组
#

# @lc code=start
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        """ method1 """
        prefixSum = ans =  0
        d = {0: 1}
        for num in nums:
            prefixSum += num
            if prefixSum - k in d:
                ans += d[prefixSum - k]
            d[prefixSum] = d.get(prefixSum, 0) + 1
        return ans 
    
    def func1(self, nums: List[int], k: int) -> int:
        """ method2 """
        ans = 0
        for end in range(len(nums)):
            sum = 0
            for start in range(end + 1)[::-1]:
                sum += nums[start]
                if sum == k:
                    ans += 1
        return ans

# @lc code=end


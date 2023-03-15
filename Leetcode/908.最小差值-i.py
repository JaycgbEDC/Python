#
# @lc app=leetcode.cn id=908 lang=python3
#
# [908] 最小差值 I
#

# @lc code=start
class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        """ bymyself: math problem """
        if min(nums) + k >= max(nums) - k:
            return 0
        return max(nums) - min(nums) - 2*k

# @lc code=end


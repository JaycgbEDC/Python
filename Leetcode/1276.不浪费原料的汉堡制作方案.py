#
# @lc app=leetcode.cn id=1276 lang=python3
#
# [1276] 不浪费原料的汉堡制作方案
#

# @lc code=start
class Solution:
    def numOfBurgers(self, tomatoSlices: int, cheeseSlices: int) -> List[int]:
        x, rem = divmod(tomatoSlices - 2 * cheeseSlices, 2)
        if x < 0 or rem == 1 or cheeseSlices - x < 0:
            return []
        return [x, cheeseSlices - x]

# @lc code=end


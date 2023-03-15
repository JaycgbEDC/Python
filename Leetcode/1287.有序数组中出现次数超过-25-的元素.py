#
# @lc app=leetcode.cn id=1287 lang=python3
#
# [1287] 有序数组中出现次数超过25%的元素
#

# @lc code=start
class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        from collections import Counter
        return Counter(arr).most_common(1)[0][0]

# @lc code=end


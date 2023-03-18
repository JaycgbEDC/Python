#
# @lc app=leetcode.cn id=914 lang=python3
#
# [914] 卡牌分组
#

# @lc code=start
class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        """ others """
        from functools import reduce
        from math import gcd
        from collections import Counter

        return reduce(gcd, Counter(deck).values()) != 1

# @lc code=end


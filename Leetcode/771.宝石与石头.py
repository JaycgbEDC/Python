#
# @lc app=leetcode.cn id=771 lang=python3
#
# [771] 宝石与石头
#

# @lc code=start
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        from collections import Counter
        return sum(Counter(stones)[i] for i in jewels)
    
    def func1(self, jewels: str, stones: str) -> int:
        """ bymyself """
        count = 0
        for ch in stones:
            if jewels.find(ch) != -1:
                count += 1
        return count

# @lc code=end


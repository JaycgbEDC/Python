#
# @lc app=leetcode.cn id=888 lang=python3
#
# [888] 公平的糖果交换
#

# @lc code=start
class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        """ others """
        difference = (sum(aliceSizes) - sum(bobSizes)) / 2
        A = set(aliceSizes)
        for candy in set(bobSizes):
            if difference + candy in A:
                return [difference + candy, candy]
        
    def func1(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        """ bymyself """
        t_sub = sum(bobSizes) - sum(aliceSizes)
        for i in aliceSizes:
            if bobSizes.count(i + t_sub // 2) != 0:
                return [i, i + t_sub // 2]

# @lc code=end


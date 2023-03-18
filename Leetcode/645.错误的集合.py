#
# @lc app=leetcode.cn id=645 lang=python3
#
# [645] 错误的集合
#

# @lc code=start
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        """ others """
        n, a, b = len(nums), sum(nums), sum(set(nums))
        s = n * (n + 1) // 2
        return [a - b, s - b]
    
    def func1(self, nums: List[int]) -> List[int]:
        """ bymyself """
        res = []
        l = list(set(nums))
        for num in l:
            if nums.count(num) == 2:
                res.append(num)
        for i, num in enumerate(l):
            if num != i + 1:
                res.append(i + 1)
                break
        if len(res) == 1:
            res.append(len(nums))
        return res

# @lc code=end


#
# @lc app=leetcode.cn id=46 lang=python3
#
# [46] 全排列
#

# @lc code=start
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """ others """
        from itertools import permutations
        return list(permutations(nums))

    def func1(self, nums: List[int]) -> List[List[int]]:
        """ others """
        def sol(self, l, path: List[int], res):
            if not l:
                res.append(path)
            for i in range(len(l)):
                self.sol(l[:i] + l[i + 1:], path + [l[i]], res)
        res = []
        self.sol(nums, [], res)
        return res

# @lc code=end


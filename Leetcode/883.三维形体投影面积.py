#
# @lc app=leetcode.cn id=883 lang=python3
#
# [883] 三维形体投影面积
#

# @lc code=start
class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        """ others """
        s_xy = sum(num > 0 for row in grid for num in row)
        s_yz = sum(map(max, grid))
        s_zx = sum(map(max, zip(*grid)))
        return s_xy + s_yz + s_zx
    
    def func1(self, grid: List[List[int]]) -> int:
        """ bymyself """
        s_xy = 0
        s_yz = [0]*len(grid)
        s_zx = [0]*len(grid)
        for i, num1 in enumerate(grid):
            for j, num2 in enumerate(grid[i]):
                if num2 != 0:
                    s_xy += 1
                    if num2 > s_yz[j]:
                        s_yz[j] = num2
            s_zx[i] = max(grid[i])
        return s_xy + sum(s_yz) + sum(s_zx)

# @lc code=end


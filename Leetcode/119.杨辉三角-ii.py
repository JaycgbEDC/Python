#
# @lc app=leetcode.cn id=119 lang=python3
#
# [119] 杨辉三角 II
#

# @lc code=start
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        """ others : use permutation-combination """
        pascal = [1]*(rowIndex+1)
        up = rowIndex
        down = 1
        for col in range(1, rowIndex):
            pascal[col] = pascal[col-1]*up//down
            up -= 1
            down += 1
        return pascal
    
    def func1(self, rowIndex: int) -> List[int]:
        """ bymyself """
        def sol_pascal(numRow):
            pascal = [[1]*(i+1) for i in range(numRow)]
            for row in range(numRow):
                for col in range(1, row):
                    pascal[row][col] = pascal[row-1][col-1] + pascal[row-1][col]
            return pascal
        
        return sol_pascal(rowIndex+1)[rowIndex]

# @lc code=end


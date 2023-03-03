#
# @lc app=leetcode.cn id=118 lang=python3
#
# [118] 杨辉三角
#

# @lc code=start
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        """ others """
        pascal = [[1]*(i+1) for i in range(numRows)]
        for row in range(numRows):
            for col in range(1, row):
                pascal[row][col] = pascal[row-1][col-1] + pascal[row-1][col]
        return pascal
    
    def func1(self, numRows: int) -> List[List[int]]:
        """ bymyself """
        res = []
        for row in range(numRows):
            res.append([]) 
            res[row].append(1)
            for num in range(row-1):
                res[row].append(res[row-1][num] + res[row-1][num+1])
            if row >= 1:
                res[row].append(1)
        return res

# @lc code=end


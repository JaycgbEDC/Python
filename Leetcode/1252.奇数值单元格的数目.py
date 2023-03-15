#
# @lc app=leetcode.cn id=1252 lang=python3
#
# [1252] 奇数值单元格的数目
#

# @lc code=start
class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        """ others: good efficiency """
        rows = [0] * m
        cols = [0] * n
        for x, y in indices:
            rows[x] += 1
            cols[y] += 1
        oddx = sum(rows[i] % 2 for i in range(m))
        oddy = sum(cols[i] % 2 for i in range(n))
        return oddx * (n - oddy) + (m - oddx) * oddy
    
    def func1(self, m: int, n: int, indices: List[List[int]]) -> int:
        """ bymyself """
        count = 0
        l_b = []
        for r in range(m):  # 产生m*n值为0的矩阵：matrix = [[0 for i in range(m)] for j in range(n)]
            temp = []
            for c in range(n):
                temp.append(0)
            l_b.append(temp)
        for l in indices:
            r, c = l
            for i in range(n):
                l_b[r][i] += 1
            for j in range(m):
                l_b[j][c] += 1
        for i in range(m):
            for j in range(n):
                if l_b[i][j] % 2 != 0:
                    count += 1
        return count

# @lc code=end


#
# @lc app=leetcode.cn id=821 lang=python3
#
# [821] 字符的最短距离
#

# @lc code=start
class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        res = [0]*len(s)
        index = [i for i in range(len(s)) if s[i] == c]
        r = 1
        if r < len(index):
            p1, p2 = index[r-1], index[r]
        else:
            p1 = p2 = index[0]
        for i in range(len(s)):
            if i < p1:
                res[i] = p1 - i
            elif i == p1:
                res[i] = 0
            elif p1 < i < p2:
                res[i] = min(abs(i - p1), abs(p2 - i))
            elif i == p2:
                res[i] = 0
                p1 = p2
                r += 1
                if r < len(index):
                    p2 = index[r]
            else:
                res[i] = i - p1
        return res

# @lc code=end


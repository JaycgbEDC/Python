#
# @lc app=leetcode.cn id=1078 lang=python3
#
# [1078] Bigram 分词
#

# @lc code=start
class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        res = []
        temp = text.split()
        if len(temp) < 3:
            return []
        for index, s in enumerate(temp):
            if s == first and (index + 2 < len(temp)):
               if temp[index+1] == second:
                   res.append(temp[index+2])
        return res

# @lc code=end


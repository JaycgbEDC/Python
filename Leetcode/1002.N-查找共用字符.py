#
# @lc app=leetcode.cn id=1002 lang=python3
#
# [1002] 查找共用字符
#

# @lc code=start
class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        if len(words) == 1:
            return list(words[0])
        res = []
        comp = set(words[0])
        for ch in comp:
            n = min([s.count(ch) for s in words])
            res.extend([ch]*n)
        return res

# @lc code=end


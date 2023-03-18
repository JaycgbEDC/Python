#
# @lc app=leetcode.cn id=824 lang=python3
#
# [824] 山羊拉丁文
#

# @lc code=start
class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        l = sentence.split()
        for i, s in enumerate(l):
            if s[0].lower() in ('a', 'e', 'i', 'o', 'u'):
                l[i] = l[i] + 'ma'
            else:
                l[i] = s[1:] + s[0] + 'ma'
            l[i] = l[i] + 'a' * (i + 1)
        return ' '.join(l)

# @lc code=end


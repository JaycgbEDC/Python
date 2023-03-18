#
# @lc app=leetcode.cn id=290 lang=python3
#
# [290] 单词规律
#

# @lc code=start
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        """ others """
        l = s.split()
        return len(set(zip(pattern, l))) == len(set(pattern)) == len(set(l)) and len(l) == len(pattern)
    
    def func1(self, pattern: str, s: str) -> bool:
        """ bymyself """
        l = s.split()
        d = {}
        if len(l) != len(pattern):
            return False
        for i, ch in enumerate(pattern):
            temp = d.get(ch, '0')
            if temp == '0':
                if l[i] in d.values():
                    return False
                d[ch] = l[i]
            elif temp != l[i]:
                return False
        return True

# @lc code=end


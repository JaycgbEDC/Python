#
# @lc app=leetcode.cn id=58 lang=python3
#
# [58] 最后一个单词的长度
#

# @lc code=start
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        """ others: use split() """
        return len(s.split()[-1])
    
    def func1(self, s: str) -> int:
        """ bymyself: use re(bad efficiency) """
        import re
        pat = re.compile(r'[A-Za-z]+')
        l = pat.findall(s)
        return len(l[-1])
    
    def func2(self, s: str) -> int:
        """ bymyself: way2(time good) """
        count = 0
        for ch in s[::-1]:
            if 'A' <= ch <= 'z':
                count += 1
            elif count:
                break
        return count

# @lc code=end


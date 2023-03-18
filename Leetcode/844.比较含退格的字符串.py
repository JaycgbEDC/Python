#
# @lc app=leetcode.cn id=844 lang=python3
#
# [844] 比较含退格的字符串
#

# @lc code=start
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        """ others: TC-O(n)、SC-O(1) """
        i, j = len(s) - 1, len(t) - 1
        count1 = count2 = 0
        while i >= 0 or j >= 0:
            while i >= 0:
                if s[i] == '#':
                    count1 += 1
                    i -= 1
                elif count1 > 0:
                    count1 -= 1
                    i -= 1
                else:
                    break
            while j >= 0:
                if t[j] == '#':
                    count2 += 1
                    j -= 1
                elif count2 > 0:
                    count2 -= 1
                    j -= 1
                else:
                    break
            if i >= 0 and j >= 0 and s[i] != t[j]:
                return False
            if (i >= 0) != (j >= 0):
                return False
            i -= 1
            j -= 1
        return True
    
    def func1(self, s: str, t: str) -> bool:
        """ bymyself: use stack """
        def judge(s):
            l_s = []
            for ch in s:
                if ch != '#':
                    l_s.append(ch)
                elif l_s:
                    l_s.pop()
            return l_s
        
        return judge(s) == judge(t)

# @lc code=end


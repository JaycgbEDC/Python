#
# @lc app=leetcode.cn id=14 lang=python3
#
# [14] 最长公共前缀
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        """ others: traditional way """
        if strs[0] == '' or len(strs) == 1:
            return strs[0]
        for i in range(len(strs[0])):
            ch = strs[0][i]
            for j in range(1, len(strs)):
                if i == len(strs[j]) or strs[j][i] != ch:
                    return strs[0][:i]
        return strs[0]    
    
    def func1(self, strs: List[str]) -> str:
        """ bymyslef """
        res = strs[0]
        for i in strs[1::]:
            if res == '':
                break
            if res == i[:len(res)]:
                continue
            for index, ch in enumerate(i):
                if index == len(res):
                    break
                if ch != res[index]:
                    res = i[:index]
                    break
            else:
                res = i
        return res
    
    def func2(self, strs: List[str]) -> str:
        """ others: use list and zip functions """
        l = list(zip(*strs))
        res = ''
        for i in l:
            if len(set(i)) == 1:
                res += i[0]
            else:
                break
        return res
        
# @lc code=end


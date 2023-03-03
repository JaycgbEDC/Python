#
# @lc app=leetcode.cn id=953 lang=python3
#
# [953] 验证外星语词典
#

# @lc code=start
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        """ bymyself """
        if len(words) == 1:
            return True
        
        def judge_two(l, order):
            i = 0
            while i < len(l[0]) and i < len(l[1]):
                if order.index(l[0][i]) < order.index(l[1][i]):
                    return True
                elif order.index(l[0][i]) > order.index(l[1][i]):
                    return False
                else:
                    i += 1
            if i < len(l[0]):
                return False
            else:
                return True
        
        for i in range(len(words)-1):
            if not judge_two(words[i:i+2], order):
                return False
        return True
    
# @lc code=end


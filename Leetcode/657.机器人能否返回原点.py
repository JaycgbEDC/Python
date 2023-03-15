#
# @lc app=leetcode.cn id=657 lang=python3
#
# [657] 机器人能否返回原点
#

# @lc code=start
class Solution:
    def judgeCircle(self, moves: str) -> bool:
        """ others """
        return moves.count('L') == moves.count('R') and moves.count('U') == moves.count('D')
    
    def func1(self, moves: str) -> bool:
        """ myself """
        d = {'L': 0, 'R': 0, 'U': 0, 'D': 0}
        for ch in moves:
            d[ch] = d.get(ch, 0) + 1
        if d['L'] == d['R'] and d['U'] == d['D']:
            return True
        return False

# @lc code=end


#
# @lc app=leetcode.cn id=860 lang=python3
#
# [860] 柠檬水找零
#

# @lc code=start
class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        d = {5: 0, 10: 0}
        for num in bills:
            if num == 5:
                d[num] = d.get(num) + 1
            elif num == 10:
                if d[5] == 0:
                    return False
                else:
                    d[5] -= 1
                    d[10] += 1
            else:
                if d[10] != 0 and d[5] != 0:
                    d[10] -= 1
                    d[5] -= 1
                elif d[5] >= 3:
                    d[5] -= 3
                else:
                    return False
        return True

# @lc code=end


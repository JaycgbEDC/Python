#
# @lc app=leetcode.cn id=66 lang=python3
#
# [66] 加一
#

# @lc code=start
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        """ others: common """
        num = 0
        for i in range(len(digits)):
            num += digits[i] * pow(10, (len(digits)-1-i))
        return [int(i) for i in str(num+1)]
    
    def func1(self, digits: List[int]) -> List[int]:
        """ bymyself: easy thought """
        num = int(''.join(list(map(str, digits)))) + 1
        return list(map(int, list(str(num))))
    
    def func2(self, digits: List[int]) -> List[int]:
        """ bymyself: time good """
        plus = 1  # carry: 进位
        for index in range(len(digits))[::-1]:
            if plus == 0:
                break
            if digits[index] < 9:
                digits[index] = digits[index] + 1
                plus = 0
            else:
                digits[index] = 0
                plus = 1
        if digits[0] == 0:
            digits.insert(0, 1)
        return digits

# @lc code=end


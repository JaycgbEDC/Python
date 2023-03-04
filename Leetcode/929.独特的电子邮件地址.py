#
# @lc app=leetcode.cn id=929 lang=python3
#
# [929] 独特的电子邮件地址
#

# @lc code=start
class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        """ others """
        def parse(email):
            local, domain = email.split('@')
            local = local.split('+')[0].replace('.', '')
            return f'{local}@{domain}'
        
        return len(set(map(parse, emails)))
    
    def func1(self, emails: List[str]) -> int:
        """ bymyself """
        for index, s in enumerate(emails):
            temp = s.split('@')
            local = ''
            for ch in temp[0]:
                if ch == '.':
                    continue
                elif ch == '+':
                    break
                else:
                    local += ch
            emails[index] = local + '@' + temp[1]
        return len(set(emails))

# @lc code=end


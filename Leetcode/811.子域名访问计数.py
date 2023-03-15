#
# @lc app=leetcode.cn id=811 lang=python3
#
# [811] 子域名访问计数
#

# @lc code=start
class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        res = []
        d = {}
        for s in cpdomains:
            count, domain = s.split()
            count = int(count)
            d[domain] = d.get(domain, 0) + count
            l = domain.split('.')
            if len(l) == 3:
                d['.'.join(l[1:])] = d.get('.'.join(l[1:]), 0) + count
            d[l[-1]] = d.get(l[-1], 0) + count
        for item in d.items():
            res.append(str(item[1])+' '+item[0])
        return res

# @lc code=end


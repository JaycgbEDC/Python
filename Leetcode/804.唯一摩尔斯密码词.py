#
# @lc app=leetcode.cn id=804 lang=python3
#
# [804] 唯一摩尔斯密码词
#

# @lc code=start
class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        d = {'a': ".-",'b': "-...",'c': "-.-.",'d': "-..",'e': ".",'f': "..-.",'g': "--.",
             'h': "....",'i': "..",'j': ".---",'k': "-.-",'l': ".-..",'m': "--",'n': "-.",
             'o': "---",'p': ".--.",'q': "--.-",'r': ".-.",'s': "...",'t': "-",'u': "..-",
             'v': "...-",'w': ".--",'x': "-..-",'y': "-.--",'z': "--.."}
        count = 0
        l = []
        for s in words:
            l.append(''.join([d[ch] for ch in s]))
        return len(set(l))

# @lc code=end


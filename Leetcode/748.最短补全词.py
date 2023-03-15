#
# @lc app=leetcode.cn id=748 lang=python3
#
# [748] 最短补全词
#

# @lc code=start
class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        """ others """
        licensePlate = ''.join([i.lower() for i in licensePlate if i.isalpha()])
        words = sorted(words, key=len)
        for word in words:
            for i in range(len(licensePlate)):
                if word.count(licensePlate[i]) < licensePlate.count(licensePlate[i]):
                    break
                if i == len(licensePlate) - 1:
                    return word

    def func1(self, licensePlate: str, words: List[str]) -> str:
        """ bymyself """
        word = ''
        res = ''
        judge = 1
        d = {}
        length = 16
        for i in licensePlate:
            if 'A' <= i <= 'z':
                word += i.lower()
        if word == '':
            return words[0]
        for ch in word:
            d[ch] = d.get(ch, 0) + 1
        for s in words:
            for item in d.items():
                if item[1] > s.count(item[0]):
                    judge = 0
                    break
            if judge == 0:
                judge = 1
                continue
            if len(s) < length:
                length = len(s)
                res = s
        return res

# @lc code=end


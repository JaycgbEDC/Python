#
# @lc app=leetcode.cn id=832 lang=python3
#
# [832] 翻转图像
#

# @lc code=start
class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        res = []
        for l in image:
            temp = []
            for num in l[::-1]:
                if num == 0:
                    num = 1
                else:
                    num = 0
                temp.append(num)
            res.append(temp)
        return res

# @lc code=end


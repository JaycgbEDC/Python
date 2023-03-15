#
# @lc app=leetcode.cn id=941 lang=python3
#
# [941] 有效的山脉数组
#

# @lc code=start
class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        """ others """
        if len(arr) < 3:
            return False
        l = 0
        r = len(arr) - 1
        while l + 1 < len(arr) - 1 and arr[l] < arr[l + 1]:
            l += 1
        while r - 1 > 0 and arr[r] < arr[r - 1]:
            r -= 1
        return l == r
    
    def func1(self, arr: List[int]) -> bool:
        """ bymysef: too complex """
        if len(arr) < 3:
            return False
        top = 0
        for i in range(1, len(arr) - 1):
            if arr[i - 1] < arr[i] > arr[i + 1]:
                top = i
                break
            if arr[i - 1] >= arr[i]:
                return False
        if top == 0:
            return False
        for i in range(top + 1, len(arr)):
            if arr[i] >= arr[i - 1]:
                return False
        return True
    
    def func2(self, arr: List[int]) -> bool:
        """ bymyself: simple """
        if len(arr) < 3:
            return False
        top = arr.index(max(arr))
        if top == 0 or top == (len(arr) - 1):
            return False
        for i in range(top):
            if arr[i] >= arr[i + 1]:
                return False
        for i in range(top, len(arr) - 1):
            if arr[i] <= arr[i + 1]:
                return False
        return True

# @lc code=end


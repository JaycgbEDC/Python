#
# @lc app=leetcode.cn id=88 lang=python3
#
# [88] 合并两个有序数组
#

# @lc code=start
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """ others: good efficiency """
        ind1, ind2, write_ind = m-1, n-1, m+n-1
        while ind2 >= 0:
            if ind1 >= 0 and nums1[ind1] > nums2[ind2]:
                nums1[write_ind] = nums1[ind1]
                ind1 -= 1
            else:
                nums1[write_ind] = nums2[ind2]
                ind2 -= 1
            write_ind -= 1

    def func1(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """ bymyself """
        ind1 = ind2 = 0
        temp = []
        while (ind1 < m) and (ind2 < n):
            if nums1[ind1] <= nums2[ind2]:
                temp.append(nums1[ind1])
                ind1 += 1
            else:
                temp.append(nums2[ind2])
                ind2 += 1
        temp.extend(nums1[ind1:m] if (ind1 < m) else nums2[ind2:])
        nums1.clear()
        nums1.extend(temp)

        """
        Do not return anything, modify nums1 in-place instead.
        """
# @lc code=end


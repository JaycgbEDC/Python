#
# @lc app=leetcode.cn id=21 lang=python3
#
# [21] 合并两个有序链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """ myself: unsolve because not familar with DS-list in python """
        dummy = r = ListNode()  # 创建两个结点，第一个表示表头（空结点），第二个表示表尾
        while list1 and list2:
            if list1.val <= list2.val:
                r.next = list1
                list1 = list1.next
            else:
                r.next = list2
                list2 = list2.next
            r = r.next
        r.next = list1 or list2
        return dummy.next
    
    def func1(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """ others: recurse """
        if not list1 or list2:
            return list1 or list2
        if list1.val < list2.val:
            list1.next = func1(list1.next, list2)
            return list1
        else:
            list2.next = func1(list1, list2.next)
            return list2

# @lc code=end


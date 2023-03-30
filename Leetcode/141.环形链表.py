#
# @lc app=leetcode.cn id=141 lang=python3
#
# [141] 环形链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        low = head
        fast = head
        while fast and fast.next:
            low = low.next
            fast = fast.next.next
            if low == fast:
                return True
        return False
    
    def func():
        """ others """
        try:
            slow = head
            fast = head.next
            while slow is not fast:
                slow = slow.next
                fast = fast.next.next
            return True
        except:
            return False
        
# @lc code=end


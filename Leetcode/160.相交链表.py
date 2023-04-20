#
# @lc app=leetcode.cn id=160 lang=python3
#
# [160] 相交链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        def cal_length(root):
            lenght = 0
            p = root
            while p:
                lenght += 1
                p = p.next
            return lenght

        lenght_a, lenght_b = cal_length(headA), cal_length(headB)
        p_a, p_b = headA, headB
        if lenght_a - lenght_b < 0:
            for _ in range(lenght_b - lenght_a):
                p_b = p_b.next
        else:
            for _ in range(lenght_a - lenght_b):
                p_a = p_a.next
        while p_a:
            if p_a == p_b:
                return p_a
            p_a = p_a.next
            p_b = p_b.next
        return None
    
    def func(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if headA is None or headB is None:
            return None
        pa = headA # 2 pointers
        pb = headB
        while pa is not pb:
            # if either pointer hits the end, switch head and continue the second traversal, 
            # if not hit the end, just move on to next
            pa = headB if pa is None else pa.next
            pb = headA if pb is None else pb.next

        return pa
        
# @lc code=end


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1:
            return l2
        if not l2:
            return l1
        head = ListNode(0)
        head_2 = head
        while l1 and l2:
            if l1.val < l2.val:
                head_2.next = l1
                l1 = l1.next
            else:
                head_2.next = l2
                l2 = l2.next
            head_2 = head_2.next
        while l1:
            head_2.next = l1
            l1 = l1.next
            head_2 = head_2.next
        while l2:
            head_2.next = l2
            l2 = l2.next
            head_2 = head_2.next
        return head.next

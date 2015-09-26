# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        s = []
        if not head:
            return True
        while True:
            s.append(head.val)
            head = head.next
            if not head:
                break
        _s = list(reversed(s))
        
        if s == _s:
            return True
        else:
            return False

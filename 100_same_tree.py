# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if p == None or q == None:
            if p == None and q == None:
                return True
            else:
                return False
        else:
            same_left = self.isSameTree(p.left, q.left)
            same_right = self.isSameTree(p.right, q.right)
            return p.val == q.val and same_left and same_right

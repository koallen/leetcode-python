# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        else:
            if root.left != None:
                max_left = self.maxDepth(root.left)
            else:
                max_left = 0
            if root.right != None:
                max_right = self.maxDepth(root.right)
            else:
                max_right = 0

            return 1 + max(max_left, max_right)

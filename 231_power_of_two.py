class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        while n >= 2:
            n /= 2.0
        if n == 1:
            return True
        else:
            return False

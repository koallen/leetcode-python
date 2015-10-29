class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        pattern = []
        sum = 0
        while sum != 1:
            sum = 0
            while n > 0:
                digit = n % 10
                sum += digit * digit
                n = n / 10
            if sum not in pattern:
                n = sum
                pattern.append(sum)
            else:
                return False
            
        return True

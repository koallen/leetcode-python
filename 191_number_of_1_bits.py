class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        digit = 0
        binary = 0
        while n > 0:
            binary += (n % 2) * pow(10,digit)
            n //= 2
            digit += 1

        numOfOne = 0
        while binary > 0:
            numOfOne += binary % 10
            binary /= 10

        return numOfOne

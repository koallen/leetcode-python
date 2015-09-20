class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        pos = 0
        number = 0
        while s != "":
            number += (ord(s[-1]) - 64) * pow(26, pos)
            pos += 1
            s = s[:-1]
        return number

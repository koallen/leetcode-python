class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        allOne = True
        for digit in digits:
            if digit != 9:
                allOne = False
                break
        if allOne:
            lena = len(digits)
            a = [1]
            for i in range(lena):
                a.append(0)
            return a
        else:
            for i in range(len(digits)-1, -1, -1):
                if digits[i] == 9:
                    digits[i] = 0
                else:
                    digits[i] += 1
                    break
            return digits

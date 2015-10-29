class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counts = {}
        for num in nums:
            if num not in counts.keys():
                counts.update({num:1})
            else:
                counts[num] += 1
                
        maximum = 0
        for num, count in counts.items():
            if count > maximum:
                maximum = count
                result = num
                
        return result

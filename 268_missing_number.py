class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum = (0 + len(nums)) * (len(nums)+1) / 2
        sum_list = 0
        for num in nums:
            sum_list += num

        return sum - sum_list

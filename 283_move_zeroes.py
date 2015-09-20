class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] == 0 and nums[j] != 0:
                    temp = nums[j]
                    nums[j] = nums[i]
                    nums[i] = temp
                    break

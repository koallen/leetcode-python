class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            if nums[0] < nums[1]:
                return nums[0]
            else:
                return nums[1]
        else:
            minLeft = self.findMin(nums[:len(nums)//2])
            minRight = self.findMin(nums[len(nums)//2:])
            if minLeft < minRight:
                return minLeft
            else:
                return minRight

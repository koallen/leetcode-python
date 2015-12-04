class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        permutations = []
        sequence = []
        nums.sort()
        self.backtrack(sequence, nums, permutations)
        return permutations
        
    def backtrack(self, sequence, nums, permutations):
        if len(sequence) == len(nums):
            permutations.append([nums[i] for i in sequence])
        else:
            i = 0
            while i < len(nums):
                if i not in sequence:
                    sequence.append(i)
                    self.backtrack(sequence, nums, permutations)
                    sequence.pop()
                    while i+1 < len(nums) and nums[i] == nums[i+1]:
                        i += 1
                i += 1

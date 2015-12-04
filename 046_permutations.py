class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        permutations = []
        sequence = []
        self.backtrack(sequence, nums, permutations)
        return permutations
        
    def backtrack(self, sequence, nums, permutations):
        if len(sequence) == len(nums):
            permutations.append(sequence[:])
        else:
            for i in nums:
                if i not in sequence:
                    sequence.append(i)
                    self.backtrack(sequence, nums, permutations)
                    sequence.pop()

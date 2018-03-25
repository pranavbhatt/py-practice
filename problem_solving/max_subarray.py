import sys

class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_so_far = -sys.maxsize - 1
        max_ending_here = 0
        
        for n in nums:
            max_ending_here = max_ending_here + n
            if max_so_far < max_ending_here:
                max_so_far = max_ending_here
                
            if max_ending_here < 0:
                max_ending_here = 0
                
        return max_so_far

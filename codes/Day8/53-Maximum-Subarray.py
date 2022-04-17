class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # We start by creating our max and current sum variables.
        
        # For the max sum, we set it out of the constraints of the question.
        # This will ensure that it will be overwriten.
        max_sum = -99999
        current_sum = 0
        
        # Now we go through every number in the list
        for num in nums:
            current_sum += num
            
            # If the current sum is greater than max, then update the max sum
            if(current_sum > max_sum):
                max_sum = current_sum
            
            # If the current sum is in the negitive, then reset current sum
            if(current_sum < 0):
                current_sum = 0
        
        return max_sum
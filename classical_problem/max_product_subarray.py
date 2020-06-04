"""
Given an integer array nums, find the contiguous subarray within an array 
(containing at least one number) which has the largest product.
"""
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        finalMaxProd = curMaxProd = curMinProd = nums[0]
        for i in range(1, len(nums)):
            temp = curMaxProd
            curMaxProd = max(max(curMaxProd*nums[i], curMinProd*nums[i]), nums[i])
            curMinProd = min(min(temp*nums[i], curMinProd*nums[i]), nums[i])
            
            finalMaxProd = max(finalMaxProd, curMaxProd)
        
        return finalMaxProd
class Solution:

    
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        numsLen = len(nums)
        lo = 0
        mid = 0
        hi = numsLen - 1
        
        for i in range(0,numsLen):
            if nums[mid] == 0:
                nums[lo], nums[mid] = nums[mid], nums[lo]
                lo = lo + 1
                mid = mid + 1
            elif nums[mid] == 1:
                mid = mid + 1
            else:
                nums[mid], nums[hi] = nums[hi], nums[mid]
                hi = hi - 1
        
        
        
        
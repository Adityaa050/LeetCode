class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        for i in range(len(nums) - 2, -1, -1): 
            if nums[i] < nums[i + 1]:
                for j in range(len(nums) - 1, i, -1):
                    if nums[j] > nums[i]:
                        nums[i], nums[j] = nums[j], nums[i]
                        nums[i+1:] = reversed(nums[i+1:]) 
                        return
        nums[:] = nums[::-1]  

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        seen = max_sum = nums[-1]
        for i in range(len(nums) - 2, -1, -1):
            seen = max(nums[i], seen + nums[i])
            max_sum = max(seen, max_sum)
        return max_sum

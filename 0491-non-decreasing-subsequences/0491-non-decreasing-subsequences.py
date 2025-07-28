class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        ans = [] 
        path = []
        self.dfs(nums, 0, path, ans)
        return ans
    
    def dfs(self, nums, s, path, ans):
        if len(path) > 1:
            ans.append(path[:])
        used = set()
        for i in range(s, len(nums)):
            if nums[i] in used:
                continue
            if not path or nums[i] >= path[-1]:
                used.add(nums[i]) 
                path.append(nums[i])
                self.dfs(nums, i+1, path, ans)
                path.pop() 
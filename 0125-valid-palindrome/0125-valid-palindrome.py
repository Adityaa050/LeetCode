class Solution:
    def isPalindrome(self, s: str) -> bool:
        nums = "".join(re.findall(r'[a-zA-Z0-9]', s)).lower()
        if len(nums) == 1:
            return True
        elif len(nums) == 2:
            return nums[0] == nums[1]
        elif nums == nums[::-1]:
            return True
        else:
            return False
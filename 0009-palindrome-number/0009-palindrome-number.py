class Solution:
    def isPalindrome(self, x: int) -> bool:
        x_s = str(x)
        if x < 0 or x_s != x_s[::-1]:
            return False
        else:
            return True

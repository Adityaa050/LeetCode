class Solution:
    def isPalindrome(self, x: int) -> bool:
        x_a = str(x)
        if x < 0 or x_a != x_a[::-1]:
            return False
        else:
            return True
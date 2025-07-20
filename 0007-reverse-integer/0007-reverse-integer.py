class Solution:
    def reverse(self, x: int) -> int:
        nums = str(x)
        if nums[0] == '-':
            rev_str = '-' + nums[:0:-1]
        else:
            rev_str = nums[::-1]
        
        rev_int = int(rev_str)

       
        if(-(2**31)<=rev_int<2**31):
            return rev_int
        else:
            return 0
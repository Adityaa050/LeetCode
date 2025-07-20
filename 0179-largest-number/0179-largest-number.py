class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nu = list(map(str, nums))
        def compare(x, y):
            if y + x > x + y:
                return 1
            else:
                return -1
        nu.sort(key=cmp_to_key(compare))

        numm = ''.join(nu)
        if numm[0] == '0': return '0'
        else: return numm
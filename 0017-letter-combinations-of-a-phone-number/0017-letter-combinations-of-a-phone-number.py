class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        digit_to_letters = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }
        m = len(digits)
        result = []
        self.findingcombinations(digit_to_letters,digits,[],0,m,result)
        return result
    def findingcombinations(self,d2l,inp,temp,ind,m,result):
        if ind >= m:
            result.append(''.join(temp))
            return
        for i in d2l[inp[ind]]:
            temp.append(i)
            self.findingcombinations(d2l,inp,temp,ind+1,m,result)
            temp.pop()
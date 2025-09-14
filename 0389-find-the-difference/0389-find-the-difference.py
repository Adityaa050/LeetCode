class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        for asd in t:
            if t.count(asd) != s.count(asd):
                return asd
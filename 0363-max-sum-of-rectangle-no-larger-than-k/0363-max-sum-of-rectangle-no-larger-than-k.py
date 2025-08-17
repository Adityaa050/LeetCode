from bisect import bisect_left, insort

class Solution:
    def maxSumSubmatrix(self, matrix: list[list[int]], k: int) -> int:
        m, n = len(matrix), len(matrix[0])
        if m > n:
            matrix = list(zip(*matrix))
            m, n = n, m
        maxSum = float("-inf")
        for left in range(n):
            rowSums = [0] * m
            for right in range(left, n):
                for i in range(m):
                    rowSums[i] += matrix[i][right]
                prefix = 0
                prefixes = [0]
                for s in rowSums:
                    prefix += s
                    idx = bisect_left(prefixes, prefix - k)
                    if idx < len(prefixes):
                        maxSum = max(maxSum, prefix - prefixes[idx])
                    insort(prefixes, prefix)
        return maxSum
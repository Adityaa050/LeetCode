# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        res = 0

        def dfs(node):
            nonlocal res
            if not node:
                # The return data is (sum, is_bst, min_val, max_val)
                return 0, True, float('inf'), float('-inf')

            left_sum, left_check, min_left, max_left = dfs(node.left)
            right_sum, right_check, min_right, max_right = dfs(node.right)
            if left_check and right_check and max_left < node.val < min_right:
                s = left_sum + right_sum + node.val
                res = max(res, s)
                return s, True, min(min_left, node.val), max(max_right, node.val)
            return 0, False, float('inf'), float('-inf')

        dfs(root)
        return res
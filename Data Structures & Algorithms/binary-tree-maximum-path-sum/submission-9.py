# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = root.val

        def dfs(root):
            if not root: return 0

            lmax, rmax = dfs(root.left), dfs(root.right)
            lmax = max(0, lmax)
            rmax = max(0, rmax)

            nonlocal res
            res = max(res, lmax + root.val + rmax)

            return max(root.val + lmax, root.val + rmax)
        
        dfs(root)
        return res
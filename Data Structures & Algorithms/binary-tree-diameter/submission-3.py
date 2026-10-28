# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # brute force - n^2 / n
        # iterative DFS - stack - n / n
        # DFS - dfs() updates res and returns 1 + max(l, r) - n / h

        res = 0
        def dfs(root):
            nonlocal res
            if not root: return 0
            left = dfs(root.left)
            right = dfs(root.right)
            
            res = max(res, left + right)

            return 1 + max(left, right)

        dfs(root)
        return res
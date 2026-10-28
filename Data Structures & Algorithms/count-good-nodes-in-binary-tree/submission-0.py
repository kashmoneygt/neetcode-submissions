# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def dfs(root, val):
            if not root: return 0

            res = 1 if root.val >= val else 0
            val = max(val, root.val)
            res += dfs(root.left, val)
            res += dfs(root.right, val)
            return res

        return dfs(root, root.val)
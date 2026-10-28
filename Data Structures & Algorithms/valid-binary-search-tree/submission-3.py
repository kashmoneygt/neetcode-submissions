# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(l, root, r):
            if not root:
                return True
            if not l < root.val < r:
                return False
            return dfs(l, root.left, root.val) and dfs(root.val, root.right, r)
        
        return dfs(float("-inf"), root, float("inf"))
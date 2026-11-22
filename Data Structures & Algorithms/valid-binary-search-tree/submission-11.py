# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(low, node, high) -> bool:
            if not node:
                return True
            if not low < node.val < high:
                return False
            return dfs(low, node.left, node.val) and dfs(node.val, node.right, high)
        
        return dfs(float("-inf"), root, float("inf"))
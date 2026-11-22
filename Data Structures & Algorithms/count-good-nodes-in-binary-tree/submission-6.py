# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        res = [0]
        def dfs(node, val) -> None:
            if node is None:
                return
            
            if node.val >= val:
                res[0] += 1
            
            val = max(val, node.val)
            dfs(node.left, val)
            dfs(node.right, val)
        
        dfs(root, float("-inf"))
        return res[0]
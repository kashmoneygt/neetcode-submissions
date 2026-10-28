# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(root):
            if not root:
                return (0, True)

            leftH, leftB = dfs(root.left)
            rightH, rightB = dfs(root.right)

            imbalance = not leftB or not rightB or abs(leftH - rightH) > 1

            return (1 + max(leftH, rightH), not imbalance)
        
        return dfs(root)[1]
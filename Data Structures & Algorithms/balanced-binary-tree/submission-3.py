# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # DFS - return (1 + max(leftH, rightH), balanced) - n / h
        def dfs(root) -> (int, bool):
            if not root: return (0, True)

            leftH, leftB = dfs(root.left)
            rightH, rightB = dfs(root.right)

            balanced = leftB and rightB and abs(leftH - rightH) <= 1
            return (1 + max(leftH, rightH), balanced)

        return dfs(root)[1]
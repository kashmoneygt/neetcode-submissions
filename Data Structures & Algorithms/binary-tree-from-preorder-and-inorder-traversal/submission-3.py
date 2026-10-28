# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        preI = inI = 0

        def dfs(limit):
            nonlocal preI, inI
            if preI >= len(preorder):
                return None
            
            if inorder[inI] == limit:
                inI += 1
                return None
            
            root = TreeNode(preorder[preI])
            preI += 1
            root.left = dfs(root.val)
            root.right = dfs(limit)
            return root

        return dfs(float("inf"))
        
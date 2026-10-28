# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # BFS - deque - n / n
        # DFS (stack) - similar to BFS - n / n
        # DFS - n / n

        if not root: return None
        
        # operation
        root.left, root.right = root.right, root.left
        
        # recursive calls
        self.invertTree(root.left)
        self.invertTree(root.right)
        
        return root
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        q = collections.deque()
        q.append((root, 0))
        while q:
            node, total = q.popleft()
            if not node:
                continue
            
            if not node.left and not node.right and total + node.val == targetSum:
                return True
            
            q.append((node.left, total + node.val))
            q.append((node.right, total + node.val))

        return False
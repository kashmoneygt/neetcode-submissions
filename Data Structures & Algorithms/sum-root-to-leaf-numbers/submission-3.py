# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        res = 0
        q = collections.deque()
        q.append((root, 0))

        while q:
            node, val = q.popleft()
            val = val * 10 + node.val

            if not node.left and not node.right:
                res += val
                continue

            if node.left:
                q.append((node.left, val))
            if node.right:
                q.append((node.right, val))
        
        return res

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        res = [root.val]
        def dfs(node) -> int:
            if not node:
                return 0
            
            leftMax = max(dfs(node.left), 0)
            rightMax = max(dfs(node.right), 0)

            # potentially update the res with val if i am the split node
            res[0] = max(res[0], leftMax + rightMax + node.val)

            # return what another parent would get if they chose me as their child
            return node.val + max(leftMax, rightMax)
                
        



        dfs(root)
        return res[0]
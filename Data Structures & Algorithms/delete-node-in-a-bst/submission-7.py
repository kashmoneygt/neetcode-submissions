# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return root
        
        if root.val < key:
            root.right = self.deleteNode(root.right, key)
        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
        else: # root val matches key
            if not root.left:
                return root.right
            elif not root.right:
                return root.left

            # both children -> find the min from right subtree
            cur = root.right
            while cur.left: # stop at a valid node, not at none
                cur = cur.left
            
            root.val = cur.val
            root.right = self.deleteNode(root.right, root.val)
        
        return root

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if root is None:
            return None

        count = 0
        def helper(root):
            nonlocal count
            if root is None:
                return None
            
            left_result = helper(root.left)
            if left_result is not None:
                return left_result
            count += 1
            if count == k:
                return root.val
            return helper(root.right)
        return helper(root)




        
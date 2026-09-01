# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if root is None:
            return None
        
        max_value = root.val
        
        def helper(root, max_value):
            count = 0
            if root is None:
                return 0
            if root.val >= max_value:
                count += 1
                max_value = root.val

            left_tree = helper(root.left, max_value)
            right_tree = helper(root.right, max_value)

            return count + left_tree + right_tree
        return helper(root, max_value)
        
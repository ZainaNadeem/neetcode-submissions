# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        result = []

        def helper(root, depth):  
            if root is None:
                return []


            if depth == len(result):
                result.append(root.val)
            helper(root.right, depth + 1)
            helper(root.left, depth + 1)
        helper(root,depth = 0)

        return result
        
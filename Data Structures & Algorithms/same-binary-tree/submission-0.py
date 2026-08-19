# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # First check if the root exist for both
        # If it does not exist for either one of them
        # return False
        # If it does not exist for both
        # return True
        # If the root exists for both
        # Start checking if the values are equal
        if not p and not q:
            return True
        if not p or not q:
            return False

        if p and q:
            if p.val == q.val: 
                left_subtree = self.isSameTree(p.left, q.left)
                right_subtree = self.isSameTree(p.right, q.right)
            else:
                return False
                
        if left_subtree and right_subtree:   
            return True
        else:
            return False

        
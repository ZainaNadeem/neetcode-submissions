# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root is None:
            return False

        def check(root, subRoot):

            if not root and not subRoot:
                return True

            if not root or not subRoot:
                return False
            
            if root.val == subRoot.val:
                left_side = check(root.left, subRoot.left)
                right_side = check(root.right, subRoot.right)
                if left_side and right_side:
                    return True
                else:
                    return False
            else:
                return False

        
        if root.val == subRoot.val and check(root, subRoot): 
            return True
        else:
            left_side = self.isSubtree(root.left, subRoot)
            right_side = self.isSubtree(root.right, subRoot)

        if left_side or right_side:
            return True
        else:
            return False
   



            

             
        
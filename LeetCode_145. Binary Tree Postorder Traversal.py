# -*- coding: utf-8 -*-
"""
Created on Wed Sep  1 15:01:32 2021

@author: VIP
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        def postOrder(root):
            if root is None:
                return

            postOrder(root.left)
            postOrder(root.right)
            result.append(root.val)
        
        result = []
        postOrder(root)
        return result 
            
        


# -*- coding: utf-8 -*-
"""
Created on Wed Sep  1 15:01:59 2021

@author: VIP
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        def preorder(root):
            if root is None:
                return

            result.append(root.val)            
            preorder(root.left)
            preorder(root.right)
            
        
        result = []
        preorder(root)
        return result 
            
        


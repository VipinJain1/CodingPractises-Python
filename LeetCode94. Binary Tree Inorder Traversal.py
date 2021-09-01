# -*- coding: utf-8 -*-
"""
Created on Wed Sep  1 15:05:56 2021

@author: VIP
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        def inorder(root):
            if root is None:
                return
            inorder(root.left)
            result.append(root.val) 
            inorder(root.right)
            
        
        result = []
        inorder(root)
        return result 
        
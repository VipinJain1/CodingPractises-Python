# -*- coding: utf-8 -*-
"""
Created on Fri Dec 10 16:34:13 2021

@author: VIP
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isMirror(self,t1,t2):
        if t1 == None  or t2 == None:
            return t1==t2
            
        if t1.val != t2.val:
            return False
        
        return self.isMirror(t1.left, t2.right) and self.isMirror(t1.right, t2.left)
        
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
            
        return self.isMirror(root.left, root.right)
        
    
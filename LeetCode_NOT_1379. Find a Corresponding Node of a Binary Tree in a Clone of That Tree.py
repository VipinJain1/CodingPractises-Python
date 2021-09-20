# -*- coding: utf-8 -*-
"""
Created on Mon Sep 20 08:37:32 2021

https://leetcode.com/problems/find-a-corresponding-node-of-a-binary-tree-in-a-clone-of-that-tree/submissions/

@author: VIP
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findPosition(self,original,cloned,target):
        if original!=None:
            if original==target:
                return cloned
            else:
                l=self.findPosition(original.left,cloned.left,target) 
                return l if l!=None else self.findPosition(original.right,cloned.right,target)    
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        return self.findPosition(original,cloned,target)
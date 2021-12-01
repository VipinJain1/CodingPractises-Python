# -*- coding: utf-8 -*-
"""
Created on Wed Dec  1 16:44:21 2021

@author: VIP
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(root, currSum, targetSum):
            if root == None:
                return False
            currSum += root.val
            if not (root.left or root.right):
                return currSum == targetSum
            
            return dfs(root.left, currSum,targetSum) or dfs(root.right, currSum,targetSum)
        
        sm =0
        return dfs(root,sm, targetSum)

        
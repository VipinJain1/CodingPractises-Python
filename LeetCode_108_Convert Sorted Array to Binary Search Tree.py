# -*- coding: utf-8 -*-
"""
Created on Sun Nov 14 10:50:40 2021

@author: VIP
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def createTree(start,end):
            if start > end:
                return None
            mid =  (start+end)//2
            root = TreeNode(nums[mid])
            root.left = createTree(start,mid-1)
            root.right = createTree(mid+1,end)
            return root
        
        start =0
        end = len(nums)-1
        return createTree(start,end)
            
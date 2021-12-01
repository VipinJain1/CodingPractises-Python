# -*- coding: utf-8 -*-
"""
Created on Wed Dec  1 16:44:23 2021

@author: VIP
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    #from queue import Queue
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        from queue import Queue
        q = Queue()
        if root == None:
            return None
        res  = []
        q.put(root)
        while (not q.empty()):
            cnt =0
            sm =0
            temp = Queue()
            while(not q.empty()):
                cnt +=1
                node = q.queue[0]
                q.get()
                sm += node.val
                if node.left:
                    temp.put(node.left)
                if node.right:
                    temp.put(node.right)
            q = temp
            res.append(sm/cnt)
        
        return res 
            
        
        
        
        
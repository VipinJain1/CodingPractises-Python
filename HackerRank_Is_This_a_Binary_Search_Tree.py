# -*- coding: utf-8 -*-
"""
Created on Tue Aug 24 15:13:48 2021

@author: VIP
"""


""" Node is defined as
class node:
  def __init__(self, data):
      self.data = data
      self.left = None
      self.right = None
"""
def check_binary_search_tree_(root):
    if root == None:
        return True
    
    if root != None:
        if root.left != None  and root.right != None:
            if root.left.data > root.right.data:
                return False
            elif root.data < root.left.data :
                return False
            elif root.data > root.right.data :
                return False
            
        if root.left == None  and root.right != None:
            check_binary_search_tree_(root.right)
        elif root.right == None  and root.left != None:
            check_binary_search_tree_(root.left)
            
        else:
            check_binary_search_tree_(root.left)
            check_binary_search_tree_(root.left)
                
    return True    
        
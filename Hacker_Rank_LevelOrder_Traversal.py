# -*- coding: utf-8 -*-
"""
Created on Tue Aug 24 14:36:23 2021

https://www.hackerrank.com/challenges/tree-level-order-traversal/problem

@author: VIP
"""class Node:
    def __init__(self, info): 
        self.info = info  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.info) 

class BinarySearchTree:
    def __init__(self): 
        self.root = None

    def create(self, val):  
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root
         
            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break

"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.info (the value of the node)
"""
def levelOrder(root):
    #Write your code here
    queue = []
    queue.append (root)
    while len(queue)>0:
        root = queue.pop(0)
        print(root.info, end=" ")
        if root.left != None:
            queue.append(root.left)
        if root.right != None:
            queue.append(root.right)
      

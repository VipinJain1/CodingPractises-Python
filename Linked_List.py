"""

Created on Thu Jul 22 07:33:24 2021

@author: VIP

https://www.geeksforgeeks.org/linked-list-set-2-inserting-a-node/

Linked List | Set 2 (Inserting a node)
Difficulty Level : Easy
Last Updated : 28 Jun, 2021
 
We have introduced Linked Lists in the previous post. We also created a simple linked list with 3 nodes and discussed linked list traversal.
All programs discussed in this post consider the following representations of linked list. 

"""


import random
import sys

# Linked list wrapper 
class LinkedList():
    def __init__(self):
        self.head = None
    
    # add node to begining of the list
    def addNodeatFront(self, Node):
     
        Node.next =self.head
        self.head = Node
    
    def addNodeInLast(self,nd):
        
        if self.head is None:
            self.head = nd
        
        ptr = self.head
        while (ptr.next is not None):
            ptr = ptr.next
        
        ptr.next = nd
    
    def deleteNodeFirst(self):
            if self.head is None:
                print ("No Node to delete")
                return 
            else:
                self.ptr = self.head
                self.head = self.ptr.next
                print ("Delete first node", self.ptr.data)
                del self.ptr.data
                        
    #https://www.geeksforgeeks.org/delete-a-linked-list-node-at-a-given-position/          
    def deleteNodeMiddle(self,num):
           if self.head is None:
                print ("No Node to delete")
                return 
        
           count =1
           self.ptr =  self.head    
           while (count < num):
               count  = count +1
               self.ptr = self.ptr.next
           self.newptr = self.ptr
           self.xptr = self.ptr.next.next
           self.newptr.next = self.xptr
           del self.ptr.next
          
             
              
    def addValInRandomLocation(self,nd,numLoc):
        
        self.head1 = nd
        if self.head is None:
            self.head = nd
            return
            
        
        ptr = self.head
        while (numLoc > 1 and ptr.next is not None):
            ptr = ptr.next
            numLoc = numLoc-1
        
        if ptr.next is None:
            print ("List is shorter, can not add element in  middle")
            return sys.exit()
        else:
            nd.next = ptr.next
            ptr.next = nd
        
    # function  for printing entire list
    def printList(self):
        
        ptr = self.head
        while (ptr is not None):
            print (ptr.data)
            ptr = ptr.next
        
#Node class                
class Node():
     def __init__(self,data):
        self.next = None
        self.data = data
     
   
List =  LinkedList()
count = random.randint(0,20)   

print ("NUmbeer of values to insert to List is - ", count)
# add random elements to begining of the list
while (count >0):
    num = random.randint(0,10)
    node = Node (num)
    List.addNodeatFront(node)
    count = count -1

# Add random elements to end of the list
node = Node(43)
List.addNodeInLast(node)


# Add  element to random location in the list
node = Node(156)
List.addValInRandomLocation(node,5)


# Add  element to middle location in the list
mid = int (count/2)

node = Node(128)
print (" MIddle location is - ", mid)
List.addValInRandomLocation(node,mid)

# print entire list
List.printList()

List.deleteNodeFirst()

List.deleteNodeMiddle(mid)

# print entire list
List.printList()
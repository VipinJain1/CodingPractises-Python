# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
      
        root1 = headA
        root2 = headB
        d = list()
        if root1 is None or root2 is None:
            return None
        rootb = root2
        roota = root1

        while (rootb):
            d.append(rootb)
            rootb = rootb.next
          
        while (roota):
            if roota in d:
                return roota
            roota = roota.next
        return None   
            
        
        
            
        
        

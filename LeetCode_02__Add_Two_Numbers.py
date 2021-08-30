# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        if l1  == None and l2 == None:
            return None
        
        if l1 == None:
            return l2
        if l2 is None:
            return l1
      
        root1 = l1
        root2 = l2
        carry = 0
        
        while (l1 != None and l2 != None):
            l1val = l1.val
            if l1.val + l2.val >=10:
                l1.val = (l1.val +l2.val)%10  + carry
            else:
                l1.val = l1.val +l2.val +carry 
            
            carry = int ((l1val +l2.val)/10)
                
            if l1 == None or l2 == None:
                break
            
            l1 = l1.next
            l2 = l2.next
       
        if l1 != None and l2 == None:
            if carry >=0:
                while carry >=0 or l1.next != None:
                    l1.val = l1.val+carry
                    if l1.val == 10:
                        carry =1
                        l1.val =0
                    else:
                        carry =0 
                     
                    if l1.next == None:
                        if carry:
                            n = ListNode(1)
                            n.data =1
                            l1.next = n
                            n.next = None
                            break
                    
                    l1 = l1.next
                        
        elif l2 != None and l1 == None:
            if carry >=0:
                while carry >=0 or l2.next != None:
                    l2.val = l2.val+carry
                    if l2.val == 10:
                        carry =1
                        l2.val =0
                    else:
                        carry =0 
                     
                    if l2.next == None:
                        if carry:
                            n = ListNode(1)
                            n.data =1
                            l2.next = n
                            n.next = None
                            break
                    
                    l2 = l2.next
                        
        if carry and l1 == None and l2  == None:
            root = root1
            while (root.next != None):
                root = root.next
            n = ListNode(1)
            n.data =1
            root.next = n
            n.next = None
            
        return root1
    
            
        
          
            
            
            
        
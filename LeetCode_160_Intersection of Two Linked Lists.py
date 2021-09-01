
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        root1 = headA
        root2 = headB
        if root1 is None or root2 is None:
            return None
        rootb = root2
        while (rootb):
            roota = root1
            while (roota):
                if roota == rootb:
                    return roota
                roota = roota.next
            rootb = rootb.next     

            
        
        

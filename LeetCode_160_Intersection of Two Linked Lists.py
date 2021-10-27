# -*- coding: utf-8 -*-
"""
Created on Wed Oct 27 18:35:11 2021

@author: VIP
"""
# Still NOT Working

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        cntA =0
        cntB = 0
        roota = headA
        rootb = headB
        if roota.next == None or rootb.next == None:
            if roota == rootb:
                return roota.val
            else:
                return None
        while (roota.next != None or  rootb.next != None):
            if roota.next != None:
                roota = roota.next
                cntA +=1
            if rootb.next != None:
                rootb = rootb.next
                cntB +=1
        if cntA == cntB:
            return None
        numA =0
        numB =0
        diff = abs(cntB- cntA)
        if cntA > cntB:
            rootA = headA
            rootB = headB
        else:
            rootA = headB
            rootB = headA
        cnt =0
        print ("diff==", diff)
        while rootA != None:
            print ("A==", rootA.val)
            if cnt >= diff:
                print ("B ==", rootB.val)
                rootB = rootB.next
            rootA  = rootA.next
            cnt +=1
            if rootA == rootB:
                print ("Now Root A ===", rootA)
                return rootA
          
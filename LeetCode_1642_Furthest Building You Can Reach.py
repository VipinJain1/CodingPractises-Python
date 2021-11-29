# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class Solution:
class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        heap = []
        ln  = len(heights)
        start =0
        end = ln -1
        import heapq
        heapq.heapify(heap)
        cnt  =0
        
        #if (bricks ==0 and ladders ==0):
        #    return 1
        
        if sum(heights) <= bricks:
            return end

        while (start <end):
            num = heights[start+1] - heights[start]
            if num >0:
                heapq.heappush(heap,num)
            cnt +=1
            
            if ladders >0:
                while (sum(heap) > bricks and ladders >0):
                    topmax  = heapq.nlargest(1,heap)
                    heap.remove(topmax[0])
                    ladders -=1
                    if sum(heap) <= bricks:
                        break
                    if ladders ==0:
                        break

            elif sum(heap)> bricks:
                cnt -=1
                break
            start +=1
            
        return cnt
                 
                
            
                
heights = [14,1,19,30,3,45,56,6,76,7,78,8,8,9,14,1,19,30,3,45,56,6,76,7,78,8,8,9,14,1,19,30,3,45,56,6,76,7,78,8,8,9]
bricks = 99
ladders =7
obj = Solution()
total = obj.furthestBuilding(heights, bricks, ladders)
print ("Total JUmps", total)
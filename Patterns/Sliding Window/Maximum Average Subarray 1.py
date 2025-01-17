from math import inf
from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        windowsum = 0
        start = 0
        maxavg = float(-inf)
        #here i will act as end index
        for i in range(0,len(nums)):
            #calculate intial window sum
            windowsum+= nums[i]
            #if the endindex - startindex+1 == k that means reached window size
            #then we need to start calculating the avg, set max 
            #after that remove first element from windowsum and set start index(increment by 1)
            if (i-start+1) == k:
                windowavg = float(windowsum/k)
                maxavg = max(windowavg,maxavg)
                windowsum-=nums[start]
                start+=1
            

        return maxavg
        


        
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        start = 0
        subarraylen = 0
        subarraysum = 0

        for end in range(0,len(nums)):
            subarraysum+=nums[end]
            while(subarraysum>=target):
                if subarraylen == 0:
                    subarraylen = end-start+1
                subarraylen = min(subarraylen,end-start+1)
                subarraysum-=nums[start]
                start+=1


        return subarraylen
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start= 0
        end = len(numbers)-1

        while (start<end):
            arraysum = numbers[start]+numbers[end]

            if arraysum == target:
                return [start+1,end+1]
            
            elif arraysum<target:
                start+=1

            else:
                end-= 1
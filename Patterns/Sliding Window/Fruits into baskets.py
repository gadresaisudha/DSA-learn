from typing import List
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        maxfruits = 0
        fruitmap = {}
        start = 0

        for end,fruittype in enumerate(fruits):
            #initally add two types of fruits to our map and calculate the max for that 2 type fruits
            if (len(fruitmap)< 2 and not (fruitmap.get(fruittype))):
                fruitmap[fruittype] = True
                maxfruits = max(maxfruits,end-start+1)

            # if we encounter any fruit types in array that are in map then just calculate the max
            elif fruitmap.get(fruittype):
                maxfruits = max(maxfruits,end-start+1)

            #incase there exists a 3rd type then just reset max to empty
            #add the fruit type before current as start and present fruit type as end
            #add these two to map and calculate max
            else:
                fruitmap.clear()
                fruitmap[fruits[end-1]] = True  #fruit type before 3rd type fruit
                fruitmap[fruittype] = True      #new 3rd type
                start = end -1

                while(fruits[start]== fruits[start-1]):
                    start-=1
                maxfruits = max(maxfruits,end-start+1)

        return maxfruits
                
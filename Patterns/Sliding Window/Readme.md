Sliding window protocol:
1.fixed window size
2.Dynamic window size
we have to decide if we are going to use a fixed size or dynamic size window


1. fixed window size:
ex:
nums = [ 1, 12,-5,-6,50,3]
now if we are asked to calculate the average of contiguous array of fixed size k
1+12+-5-6/4 since k =4
=1/2

now if we are asked to maximum average of all contiguous array of size k within the array
1+12-5-6
12-5-6+50
-5-6+50+3

3 sets take average and find max

Bruteforce approach:
For each element in input array:
    iterate through elemnt+contiguous k elements:
        calculate sum
    calculatev average
    set max

max = -math.inf
for i in range(0,len(nums)-k):
    ws = 0
    for j in range(i,i+k):
        ws+=nums[j]
    
    max = max(ws/k,max)

return max
        
Time complexity:
for each value in array of size n 
we are travelling k times
so total will travel n*k times
O(n*k)



Sliding window protocol:
first calculate the sum of k elements and calculate the average and set it as max
now from here we will calculate the sum of every set by removing first elemnt and adding next element(after k element)
and caluclating sum and setting the max
we need to track start index and last index and also window sum
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
        

Time complexity:
we are going to go over each element of the array only once
so travel all elements of array i.e length of array:
O(n)
        


2. Dynamic window size:
ex: visiting a farm and you have row of fruit trees 
The trees are represented by an integer array fruits where fruits[i] is the type of fruit the ith tree produces.

You want to collect as much fruit as possible. However, the owner has some strict rules that you must follow:

You only have two baskets, and each basket can only hold a single type of fruit. There is no limit on the amount of fruit each basket can hold.
Starting from any tree of your choice, you must pick exactly one fruit from every tree (including the start tree) while moving to the right. The picked fruits must fit in one of your baskets.
Once you reach a tree with fruit that cannot fit in your baskets, you must stop.
Given the integer array fruits, return the maximum number of fruits you can pick.


Example 1:

Input: fruits = [1,2,3,2,2]

here the numbers are type of fruit trees and you can fit single type of fruit into one basketand you are given two baskets
basically here we dont have a fixed size we have to check for different window sizes as we need to dynamically either expand the window size or shrink it in order to fill our 2 basket with 2 different type fruits and they have to be maximum
basically iterate whole array and give the maximum number of fruits you can pick after iterating the whole array
so that the tree categories are of two types
{note: you are going to pick one fruit from each tree over there we have make sure that the fruit types fall into 2 categories so that we get maximum nmber of fruits
}
Approach :
so first we need to fix our basket size to 2 like two different type of fruits
and then if we find fruits types that are same as one in basket then we expand our window size
if not we stop there and move on to new start point for the basket

Iteration 1:
Baskets:{1:[1],2:[1]} next 3 -> cant move forward basket already full with types
basket size always 2, window size 2
max fruits : 1+1 =2

Iteration 2: move to new start
Baskets:{2:[1],3:[1]}  basket size 2, window size 2
next 2 -> expand window size and add to number of fruits of type 2
Baskets:{2:[2],3:[1]}  basket size 2, window size 3
next 2->  expand window size and add to number of fruits of type 2
Baskets:{2:[3],3:[1]}  basket size 2, window size 4
            |
max fruits 3+1 = 4

similarly .....

solution:
def totalFruit(self, fruits: List[int]) -> int:
        maxfruits = 0
        fruitmap = {}
        start = 0

        for end,fruittype in enumerate(fruits):
            #initally add two types of fruits to our map and calculate the max for that 2 type fruits
            if (len(fruitmap)< 2 and not (fruitmap[fruittype])):
                fruitmap[fruittype] = True
                maxfruits = max(maxfruits,end-start+1)

            # if we encounter any fruit types in array that are in map then just calculate the max
            elif fruitmap[fruittype]:
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

when iteration your fruits array that lines up different fruit types in a row and we need to find maximum 
number of fruits basically the maxlen in array accomadating two different fruit types:

three cases comes into picture
case 1: when the basket  i.e map has less than 2 types
in this case just add those types to map and calculate max

if (len(fruitmap)< 2 and not (fruitmap[fruittype])):
    fruitmap[fruittype] = True
    maxfruits = max(maxfruits,end-start+1)

keeps track of max among the previous and present one

case 2: if we encouter fruittype in fruits array that is in the map
then just increase window size that is calculate max
elif fruitmap[fruittype]:
    maxfruits = max(maxfruits,end-start+1)

case 3 : when you encouter a 3rd type
in that case we are resetting our map
and choosing the before fruit type as start
and current one as end and putting them in max
also we are checking if the start and also one before start are same
move start to the back
finally keep track of window size everytime so that you are calculating the  max fruits
else:
    fruitmap.clear()
    fruitmap[fruits[end-1]] = True  #fruit type before 3rd type fruit
    fruitmap[fruittype] = True      #new 3rd type
    start = end -1

    while(fruits[start]== fruits[start-1]):
        start-=1
    maxfruits = max(maxfruits,end-start+1)


Time complexity: O(n)
iterating over each elemnt only once
but there is possiblity for one elemnt to be the repeatins start value 
in that case O(n+n) == O(2n) === O(n)


another dynamic size window:
Longest substring without repeat
pattern for sliding window is used when we need to find something in contiguous that is not repeating
Given a string s, find the length of the longest 
substring
 without repeating characters.

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Basically we need to find the longest substring without repeating characters
for this we consider our string inside a window
window size == substring length
we need to find max len and also characters should not be repeating

solution:
def lengthOfLongestSubstring(self, s: str) -> int:
    charmap = {}
    longestsublen = 0
    start = 0

    for end in range(len(s)):
        c = s[end]

        if not charmap[c]:
            charmap[c] = True
            longestsublen = max(longestsublen,end-start+1)

        else:
            while(charmap[c]):
                charmap[s[start]] = False
                start+=1

            charmap[c] = True


    return longestsublen

Approach:
for this first we store whether a character has been visited or not by using a map
map : charcter: bool
keep track of characters that we visit
two scenarios to consider
scenario one:
when character is not repeated 
in this case we store it in our map make it as true
calculate the length of substring keep track of it

c = s[end]
if not charmap[c]:
    charmap[c] = True
    longestsublen = max(longestsublen,end-start+1)

scenario two:
when charcter is repeated 
in this case first we make all the charcters from start to point where the repeating character is set to false
in map
and increment the start pointer forward
do this untill the repeating character is set to false
now make the current character to True
else:
    while(charmap[c]):
        charmap[s[start]] = False
        start+=1

    charmap[c] = True
continue this and finally return the longestsublen

Time complexity: O(n)
iterating over each elemnt only once(end pointer)
but there is possiblity that start pointer may go on untill the last character of string
in that case O(n+n) == O(2n) === O(n)


Another dynamic size sliding window:
minimum size subarray sum:
Given an array of positive integers nums and a positive integer target, return the minimal length of a 
subarray
 whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.

Example 1:

Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.

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

approach:
find sum untill target reached when sum is more than target increment start pointer so that you get min len array



conclusion:
So basically use sliding window whenever you seem something that needs to be contiguous
like find something in continuous pattern like substring, subarray, subset .....
when we have to consider all elements in a window



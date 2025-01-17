Two pointer technique:
use this when we need to consider only two elements that are pointers
literally keep track of two pointers all the time

Two sum:
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Brute force approach:
Run two loops to get all the combinations and find whether equal to target

two pointer approach:
here the array is in ascending order
so we take two pointers one from beginning and another from end

start = 0
end = len(nums)-1

Run the loop untill start<end
now if the array values sum at pointers start and end are equal to target then just return them
if the pointers sum is less than target then just move start pointer as the array is in ascending order and we are just adding more value to it
if the pointer sum is greater than target that means we need to decrease the value so we need to decrement the end pointer

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

Time complexity: O(n)
as our pointers are travelling all element from array from front and back only once
if they cross our while loop breaks so o(n)


2. Container with most water
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

Approach:
keep track of maxarea using a variable
now take start and end pointer
calculate width and height
w = end-start
h = min(height[start],height[end]) -> min of both pointers to hold water
then calulate area
maxarea = max(area,maxarea)-> always keep track of areas
height should be largest on both sides so that water doesnt fall
Run the loop untill start<end
compare start and end pointer 
if height[start]<height[end] move start forward
else if height[start]>height[end] move end backward

def maxArea(self, height: List[int]) -> int:
        start = 0
        end = len(height)-1
        maxarea = 0

        while(start<end):
            w = end - start
            h = min(height[start],height[end])
            area = w*h
            maxarea = max(area,maxarea)
            if height[start]<height[end]:
                start+=1
            else:
                end-=1
        

        return maxarea

3. Merge Two sorted lists
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.
Return the head of the merged linked list.

Example 1:

Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

we are not using extra memory so space complexity o(1)

Inorder to create a singly linkedlist
we need to create a ListNode and attach next one to the former one

set your pointers
and compare them 
which is less that will be next to our tail node
since that node in either list1 or list2 is visitied move l1 or l2 pointer

at the end make sure to move tail pointer

def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        placeholder = ListNode()
        tail = placeholder

        l1 = list1
        l2 = list2

        while l1 and l2:
            if l1.val <l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next


        if l1:
            tail.next = l1
        elif l2:
            tail.next = l2

        return placeholder.next

Time complexity O(m+n)
size of list1 and list2
space complexity -  o(1)
not allocating memory just pointing them

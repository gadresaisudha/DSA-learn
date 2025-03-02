class Solution:
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
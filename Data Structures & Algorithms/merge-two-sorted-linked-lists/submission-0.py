# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        n = ListNode()
        first = n
        if not list1:
            return list2
        if not list2:
            return list1
        if list1.val < list2.val:
            n.val = list1.val
            list1 = list1.next
        else:
            n.val = list2.val
            list2 = list2.next
        while list1 is not None:
            while list2 is not None and list1 is not None and list1.val < list2.val:
                n.next = ListNode()
                n = n.next
                n.val = list1.val
                list1 = list1.next
                
            while list2 is not None and list1 is not None and list2.val < list1.val:
                n.next = ListNode()
                n = n.next
                n.val = list2.val
                list2 = list2.next
            while list2 is not None and list1 is not None and list1.val == list2.val:
                n.next = ListNode()
                n = n.next
                n.val = list1.val
                list1 = list1.next
                n.next = ListNode()
                n = n.next
                n.val = list2.val
                list2 = list2.next
            if list2 is None:
                while list1 is not None:
                    n.next = ListNode()
                    n = n.next
                    n.val = list1.val
                    list1 = list1.next
        if list1 is None:
            while list2 is not None:
                n.next = ListNode()
                n = n.next
                n.val = list2.val
                list2 = list2.next 
        return first

            

        
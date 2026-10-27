# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1

        curr1 = list1
        curr2 = list2
        head = None
        curr = None

        while curr1 and curr2:
            if curr1.val < curr2.val:
                if head == None:
                    head = curr1
                else:
                    curr.next = curr1
                
                curr = curr1
                curr1 = curr1.next
            else:
                if head == None:
                    head = curr2
                else:
                    curr.next = curr2
                                
                curr = curr2
                curr2 = curr2.next
        
        while curr1:
            curr.next = curr1
            curr = curr1
            curr1 = curr1.next  

        while curr2:
            curr.next = curr2
            curr = curr2
            curr2 = curr2.next      
        
        return head
                    
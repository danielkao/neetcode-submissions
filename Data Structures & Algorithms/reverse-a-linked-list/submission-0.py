# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        prev = None
        current = head
        # (head) 1 -> 4 -> 9 -> 10
        while current:
            temp = current.next # 1
            current.next = prev # None <- 1
            prev = current # previous = 1
            current = temp # current = 4
            
        head = prev
        return head
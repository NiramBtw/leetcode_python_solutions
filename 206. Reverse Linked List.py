# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        curr = head
        # iteratively Solution
        while curr: 
            nxt = curr.next # the next pointer
            curr.next = prev 
            prev = curr
            curr = nxt
        return prev
        

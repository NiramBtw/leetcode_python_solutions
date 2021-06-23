# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        # remove all ele == val 
        # so going from 1 to the next as long not == val then skip
        
        while head and head.val == val:  
            head = head.next  # jumping 
        
        if not head:
            return head
        
        cur = head
        while cur:
            if cur.next and cur.next.val == val:  # cur == val skip as well
                cur.next = cur.next.next
            else:
                cur =cur.next
        return head
                

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        p1 = headA
        p2 = headB
        
        while p1 != p2: 
            if p1:  # if p1 not ant the end
                p1 = p1.next  # move 1 stape
            else:   # at the end
                p1 = headB  # if they link they need to be the same 
            if p2:
                p2 = p2.next
            else:
                p2 = headA
        return p1  # if no intersection p1 at the end will be None
                        
        

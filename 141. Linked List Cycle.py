# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        """
        to find if passing the index all ready 
        save them as seen 
        else false 
        
        """
        
        seen = set()  # getting uniques
        current = head  # pointer
        # now looping in seen to cheack 
        while current:
            if current in seen:     # mean we pass that all ready 
                return True
            seen.add(current)  #adding
            current = current.next  # moving the pointer 1 
        return False
            
        

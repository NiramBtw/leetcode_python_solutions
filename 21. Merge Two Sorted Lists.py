# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        create a dummy output 
        1,2,4 
        1,3,4
        
        if both not empty keep runnig 
        else mean that 1 list have no elemet then we can take 
        the remainder of that list 
        
        
        """
        
        dummy = ListNode()
        tail = dummy 
        # using while cuz for more general prob
        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
                #the tail pointer will update regardless of which node 
                # we insert into the list
            tail = tail.next
            # need to find the non empty list and then insert
        if l1:
            tail.next = l1
        elif l2:
            tail.next = l2
        return dummy.next
                
                

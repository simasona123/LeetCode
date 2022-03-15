# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pt0 = head
        if pt0 == None :
            return head
        pt1 = pt0.next
        while pt0 != None and pt0.next != None:
            if pt1.val != pt0.val:
                pt0 = pt0.next
                pt1 = pt0.next
                continue
            if pt0.val == pt1.val :
                pt0.next = pt1.next
                pt1 = pt1.next
        return head
                
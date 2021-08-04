# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        try:
            i = head.next
            j = head.next.next
            if i == None or j == None:
                return False
            if i == j :
                return True
            while i != j :
                i = i.next
                j = j.next.next
                if i == None or j == None:
                    return False
                elif i == j :
                    return True
        except:
            return False

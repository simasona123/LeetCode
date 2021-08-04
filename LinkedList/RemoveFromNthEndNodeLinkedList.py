# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        i = 0
        temp = {}
        node = head
        while node.next != None:
            temp[i] = node
            node = node.next
            i += 1
        temp[i] = node
        n = i + 1 - n
        if n == 0:
            if temp[n].next == None:
                return
            else:
                return temp[n].next
        node = temp[n-1]
        if temp[n].next == None:
            node.next = None
            return head
        else:
            node.next = temp[n+1]
            return head
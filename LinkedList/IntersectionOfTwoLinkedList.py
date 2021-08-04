# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        node1 = headA
        node2 = headB
        temp1 = set()
        temp2 = set()
        if node1 == node2:
            return node1
        temp1.add(node1)
        temp2.add(node2)
        while node1.next != None or node2.next != None:
            if node1.next != None:
                node1 = node1.next
                temp1.add(node1)
            if node2.next != None:
                node2 = node2.next
                temp2.add(node2)
            if node2 in temp1:
                return node2
            elif node1 in temp2:
                return node1
        return None
            
            
    
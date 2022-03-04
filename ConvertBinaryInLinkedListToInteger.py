# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        node = head
        binary_value = []
        binary_value.append(node.val)
        while node.next != None:
            node = node.next
            binary_value.append(node.val)
        binary_value_order = len(binary_value)-1
        result = 0
        for item in binary_value:
            result += item * (2**binary_value_order)
            binary_value_order -= 1
        return result
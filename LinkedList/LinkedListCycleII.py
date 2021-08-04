# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        try :
            node = head
            temp = {}
            i = 0
            while node.next != None :
                if temp.get(node, None) == None:
                    temp[node] = i
                else :
                    return node
                node = node.next
        except:
            return None
        
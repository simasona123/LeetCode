# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 == None and list2 == None:
            return None
        result = ListNode()
        result_pt = result
        list1_pt = list1
        list2_pt = list2
        while True :
            if list1_pt != None and list2_pt != None:
                if list1_pt.val <= list2_pt.val :
                    list1_pt, result_pt = self.listKecil(list1_pt, result_pt)
                elif list2_pt.val <= list1_pt.val:
                    list2_pt, result_pt = self.listKecil(list2_pt, result_pt)
            if list1_pt == None:
                result_pt = self.listNone(list2_pt, result_pt)
                return result
            elif list2_pt == None:
                result_pt = self.listNone(list1_pt, result_pt)
                return result
    def listNone(self, list_x, hasil):
        while True:
            if list_x != None:
                hasil.val = list_x.val
                list_x = list_x.next
                if list_x != None :
                    hasil.next = ListNode()
                    hasil = hasil.next
                else :
                    break
        return hasil
    
    def listKecil(self, list_besar, result_pt):
        result_pt.val = list_besar.val
        result_pt.next = ListNode()
        result_pt = result_pt.next
        list_besar = list_besar.next
        return list_besar, result_pt
        
        
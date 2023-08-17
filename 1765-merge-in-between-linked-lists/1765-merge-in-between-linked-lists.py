# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        
        curr = list1

        for _ in range(a - 1):
            curr = curr.next
        
        point = curr.next
        for _ in range(b - a):
            point = point.next

        curr.next = list2
        while curr.next:
            curr = curr.next
        
        curr.next = point.next

        return list1
        


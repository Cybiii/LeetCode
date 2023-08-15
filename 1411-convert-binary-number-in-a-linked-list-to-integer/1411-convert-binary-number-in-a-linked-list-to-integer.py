# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        curr = head
        lst = []
        
        if not head: return 0
        
        while curr:
            lst += [curr.val]
            curr = curr.next
            
        num = 0
        lst.reverse()
        for i in range(len(lst)):
            num += (2**i) * lst[i]

        return num
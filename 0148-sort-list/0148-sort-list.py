# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        curr2 = head

        lst = []
        while curr:
            lst += [curr.val]
            curr = curr.next
        
        lst = sorted(lst)

        i = 0
        while curr2:
            curr2.val = lst[i]
            curr2 = curr2.next
            i += 1
        return head
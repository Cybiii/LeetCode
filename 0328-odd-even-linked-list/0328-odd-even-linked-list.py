# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return head
        odd = curr = head
        even = head.next
        
        odds, evens = [], []
        while even and odd:

            odds += [odd.val]
            evens += [even.val]

            odd = odd.next.next
            if not even.next:
                break
            even = even.next.next
        
        if odd:
            odds += [odd.val]

        lst = odds + evens

        i = 0
        while curr:
            curr.val = lst[i]
            curr = curr.next
            i += 1

        return head
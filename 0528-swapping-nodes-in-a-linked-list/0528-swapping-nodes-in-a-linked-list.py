# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head: return head
        curr = curr2 = head

        lst = []
        while curr:
            lst += [curr.val]
            curr = curr.next
        
        l = 0
        r = len(lst) - 1

        l += (k - 1)
        r = (r - k + 1)

        tmp = lst[l]
        lst[l] = lst[r]
        lst[r] = tmp

        i = 0
        while curr2:
            curr2.val = lst[i]
            curr2 = curr2.next
            i += 1
        
        return head
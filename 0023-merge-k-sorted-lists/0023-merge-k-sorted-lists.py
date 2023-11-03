# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        lst = []
        for linkedlist in lists:
            curr = linkedlist

            while curr:
                lst += [curr.val]
                curr = curr.next
        
        lst = sorted(lst)

        newlink = ListNode()
        curr = newlink

        li = len(lst) - 1

        if not lst:
            return

        for i in range(len(lst)):
            
            if i == len(lst) - 1:
                curr.val = lst[i]
                break

            curr.val = lst[i]
            curr.next = ListNode()
            curr = curr.next
        
        return newlink
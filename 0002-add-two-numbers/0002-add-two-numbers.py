# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def ltoint (lx):
            curr = lx
            lsx = []
            while curr:
                lsx += [curr.val]
                curr = curr.next
            lsx.reverse()

            return int(''.join([str(i) for i in lsx]))

        res = str(ltoint(l1) + ltoint(l2))

        k = len(res)
        res = int(res)
        dummy = ListNode()
        curr = dummy
        for i in range(k):
            if i != k - 1:
                curr.next = ListNode()    
            curr.val = res % 10
            curr = curr.next
            res //= 10
        
        return dummy

        
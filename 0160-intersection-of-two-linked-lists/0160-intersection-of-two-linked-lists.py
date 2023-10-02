# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        tailA = currA = headA
        tailB = currB = headB
        lenA = lenB = 0


        if not (headA and headB):
            return null

        while tailA:
            lenA += 1
            tailA = tailA.next
        while tailB:
            lenB += 1
            tailB = tailB.next

        if tailA is not tailB:
            return null
        
        if lenB > lenA:
            for _ in range(lenB - lenA):
                currB = currB.next
        
        elif lenA > lenB:
            for _ in range(lenA - lenB):
                currA = currA.next

        while currA != currB:
            currA = currA.next
            currB = currB.next

        return currA
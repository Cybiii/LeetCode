class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        for _ in range(n):
            nums1.pop()
        for elem in nums2:
            nums1.append(elem)

        nums1.sort()

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        lst = []
        for x in nums1:
            for y in nums2:
                if x == y:
                    lst += [x]
        return set(lst)
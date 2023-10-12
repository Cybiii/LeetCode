class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        if not nums:
            return nums
        d = {}
        m = -1
        for num in nums:
            d[num] = num*-1
            if num in d.values():
                m = max(abs(num), m)

        print(d, m)
        return m
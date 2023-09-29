class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxc = 0
        c = 0
        for num in nums:
            if num == 1:
                c += 1
            else:
                maxc = max(c, maxc)
                c = 0
        maxc = max(c, maxc)
        return maxc
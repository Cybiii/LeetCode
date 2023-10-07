class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count = 0
        for num in nums:
            c = 0
            while (num > 0):
                c += 1
                num = num // 10
            if c % 2 == 0:
                count += 1
        return count
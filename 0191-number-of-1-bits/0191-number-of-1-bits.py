class Solution:
    def hammingWeight(self, n: int) -> int:
        return Counter([i for i in str(bin(n))[2:]])["1"]
        
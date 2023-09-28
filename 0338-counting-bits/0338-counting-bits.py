class Solution:
    def countBits(self, n: int) -> List[int]:
        lst = []
        for num in range(n+1):
            lst += [Counter([i for i in str(bin(num))[2:]])["1"]]
        return lst
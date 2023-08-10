class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        lst = []
        for i in range(len(candies)):
            if (candies[i] + extraCandies) >= max(candies):
                lst += [True]    
            else:
                lst += [False]
        return lst
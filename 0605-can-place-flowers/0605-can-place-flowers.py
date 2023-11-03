class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        flowerbed = [0] + [0] + flowerbed + [0] + [0]
        i = 2
        print(flowerbed)
        while(i+1 != len(flowerbed) - 1):         
            if flowerbed[i - 1] == 0 and flowerbed[i] == 0 and flowerbed[i + 1] == 0:
                flowerbed[i] = 1
                n -= 1
            
            i += 1
        print(flowerbed)

        if n <= 0:
            return True
        return False

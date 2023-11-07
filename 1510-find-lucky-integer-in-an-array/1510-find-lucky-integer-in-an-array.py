class Solution:
    def findLucky(self, arr: List[int]) -> int:
        counter = {}
        for num in arr:
            if num not in counter:
                counter[num] = 0
            counter[num] += 1

        lst = []
        for key in counter.keys():
            if key == counter[key]:
                lst += [key]
        
        if not lst:
            return -1
        return max(lst)
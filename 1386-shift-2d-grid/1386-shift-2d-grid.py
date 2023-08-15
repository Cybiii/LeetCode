class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        lst = []
        for line in grid:
            lst += line
            size = len(line)

        for _ in range(k):
            lst.insert(0, lst[len(lst) - 1])
            lst.pop()
        
        i = 0
        biglist = []
        while i < len(lst):
            tmp = []
            for _ in range(size):
                tmp += [lst[i]]
                i += 1
            biglist += [tmp]
        return biglist            

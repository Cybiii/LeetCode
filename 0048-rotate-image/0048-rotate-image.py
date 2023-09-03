class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        if len(matrix[0]) == 0:
            pass
        else:
            lst = []
            l = len(matrix[0])
            for i in range(l):
                lst += [matrix[i]]
            for _ in range(l):
                matrix.pop()
            
            for i in range(l):
                lst2 = []
                for j in range(l):
                    lst2 += [lst[j][i]]
                lst2.reverse()
                matrix += [lst2]
                print(lst2)
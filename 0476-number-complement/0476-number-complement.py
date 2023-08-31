class Solution:
    def findComplement(self, num: int) -> int:

        print(bin(num))
        num = str(bin(num))
        num = num[2:]
        
        lst = []
        num = [i for i in num]
        print(num)
        for i in range(len(num)):
            if num[i] == '0':
                lst += [1]
            else:
                lst += [0]

        count = 0
        for i in range(len(lst)):
            j = len(lst) - i - 1
            print(j, i)
            if lst[i] == 1:
                count += pow(2, j)
        return count


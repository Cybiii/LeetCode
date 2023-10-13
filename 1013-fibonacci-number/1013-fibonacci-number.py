class Solution:
    def fib(self, n: int) -> int:
        num = 0
        nextt = 1
        while (n > 0):
            print(num, nextt)
            tmp = num
            num = nextt
            nextt += tmp
            n -= 1
        return num
        
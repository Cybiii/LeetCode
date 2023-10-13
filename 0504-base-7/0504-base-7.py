class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return "0"
        lst = []
        positive = True
        if num < 0:
            positive = False
            num = num*-1
        while (num > 0):
            val = num % 7
            lst += [str(val)]
            num //= 7

        lst.reverse()
        val = "".join(lst)
        if positive != False:
            return val
        return "-" + val

        
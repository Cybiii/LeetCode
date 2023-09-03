class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        num_stack = []
        ops = {'+', '-', '*', '/'}

        for t in tokens:
            if t in ops:
                num2 = num_stack.pop()  
                # num2 is popped before num1 due to the order of operations.
                num1 = num_stack.pop()
                if t == '+':
                    num_stack.append(num1 + num2)
                elif t == '-':
                    num_stack.append(num1 - num2)
                elif t == '*':
                    num_stack.append(num1 * num2)
                else:
                    # Handling division and making sure it's floored division for negative numbers.
                    if num1 * num2 < 0 and num1 % num2 != 0:
                        num_stack.append(num1 // num2 + 1)
                    else:
                        num_stack.append(num1 // num2)
            else:
                num_stack.append(int(t))
                


        return num_stack.pop()
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        temp = deque()
        operators = ['*', '/', '+', '-']
        for token in tokens:
            if token in operators:
                operandOne = temp.pop()
                operandTwo = temp.pop()
                solution = 0
                if token == '*':
                    solution = operandOne * operandTwo
                elif token == '+':
                    solution = operandOne + operandTwo
                elif token == '/':
                    solution = int(operandTwo / operandOne)
                else:
                    solution = operandTwo - operandOne

                temp.append(solution)

            else:
                temp.append(int(token))

        return temp.pop()

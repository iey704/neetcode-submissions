class Solution:
    def calPoints(self, operations: List[str]) -> int:
        result = []
        answer = 0
        for i in range(len(operations)):
            if operations[i] == "+":
                answer = result[-2] + result[-1]
                result.append(answer)
            elif operations[i] == "D":
                answer = (result[-1])*2
                result.append((answer))
            elif operations[i] == "C":
                result.pop()
            else:
                result.append(int(operations[i]))

        return sum(result)
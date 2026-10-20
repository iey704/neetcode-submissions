class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        if n < 3:
            return 1

        a, b, c = 0, 1, 1 # 초기값

        for i in range(3, n + 1):
            next_num = a + b + c  # 기존 세 숫자로 다음 숫자 계산
            a = b                
            b = c
            c = next_num         

        return c
class Solution:
    def guessNumber(self, n: int) -> int:
        num = 0
        left = 1
        right = n
        while left <= right:   
            mid = (left+right)//2         
            result = guess(mid)
            if result == -1:
                # 왼쪽 반쪽 영역 선택
                right = mid-1
            elif result == 1:
                # 오른쪽 반쪽 영역 선택
                left = mid+1
            elif result == 0:
                return mid

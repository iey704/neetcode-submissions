class Solution:
    def orangesRotting(self, grid):
        rows = len(grid)
        cols = len(grid[0])
        minutes = 0

        while True:
            fresh = 0
            targets = []  # 이번 1분이 지나면 썩을 위치

            for r in range(rows):
                for c in range(cols):
                    if grid[r][c] != 1:
                        continue

                    fresh += 1

                    # 상하좌우 중 썩은 과일이 있는지 확인
                    if (
                        (r > 0 and grid[r - 1][c] == 2) or
                        (r < rows - 1 and grid[r + 1][c] == 2) or
                        (c > 0 and grid[r][c - 1] == 2) or
                        (c < cols - 1 and grid[r][c + 1] == 2)
                    ):
                        targets.append((r, c)) # 먼저 썩힐 과일들 위치만 저장

            # 신선한 과일이 없으면 끝
            if fresh == 0:
                return minutes

            # 신선한 과일은 있는데 더 썩힐 수 없으면 실패
            if not targets:
                return -1

            # 모아둔 과일을 한꺼번에 썩히기
            for r, c in targets:
                grid[r][c] = 2

            minutes += 1
class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        total = m * n
        
        # Create an empty result grid
        res = [[0] * n for _ in range(m)]
        
        for r in range(m):
            for c in range(n):
                # Calculate new 1D index
                new_idx = (r * n + c + k) % total
                new_r, new_c = new_idx // n, new_idx % n
                res[new_r][new_c] = grid[r][c]
                
        return res
        
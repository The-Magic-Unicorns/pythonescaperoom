def run(riddle):
    def place_queens(grid):
        size = len(grid)
        for y in range(size):
            for x in range(size):
                if grid[y][x] == 0:
                    if is_valid_position(grid, y, x):
                        grid[y][x] = 1
                        place_queens(grid)
                        if sum(sum(a) for a in grid) == size:
                            return grid
                        grid[y][x] = 0

    def is_valid_position(grid, y, x):
        size = len(grid)
        for i in range(size):
            if grid[y][i] == 1:
                return False
        for i in range(size):
            if grid[i][x] == 1:
                return False
        for i in range(size):
            for j in range(size):
                if grid[i][j] == 1:
                    if abs(i - y) == abs(j - x):
                        return False
        return True

    grid = place_queens(riddle)
    return grid

class MagicSquare:

    dim = 0
    magicNumber = 0
    sum = 0

    def deploy(self, dim):
        self.grid = [[0 for x in range(dim)] for y in range(dim)]
        self.magicNumber = int((dim * dim + 1) * ((dim * dim) / 2))
        self.sum = int(self.magicNumber / dim)
        self.dim = dim
        if dim % 2:
            grid = self.deployOgg(dim, self.grid)
        else:
            grid = self.deployEven(dim, self.grid)

        return grid

    def deployOgg(self, dim, grid):
        row = 0
        col = int(dim / 2)
        val = 1
        for i in range(dim * dim):
            grid[row][col] = val
            if val % dim != 0:
                row = row - 1
                col = col + 1
                if row < 0:
                    row = dim - 1
                if col >= dim:
                    col = 0
            else:
                row = row + 1
            val = val + 1
        return grid

    def deployEven(self, dim, grid):
        if dim % 4 == 0:
            grid = self.deployEven4k(dim, grid)
        else:
            raise NotImplemented
            ## TODO: implement magic square 4k2
            #grid = deployEven4k2(dim, grid)
        return grid

    def deployEven4k(self, dim, grid):
        k = int(dim / 4)
        dim2 = int(2 * k)
        row = 0
        col = 0
        fields = dim * dim
        j = fields
        i = 1
        for x in range(fields):
            if (row < k or row >= dim2 + k) and (col < k or col >= dim2 + k):
                grid[row][col] = j
                j -= 1
            elif (row >= k and row < (dim2 + k)) and (col >= k and col < (dim2 + k)):
                grid[row][col] = j
                j -= 1
            else:
                grid[row][col] = i
                i += 1
            col += 1
            if col >= dim:
                col = 0
                row += 1
        return grid

    def deployEven4k2(self, dim, grid):
        k = int((dim - 2) / 4)
        fields = dim * dim
        col = 0
        row = 0
        i = 1
        print("K: " + str(k))
        for x in range(fields):
            if ((col >= row and col < row + k) or (col >= dim - row - k and col < dim - row)) and (row < dim / 2):
                grid[row][col] = i
            elif ((col >= row - 1 and col < row + k - 1) or (col >= dim - row - k + 1 and col < dim - row + 1)) and (
                    row >= dim / 2):
                grid[row][col] = i
            elif ((col < k / 2) or (col >= dim - k / 2)) and (row >= dim / 2 - 1 and row < dim / 2 + k - 1):
                grid[row][col] = i
            else:
                # grid[row][col] = fields - i
                i = i
            col += 1
            i += 1
            if (col >= dim):
                col = 0
                row += 1

        return grid

    def check(self, grid, checkSum):
        sumCols = [0] *len(grid[0])
        for line in grid:
            sumRow = 0
            i = 0
            for field in line:
                sumRow += field
                sumCols[i] += field
                i += 1
            if int(sumRow) != int(checkSum):
                return False
        for sumCol in sumCols:
            if int(sumCol) != int(checkSum):
                return False

        return True
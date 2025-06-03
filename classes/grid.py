class Grid():
    def __init__(self, grid):
        '''
        Converts the grid format from immutable strings to a matrix - makes it much easier to work with
        '''
        self.num_rows = len(grid)
        self.num_cols = len(grid[0])
        self.grid = [[' ']*self.num_cols for _ in range(self.num_rows)]

        for row in range(self.num_rows):
            for col in range(self.num_cols):
                self.grid[row][col] = grid[row][col]

    def print_grid(self):
        '''
        Prints map to output (with nicer formatting than a list of strings)
        '''
        out_str = ''
        for row in range(self.num_rows):
            for col in range(self.num_cols):
                out_str += self.grid[row][col]
            out_str += '\n'
        print(out_str)

    def replace_tile(self, row, col, new_val):
        '''
        Replaces tile at given row/col to new_val
        '''
        self.grid[row][col] = new_val
    
    def get_tiles(self, val):
        '''
        Returns a set of all (row,col) coords of the symbol given by val
        '''
        coords = set()

        for row in range(self.num_rows):
            for col in range(self.num_cols):
                if self.grid[row][col] == val:
                    coords.add((row,col))
        return coords

    def count_tiles(self, val):
        '''
        Counts the number of tiles in the grid that have the character given by val and returns that value
        '''
        count = 0
        for row in range(self.num_rows):
            for col in range(self.num_cols):
                if self.grid[row][col] == val:
                    count += 1
        return count
    
    def get_relative(self, row, col, dir, step=1, wraparound=False):
        '''
        Gets the relative tile 'step' steps (default 1) in the direction dir from row,col
        Setting wraparound=True allows to traverse from left->right boundaries and top->bottom, and vice versa
        dir: 'left','right','up,'down','nw','ne','sw','se' - last four are diagonals (north west, etc)
        step: int
        wraparound: bool

        output:
        row, col, val - of tile at respective step. If step exceeds boundary and wraparound=False, then error code (-1,-1,'.') is returned
        '''
        row_shift = col_shift = 0

        match dir:
            case 'left' | '<':
                col_shift -= step
            case 'right' | '>':
                col_shift += step
            case 'up' | '^':
                row_shift -= step
            case 'down' | 'v':
                row_shift += step
            case 'nw':
                row_shift -= step
                col_shift -= step
            case 'ne':
                row_shift -= step
                col_shift += step                
            case 'sw':
                row_shift += step
                col_shift -= step
            case 'se':
                row_shift += step
                col_shift += step
        
        # Get new tile row/col
        if wraparound:
            new_row = (row + row_shift) % self.num_rows
            new_col = (col + col_shift) % self.num_cols
        else:
            new_row = (row + row_shift)
            new_col = (col + col_shift)            

        # Check not exceeding boundary
        if new_row < 0 or new_col < 0 or new_row >= self.num_rows or new_col >= self.num_cols:
            return (-1,-1,'.')

        return (new_row, new_col, self.grid[new_row][new_col])



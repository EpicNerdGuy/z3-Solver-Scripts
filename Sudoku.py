from z3 import *

banner = r'''
                                                                        
 ▄▄▄▄▄▄▄          ▄▄                     ▄▄▄▄▄▄▄ ▄▄▄      ▄▄▄ ▄▄▄▄▄▄▄▄▄ 
█████▀▀▀          ██       ▄▄           █████▀▀▀ ████▄  ▄████ ▀▀▀███▀▀▀ 
 ▀████▄  ██ ██ ▄████ ▄███▄ ██ ▄█▀ ██ ██  ▀████▄  ███▀████▀███    ███    
   ▀████ ██ ██ ██ ██ ██ ██ ████   ██ ██    ▀████ ███  ▀▀  ███    ███    
███████▀ ▀██▀█ ▀████ ▀███▀ ██ ▀█▄ ▀██▀█ ███████▀ ███      ███    ███    
                                                                        
                                                                        
'''

def read_sudoku():
    grid = []
    for i in range(9):
        line = input().strip()
        
        if len(line) != 9:
            raise ValueError("Each row/line must contain exactly 9 characters")
        
        row = []
        for ch in line:
            if ch in '0.':
                row.append(0)
            elif ch.isdigit() and '1' <= ch <= '9':
                row.append(int(ch))
            else:
                raise ValueError("Invalid character in Sudoku input")
            
        grid.append(row)
        
    return grid

def sudoku_solver(grid):
    s = Solver()
    
    # 9x9 Int variables
    cells = [[Int(f"x_{i}_{j}") for j in range(9)] for i in range(9)]
    
    
    # Cell constraints
    for i in range(9):
        for j in range(9):
            s.add(And(cells[i][j]>=1, cells[i][j]<=9))
            if grid[i][j] != 0:
                s.add(cells[i][j] == grid[i][j])
    
    # Row and columns
    for i in range(9):
        s.add(Distinct(cells[i]))  
        s.add(Distinct([cells[j][i] for j in range(9)]))
    
    # 3 x 3 subgrids 
    for br in range(3):
        for bc in range(3):
            block = [cells[i][j] for i in range(br*3, br*3+3) for j in range(bc*3, bc*3+3)]
            s.add(Distinct(block))
            
    if s.check() == sat:
        m = s.model()
        sol = [[m.evaluate(cells[i][j]).as_long() for j in range(9)] for i in range(9)]
        return sol
    else:
        print('No solution exists')
        return None
    

def main():
    print(banner)
    print("Enter the Sudoku puzzle (9 lines of 9 characters each, use 0 or . for empty cells):")
    grid = read_sudoku()
    sol = sudoku_solver(grid)
    if sol:
        print("\nSolved Sudoku:")
        for row in sol:
            print(" ".join(str(num) for num in row))
    
    
    
if __name__ == "__main__":
    main()
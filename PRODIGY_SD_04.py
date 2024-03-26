import tkinter as tk

def solve_sudoku():
    def possible(Row, Column, Num):
        for i in range(0, 9):
            if sudoku_puzzle[Row][i] == Num:
                return False
        for i in range(0, 9):
            if sudoku_puzzle[i][Column] == Num:
                return False
        x0 = (Column // 3) * 3
        y0 = (Row // 3) * 3
        for i in range(0, 3):
            for j in range(0, 3):
                if sudoku_puzzle[y0 + i][x0 + j] == Num:
                    return False
        return True

    def solve(sudoku_puzzle):
        for Row in range(0, 9):
            for Column in range(0, 9):
                if sudoku_puzzle[Row][Column] == 0:
                    for Num in range(1, 10):
                        if possible(Row, Column, Num):
                            sudoku_puzzle[Row][Column] = Num
                            solve(sudoku_puzzle)
                            sudoku_puzzle[Row][Column] = 0
                    return
        update_gui(sudoku_puzzle)

    def update_gui(sudoku_puzzle):
        root = tk.Tk()
        root.title("Sudoku Game")
        
        # Set the window size
        root.geometry("400x400")  # Set your desired window size here

        frame = tk.Frame(root)
        frame.pack()

        def display_puzzle(puzzle):
            for i in range(9):
                for j in range(9):
                    if puzzle[i][j] != 0:
                        label = tk.Label(frame, text=str(puzzle[i][j]), font=("Arial", 14))
                        label.grid(row=i, column=j)
                    else:
                        entry = tk.Entry(frame, width=3, font=("Arial", 14))
                        entry.grid(row=i, column=j)
                        entry.insert(0, '')

        display_puzzle(sudoku_puzzle)

        solve_button = tk.Button(root, text="Solve", command=lambda: solve(sudoku_puzzle))
        solve_button.pack()

        root.mainloop()

    sudoku_puzzle = [[5,3,0,0,7,0,0,0,0],
                     [6,0,0,1,9,5,0,0,0],
                     [0,9,8,0,0,0,0,6,0],
                     [8,0,0,0,6,0,0,0,3],
                     [4,0,0,8,0,3,0,0,1],
                     [7,0,0,0,2,0,0,0,6],
                     [0,6,0,0,0,0,2,8,0],
                     [0,0,0,0,1,9,0,0,5],
                     [0,0,0,0,0,0,0,0,0]]

    update_gui(sudoku_puzzle)

solve_sudoku()

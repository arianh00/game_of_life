import tkinter as tk

# Constants
ALIVE_COLOR = '#f3faf2'
DEAD_COLOR = '#292b29'
LINES_COLOR = '#969e96'
CELL_SIZE = 20
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 800

# Global variables
simulation_state = False
grid = [[0 for i in range(WINDOW_WIDTH//CELL_SIZE)] for j in range(WINDOW_HEIGHT//CELL_SIZE)]

# Interacion Functions
def cell_drawer(x, y, status):
    if status == 1:
        color = ALIVE_COLOR
    else:
        color = DEAD_COLOR
    canvas.create_rectangle(x * CELL_SIZE, y * CELL_SIZE, (x + 1) * CELL_SIZE, (y + 1) * CELL_SIZE, outline=LINES_COLOR, fill=color)

def left_click(event):
    if not simulation_state:
        x, y = event.x, event.y
        x = x // CELL_SIZE
        y = y // CELL_SIZE
        if grid[y][x] == 0:
            grid[y][x] = 1
            cell_drawer(x, y, 1)
        else:
            grid[y][x] = 0
            cell_drawer(x, y, 0)

def start_stop_simulation(event):
    if event.char == 'r' and not simulation_state:
        simulation_state = True
        print('Simulation started')
        #commence simulation
    if event.char == 's' and simulation_state:
        simulation_state = False
        print('Simulation stopped')
        #stop simulation

def clear_grid(event):
    if not simulation_state:
        for y, row in enumerate(grid):
            for x, status in enumerate(row):
                grid[y][x] = 0
        draw_grid()

def draw_grid():
    for y, row in enumerate(grid):
        for x, status in enumerate(row):
            cell_drawer(x, y, status)

# Logic Functions

# Create the root window
root = tk.Tk()
root.title('Base')
root.geometry('1000x800')

# Create the canvas
canvas = tk.Canvas(root, bg=DEAD_COLOR)
canvas.pack(expand=True, fill='both')

# Draw the grid
draw_grid()

root.bind('<Button-1>', left_click)
root.bind('<Key>', start_stop_simulation)

# Run the main loop
root.mainloop()
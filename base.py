import tkinter as tk

# explorar el type hinting

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
    global simulation_state
    if event.char == 'r' and not simulation_state:
        simulation_state = True
        print('Simulation started')
        simulation()
    if event.char == 's' and simulation_state:
        simulation_state = False
        print('Simulation stopped')
        #stop simulation

def clear_grid(event):
    global simulation_state
    if event.char == 'c' and not simulation_state:
        for y, row in enumerate(grid):
            for x, status in enumerate(row):
                grid[y][x] = 0
        draw_grid()

def key_press(event):
    start_stop_simulation(event)
    clear_grid(event)

def draw_grid():
    for y, row in enumerate(grid):
        for x, status in enumerate(row):
            cell_drawer(x, y, status)

def simulation():
    global simulation_state
    if simulation_state:
        next_gen()
        draw_grid()
        root.after(200, simulation)

# Logic Functions
def count_neighbors(x, y):
    count = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue
            if 0 <= y + i < len(grid) and 0 <= x + j < len(grid[0]):
                if grid[y + i][x + j] == 1:
                    count += 1
    return count

def next_gen():
    global grid
    new_gen = []
    for y, row in enumerate(grid):
        new_row = []
        for x, status in enumerate(row):
            neighbors = count_neighbors(x, y)
            if status == 1:
                if neighbors < 2 or neighbors > 3:
                    new_row.append(0)
                else:
                    new_row.append(1)
            else:
                if neighbors == 3:
                    new_row.append(1)
                else:
                    new_row.append(0)
        new_gen.append(new_row)
    grid = new_gen
        

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
root.bind('<Key>', key_press)

# Run the main loop
root.mainloop()
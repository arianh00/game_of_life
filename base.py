import tkinter as tk

# Constants
ALIVE_COLOR = '#f3faf2'
DEAD_COLOR = '#292b29'
LINES_COLOR = '#969e96'
CELL_SIZE = 20

# Global variables
simulation_state = False

# Functions
def left_click(event):
    if not simulation_state:
        x, y = event.x, event.y
        x = x // CELL_SIZE * CELL_SIZE
        y = y // CELL_SIZE * CELL_SIZE
        canvas.create_rectangle(x, y, x + CELL_SIZE, y + CELL_SIZE, outline=LINES_COLOR, fill=ALIVE_COLOR)

def start_stop_simulation(event):
    if event.char == 'r' and not simulation_state:
        simulation_state = True
        print('Simulation started')
        #commence simulation
    if event.char == 's' and simulation_state:
        simulation_state = False
        print('Simulation stopped')
        #stop simulation

# Create the root window
root = tk.Tk()
root.title('Base')
root.geometry('1000x800')

# Create the canvas
canvas = tk.Canvas(root, bg=DEAD_COLOR)
canvas.pack(expand=True, fill='both')

# Draw the grid
for i in range(0, 1000, CELL_SIZE):
    canvas.create_line(i, 0, i, 800, fill=LINES_COLOR)
    canvas.create_line(0, i, 1000, i, fill=LINES_COLOR)

root.bind('<Button-1>', left_click)
root.bind('<Key>', start_stop_simulation)

# Run the main loop
root.mainloop()
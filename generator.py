import matplotlib.pyplot as plt
import numpy as np

def generate_lattice(max_y, max_x):
    """
    The Core Logic of the [Your Name] Lattice.
    Generates the basic Divisor Grid.
    """
    # 0 = Composite/Empty, 1 = Divisor Node
    grid = np.zeros((max_y, max_x))

    for y in range(max_y):      # Rows (Integers)
        for x in range(1, max_x + 1):  # Columns (Divisors)
            if y % x == 0:
                grid[y, x-1] = 1 
            
    return grid

# --- CONFIGURATION ---
HEIGHT = 200
WIDTH = 100

print(f"Generating Lattice ({HEIGHT}x{WIDTH})...")
grid = generate_lattice(HEIGHT, WIDTH)

# --- VISUALIZATION ---
plt.figure(figsize=(10, 10))
# Black and White (Binary)
plt.imshow(grid, cmap='binary', interpolation='nearest')

plt.title("The Geometric Prime Lattice\n(Visualizing Divisibility Structures)")
plt.xlabel("Column (Divisor Logic)")
plt.ylabel("Row (Integer Value)")

# Save the master reference image
plt.savefig('diagram_lattice.png')
print("Success: 'diagram_lattice.png' saved.")

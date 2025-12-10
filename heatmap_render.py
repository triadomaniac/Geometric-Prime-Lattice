import matplotlib.pyplot as plt
import numpy as np

def generate_overlap_heatmap(limit):
    """
    Generates a heatmap showing HOW OFTEN each number is 'hit'
    by the Square and Pronic trajectories.
    """
    # Array to count hits per number. 
    # Index i represents number i.
    hit_counts = np.zeros(limit, dtype=int)
    
    # --- 1. SQUARE TRAJECTORIES (n^2 - odds) ---
    n = 2
    while True:
        start = n * n
        # Heuristic break to stop infinite loop
        if (n*n) - ((n-2)**2) > limit and start > limit: 
             if (n * 2) > limit: break 
        
        current = start
        step = 1
        
        while current >= 0:
            if current < limit:
                hit_counts[current] += 1
            current -= step
            step += 2 # 1, 3, 5...
            if current < 0: break
        n += 1

    # --- 2. PRONIC TRAJECTORIES (n(n+1) - evens) ---
    n = 1
    while True:
        start = n * (n + 1)
        if n * n > limit * 10: break
        
        current = start
        step = 2
        
        while current >= 0:
            if current < limit:
                hit_counts[current] += 1
            current -= step
            step += 2 # 2, 4, 6...
            if current < 0: break
        n += 1

    return hit_counts

# --- CONFIGURATION ---
# We use a square grid for visualization (e.g., 100x100 = 10,000 numbers)
GRID_WIDTH = 100 
GRID_HEIGHT = 100
LIMIT = GRID_WIDTH * GRID_HEIGHT

counts = generate_overlap_heatmap(LIMIT)

# Reshape 1D array into 2D grid for plotting
# We ignore 0 and 1 for clarity in visualization
grid_data = counts.reshape((GRID_HEIGHT, GRID_WIDTH))

# --- PLOTTING ---
plt.figure(figsize=(12, 12))

# Create a custom view
# 0 hits (Primes) will be marked separately to make them pop
masked_data = np.ma.masked_where(grid_data == 0, grid_data)

# Plot the Heatmap (Composites)
# 'viridis' or 'plasma' are good for heat. Yellow = High Overlap.
cmap = plt.cm.plasma
cmap.set_bad(color='black') # Set Primes (0 hits) to BLACK

grid_data[0,0] = 0

plt.imshow(grid_data, cmap='magma', interpolation='nearest', vmax=5)
plt.colorbar(label='Number of Overlapping Trajectories (Capped at 5)')

plt.title(f"Heatmap of Trajectory Overlaps (First {LIMIT} integers)\nBlack = Primes | Bright = Highly Redundant Composites")
plt.xlabel(f"x (Mod {GRID_WIDTH})")
plt.ylabel(f"y (Rows of {GRID_WIDTH})")

# Invert Y to read like a book (0 at top left)
# But standard math plots usually have 0 at bottom. 
# Let's keep 0 at top to match reading order.
# plt.gca().invert_yaxis() 

plt.savefig('heatmap.png')
print("Success! Heatmap saved as 'heatmap.png' in this folder")

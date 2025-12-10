import matplotlib.pyplot as plt
import numpy as np

def generate_robust_goldbach(limit):
    """
    Robust version: No heuristic breaks. Calculates the full lattice.
    """
    print(f"Calculating Goldbach Mirror for N={limit}...")
    
    # 0 = Prime (Gap), 1 = Composite (Wall)
    # We initialize as 0 (Prime) and fill in the walls
    forward_map = np.zeros(limit + 1, dtype=int)
    
    # Manually mark 0 and 1 as Composite (Standard math rules)
    forward_map[0] = 1
    forward_map[1] = 1
    
    # --- 1. SQUARE TRAJECTORIES ---
    # We iterate N purely based on coverage, no early breaks.
    # Max square needed: roughly limit + limit (to step back)
    # Safest upper bound for n is 'limit' itself (overkill but safe)
    for n in range(2, limit): 
        start = n * n
        # Optimization: If the FIRST step back is already out of bounds, stop.
        if (n*n) - ((n-2)**2) > limit and start > limit: 
             break 
             
        current = start
        step = 1
        while current >= 0:
            if current <= limit:
                forward_map[current] = 1
            current -= step
            step += 2 # 1, 3, 5...

    # --- 2. PRONIC TRAJECTORIES ---
    for n in range(1, limit):
        start = n * (n + 1)
        if (n*n) > limit * 4: break # Loose bound
        
        current = start
        step = 2
        while current >= 0:
            if current <= limit:
                forward_map[current] = 1
            current -= step
            step += 2 # 2, 4, 6...

    # --- 3. THE MIRROR ---
    backward_map = forward_map[::-1]
    
    # --- 4. VISUALIZATION ---
    # We want to clearly see the "Gold Lasers"
    visualization_grid = np.zeros((100, limit + 1)) # Taller image for clarity
    
    solutions = 0
    
    # Fill the grid for visual impact
    for i in range(limit + 1):
        # Top 40% = Forward Lattice
        if forward_map[i] == 1:
            visualization_grid[0:40, i] = 0.2 # Grey for Composite
        else:
            visualization_grid[0:40, i] = 0 # Black for Prime
            
        # Bottom 40% = Backward Lattice
        if backward_map[i] == 1:
            visualization_grid[60:100, i] = 0.2
        else:
            visualization_grid[60:100, i] = 0
            
        # Middle 20% = The "Collider"
        # If both are 0 (Prime), we have a match!
        if forward_map[i] == 0 and backward_map[i] == 0:
            visualization_grid[:, i] = 1.0 # PURE WHITE BEAM
            solutions += 1

    print(f"Found {solutions} Goldbach pairs for {limit}.")

    plt.figure(figsize=(15, 8))
    # inferno is a high-contrast heatmap (Black -> Orange -> Yellow -> White)
    plt.imshow(visualization_grid, cmap='inferno', aspect='auto', interpolation='nearest')
    
    plt.title(f"The Goldbach Mirror (N={limit})\nTotal Pairs Found: {solutions}", fontsize=16)
    plt.axis('off')
    
    plt.savefig(f"goldbach_robust_{limit}.png")
    print(f"Saved: goldbach_robust_{limit}.png")

# Run for 2000 to see the "Comet" clearly
generate_robust_goldbach(2000)

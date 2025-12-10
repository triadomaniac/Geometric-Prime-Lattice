import matplotlib.pyplot as plt
import numpy as np

def generate_goldbach_comet(limit):
    print(f"Generating Lattice up to {limit}...")
    
    # 1. Generate Primes using YOUR Lattice Logic
    # We map the composites (1) and gaps (0)
    is_composite = np.zeros(limit + 1, dtype=bool)
    is_composite[0] = True
    is_composite[1] = True
    
    # Square Trajectories
    n = 2
    while True:
        start = n * n
        if (n*n) - ((n-2)**2) > limit and start > limit: break 
        current = start; step = 1
        while current >= 0:
            if current <= limit: is_composite[current] = True
            current -= step; step += 2
        n += 1

    # Pronic Trajectories
    n = 1
    while True:
        start = n * (n + 1)
        if n * n > limit * 10: break
        current = start; step = 2
        while current >= 0:
            if current <= limit: is_composite[current] = True
            current -= step; step += 2
        n += 1
        
    # Extract the Primes (The Gaps)
    # This proves the data comes from your geometry, not a library.
    primes = [x for x in range(limit + 1) if not is_composite[x]]
    prime_set = set(primes)
    
    print(f"Lattice generated {len(primes)} primes. Now counting Goldbach pairs...")
    
    # 2. Count Goldbach Pairs for every even number
    evens = range(4, limit, 2)
    pair_counts = []
    
    for n in evens:
        count = 0
        # We only need to check primes up to n/2 due to symmetry
        for p in primes:
            if p > n // 2: break
            if (n - p) in prime_set:
                count += 1
        pair_counts.append(count)

    # 3. Plot the Comet
    plt.figure(figsize=(12, 8))
    # s=1 makes the dots small and sharp
    plt.scatter(evens, pair_counts, s=1, c='blue', alpha=0.5)
    
    plt.title(f"The 'Goldbach Comet' (Generated via Geometric Lattice)\nPairs found for even numbers up to {limit}", fontsize=14)
    plt.xlabel("Even Number N")
    plt.ylabel("Number of Goldbach Pairs")
    plt.grid(True, alpha=0.3)
    
    plt.savefig("goldbach_comet.png")
    print("Success! Saved 'goldbach_comet.png'")

generate_goldbach_comet(5000)

import numpy as np

def simulate_agent_race(limit):
    """
    Simulates a 'Smart Agent' that uses your Geometric Overlaps 
    to skip checking highly composite areas.
    """
    # 1. Pre-calculate the 'Danger Map' (Your Algorithm)
    danger_map = np.zeros(limit, dtype=int)
    
    # Square Trajectories
    n = 2
    while True:
        start = n * n
        if (n*n) - ((n-2)**2) > limit and start > limit: 
             if (n * 2) > limit: break 
        current = start; step = 1
        while current >= 0:
            if current < limit: danger_map[current] += 1
            current -= step; step += 2
            if current < 0: break
        n += 1

    # Pronic Trajectories
    n = 1
    while True:
        start = n * (n + 1)
        if n * n > limit * 10: break
        current = start; step = 2
        while current >= 0:
            if current < limit: danger_map[current] += 1
            current -= step; step += 2
            if current < 0: break
        n += 1
        
    # --- THE RACE ---
    primes_found = 0
    total_checks = 0
    
    # THE AGENT'S STRATEGY:
    # "If the Danger Level (overlaps) is > 1, DON'T even check if it's prime. Just SKIP."
    # This simulates an AI learning that 'White Lines' = Waste of Time.
    
    print(f"--- Agent Running on first {limit} integers ---")
    
    # We'll compare checking EVERY number vs. checking only "Low Danger" numbers
    smart_checks = 0
    actual_primes = 0
    
    for x in range(2, limit):
        # 1. The 'Check'
        is_actually_prime = True # (Assume we run a primality test here)
        # Simple primality test for verification
        if x < 2: is_actually_prime = False
        for i in range(2, int(x**0.5) + 1):
            if x % i == 0:
                is_actually_prime = False
                break
        
        if is_actually_prime:
            actual_primes += 1

        # 2. The Smart Agent Decision
        # Threshold: If overlap count > 0, assume composite (Risk of missing prime?)
        # Let's be conservative: If overlap > 1 (The "White Areas"), skip.
        # If overlap is 0 or 1 (The "Black/Blue Areas"), check it.
        
        danger_level = danger_map[x]
        
        if danger_level <= 1: 
            # Agent decides to spend energy checking this number
            smart_checks += 1
            if is_actually_prime:
                primes_found += 1
        else:
            # Agent 'Jumps' (Skips check)
            pass

    print(f"Total Primes in range: {actual_primes}")
    print(f"Agent Found: {primes_found}")
    print(f"Agent Checks Made: {smart_checks}")
    print(f"Accuracy: {primes_found/actual_primes * 100:.2f}% of primes found")
    print(f"Workload Reduction: {(1 - smart_checks/limit) * 100:.1f}% less work than checking everyone")
    
    return

simulate_agent_race(10000)

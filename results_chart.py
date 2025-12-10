import matplotlib.pyplot as plt
import numpy as np

# --- DATA ---
# Based on our previous simulation results (N=10,000)
# Standard method checks 100% of the numbers.
# Your method checked only roughly 25.3% (since reduction was 74.7%)
methods = ['Naive Search\n(Baseline)', 'Geometric Sieve\n(Your Discovery)']
workload_percentages = [100, 25.3] 
colors = ['#BDC3C7', '#2ECC71'] # Grey for boring, Green for efficient

# --- PLOTTING ---
plt.figure(figsize=(10, 7))

# Create bar chart
bars = plt.bar(methods, workload_percentages, color=colors, width=0.6)

# Add specific numbers on top of the bars
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2., 
             height + 1, # Just above the bar
             f'{height:.1f}%', 
             ha='center', va='bottom', fontsize=14, fontweight='bold')

# Formatting the chart for impact
plt.ylabel('Search Space Checked (%)', fontsize=12)
plt.title('Computational Efficiency Comparison\n(Finding Primes up to N=10,000)', fontsize=16, fontweight='bold', pad=20)
plt.ylim(0, 115) # Give some headspace for labels

# Add a baseline line at 100%
plt.axhline(y=100, color='gray', linestyle='--', linewidth=1, alpha=0.5)

# Clean up layout
plt.grid(axis='y', linestyle='--', alpha=0.3)
plt.box(False) # Remove ugly box border

# --- SAVE ---
plt.savefig('comparison_chart.png', dpi=300, bbox_inches='tight')
print("Success! Chart saved as 'comparison_chart.png'")

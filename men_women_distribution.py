import matplotlib.pyplot as plt
import numpy as np

# Define pie chart sections
sizes = [58, 42]  # 58% male, 42% female
colors = ['#3498db', '#e74c3c']  # Blue for male, Red for female
symbols = ['♂', '♀']
angles = np.cumsum([0] + sizes) * 360 / sum(sizes)

# Create figure
fig, ax = plt.subplots(figsize=(6, 6), dpi=100)
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.set_xticks([])
ax.set_yticks([])
ax.set_frame_on(False)

# Scatter symbols within their respective pie sections
num_symbols = 10000
symbol_size = 0.08  # Define minimum spacing between symbols
placed_positions = []
np.random.seed(42)
for i, symbol in enumerate(symbols):
    count = 0
    while count < num_symbols:
        theta = np.random.uniform(angles[i], angles[i + 1]) * np.pi / 180
        r = np.sqrt(np.random.uniform(0.3, 1))  # Leave space in the center
        x = r * np.cos(theta)
        y = r * np.sin(theta)

        # Check if new position overlaps with existing ones
        if all(np.linalg.norm(np.array([x, y]) - np.array(p)) > symbol_size for p in placed_positions):
            ax.text(x, y, symbol, color=colors[i], fontsize=8, ha='center', va='center')
            placed_positions.append((x, y))

        count += 1


# Add percentage labels in the center
ax.text(0, 0.2, 'Men\n58%', color='#3498db', fontsize=14, ha='center', va='center', fontweight='bold')
ax.text(0, -0.2, 'Women\n42%', color='#e74c3c', fontsize=14, ha='center', va='center', fontweight='bold')

# Display the chart
plt.show()
